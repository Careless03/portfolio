# docs and experiment results can be found at https://docs.cleanrl.dev/rl-algorithms/dqn/#dqnpy
import time
import random
import os
from dataclasses import dataclass

import tyro
import tensorflow as tf
from tensorflow import keras
import numpy as np
import gymnasium as gym
from stable_baselines3.common.buffers import ReplayBuffer
from QNetwork import QNetwork


@dataclass
class Args:
    exp_name: str = os.path.basename(__file__)[: -len(".py")]
    """the name of this experiment"""
    seed: int = 1
    """seed of the experiment"""
    deterministic: bool = True
    """if toggled, `tf.config.experimental.enable_op_determinism()`"""
    cuda: bool = True
    """if toggled, cuda will be enabled by default"""
    track: bool = False
    """if toggled, this experiment will be tracked with Weights and Biases"""
    wandb_project_name: str = "cleanRL"
    """the wandb's project name"""
    wandb_entity: str = None
    """the entity (team) of wandb's project"""
    capture_video: bool = False
    """whether to capture videos of the agent performances (check out `videos` folder)"""
    save_model: bool = True
    """whether to save model into the `runs/{run_name}` folder"""
    upload_model: bool = False
    """whether to upload the saved model to huggingface"""
    hf_entity: str = ""
    """the user or org name of the model repository from the Hugging Face Hub"""

    # Algorithm specific arguments
    env_id: str = "LunarLander-v3"
    """the id of the environment"""
    total_timesteps: int = 200000
    """total timesteps of the experiments"""
    learning_rate: float = 5e-4
    """the learning rate of the optimizer"""
    num_envs: int = 1
    """the number of parallel game environments"""
    buffer_size: int = 50000
    """the replay memory buffer size"""
    gamma: float = 0.995
    """the discount factor gamma"""
    tau: float = 1.0
    """the target network update rate"""
    target_network_frequency: int = 500
    """the timesteps it takes to update the target network"""
    batch_size: int = 64
    """the batch size of sample from the reply memory"""
    start_e: float = 1.0
    """the starting epsilon for exploration"""
    end_e: float = 0.05
    """the ending epsilon for exploration"""
    exploration_fraction: float = 0.8
    """the fraction of `total-timesteps` it takes from start-e to go end-e"""
    learning_starts: int = 2000
    """timestep to start learning"""
    train_frequency: int = 4
    """the frequency of training"""


def make_env(env_id, seed, idx, capture_video, run_name):
    def thunk():
        if capture_video and idx == 0:
            env = gym.make(env_id, render_mode="rgb_array")
            env = gym.wrappers.RecordVideo(env, f"videos/{run_name}")
        else:
            env = gym.make(env_id)
        env = gym.wrappers.RecordEpisodeStatistics(env)
        env.action_space.seed(seed)

        return env

    return thunk


def linear_schedule(start_e: float, end_e: float, duration: int, t: int):
    slope = (end_e - start_e) / duration
    return max(slope * t + start_e, end_e)


@tf.function
def train_step(q_network, target_network, optimizer, obs, next_obs, actions, rewards, dones, gamma):

    target_q_next = target_network(next_obs)
    target_max = tf.reduce_max(target_q_next, axis=1)
    td_target = rewards + gamma * target_max * (1.0 - dones)

    with tf.GradientTape() as tape:
        q_vals = q_network(obs)
        indices = tf.stack(
            [tf.range(tf.shape(actions)[0]), tf.squeeze(actions)], axis=1)
        q_s_a = tf.gather_nd(q_vals, indices)
        loss = tf.reduce_mean(tf.square(td_target - q_s_a))

    grads = tape.gradient(loss, q_network.trainable_variables)
    optimizer.apply_gradients(zip(grads, q_network.trainable_variables))
    return loss, tf.reduce_mean(q_s_a)


if __name__ == "__main__":
    args = tyro.cli(Args)
    run_name = f"{args.env_id}__{args.exp_name}__{args.seed}__{int(time.time())}"

    # TensorBoard writer
    logdir = f"runs/{run_name}"
    writer = tf.summary.create_file_writer(logdir)

    # TRY NOT TO MODIFY: seeding
    random.seed(args.seed)
    np.random.seed(args.seed)
    tf.random.set_seed(args.seed)
    if args.deterministic:
        tf.config.experimental.enable_op_determinism()

    # env setup
    envs = gym.vector.SyncVectorEnv(
        [make_env(args.env_id, args.seed + i, i, args.capture_video, run_name)
         for i in range(args.num_envs)]
    )
    assert isinstance(envs.single_action_space,
                      gym.spaces.Discrete), "only discrete action space is supported"

    obs_shape = envs.single_observation_space.shape
    n_actions = envs.single_action_space.n

    q_network = QNetwork(obs_shape, n_actions)
    target_network = QNetwork(obs_shape, n_actions)
    # Build networks (call once to create weights)
    dummy_obs = np.zeros((1, *obs_shape), dtype=np.float32)
    q_network(dummy_obs)
    target_network(dummy_obs)
    # Copy weights
    target_network.set_weights(q_network.get_weights())

    optimizer = keras.optimizers.Adam(learning_rate=args.learning_rate)
    mse_loss = keras.losses.MeanSquaredError()

    # Replay buffer
    rb = ReplayBuffer(
        buffer_size=args.buffer_size,
        observation_space=envs.single_observation_space,
        action_space=envs.single_action_space,
        device="cpu",  # returns numpy
        handle_timeout_termination=False,
        n_envs=args.num_envs,
    )

    start_time = time.time()

    # TRY NOT TO MODIFY: start the game
    obs, _ = envs.reset(seed=args.seed)
    # obs shape: (num_envs, *obs_shape)
    obs = obs.astype(np.float32)

    for global_step in range(args.total_timesteps):
        # ALGO LOGIC: put action logic here
        epsilon = linear_schedule(
            args.start_e, args.end_e, args.exploration_fraction * args.total_timesteps, global_step)
        if random.random() < epsilon:
            actions = np.array([envs.single_action_space.sample()
                               for _ in range(envs.num_envs)])
        else:
            # compute q values
            obs_tensor = tf.convert_to_tensor(obs, dtype=tf.float32)
            q_values = q_network(obs_tensor)  # shape (num_envs, n_actions)
            actions = tf.argmax(q_values, axis=1).numpy().astype(np.int32)

        # TRY NOT TO MODIFY: execute the game and log data.
        next_obs, rewards, terminations, truncations, infos = envs.step(
            actions)
        next_obs = next_obs.astype(np.float32)

        # TRY NOT TO MODIFY: record rewards for plotting purposes
        if "final_info" in infos:
            for info in infos["final_info"]:
                if info and "episode" in info:
                    print(
                        f"global_step={global_step}, episodic_return={info['episode']['r']}")
                    with writer.as_default():
                        tf.summary.scalar("charts/episodic_return",
                                          info["episode"]["r"], step=global_step)
                        tf.summary.scalar("charts/episodic_length",
                                          info["episode"]["l"], step=global_step)

        # TRY NOT TO MODIFY: save data to reply buffer; handle `final_observation`
        real_next_obs = next_obs.copy()
        for idx, trunc in enumerate(truncations):
            if trunc:
                # infos["final_observation"][idx]
                real_next_obs[idx] = next_obs

        rb.add(obs, real_next_obs, actions, rewards, terminations, infos)

        # TRY NOT TO MODIFY: CRUCIAL step easy to overlook
        obs = next_obs

        # ALGO LOGIC: training.
        if global_step > args.learning_starts:
            if global_step % args.train_frequency == 0:
                # Sample for past transitions
                batch = rb.sample(args.batch_size)
                b_obs = batch.observations.cpu().numpy().astype(np.float32)
                b_next_obs = batch.next_observations.cpu().numpy().astype(np.float32)
                b_actions = batch.actions.cpu().numpy().astype(np.int32).flatten()
                b_rewards = batch.rewards.cpu().numpy().flatten().astype(np.float32)
                b_dones = batch.dones.cpu().numpy().astype(np.float32).flatten()
                loss, q_mean = train_step(q_network, target_network, optimizer,
                                          b_obs, b_next_obs, b_actions, b_rewards, b_dones, args.gamma)

                if global_step % 100 == 0:
                    with writer.as_default():
                        tf.summary.scalar(
                            "losses/td_loss", loss.numpy(), step=global_step)
                        tf.summary.scalar("losses/q_values",
                                          q_mean.numpy(), step=global_step)
                        sps = int(global_step /
                                  (time.time() - start_time + 1e-8))
                        tf.summary.scalar(
                            "charts/SPS", sps, step=global_step)

                    print("SPS:", sps)

            # update target network
            if global_step % args.target_network_frequency == 0:
                if args.tau == 1.0:
                    # hard update
                    target_network.set_weights(q_network.get_weights())
                else:
                    # polyak update
                    q_weights = q_network.get_weights()
                    target_weights = target_network.get_weights()
                    new_weights = []
                    for tw, qw in zip(target_weights, q_weights):
                        new_weights.append(
                            args.tau * qw + (1.0 - args.tau) * tw)
                    target_network.set_weights(new_weights)

    if args.save_model:
        model_path = f"runs/{run_name}/{args.exp_name}.weights.h5"
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        q_network.save_weights(model_path)
        print(f"model saved to {model_path}")

    envs.close()
    writer.close()
