
import sys
import gymnasium as gym
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from QNetwork import QNetwork


# class QNetwork(keras.Model):
#     def __init__(self, obs_shape, n_actions):
#         super().__init__()
#         flat_dim = int(np.prod(obs_shape))
#         self.net = keras.Sequential(
#             [
#                 layers.Input(shape=(flat_dim,)),
#                 layers.Dense(120, activation="relu"),
#                 layers.Dense(84, activation="relu"),
#                 layers.Dense(n_actions, activation=None),
#             ]
#         )

#     def call(self, x):
#         # x expected shape: (batch, *obs_shape)
#         x = tf.reshape(x, [tf.shape(x)[0], -1])
#         return self.net(x)


if __name__ == "__main__":

    path = sys.argv[1]
    # make_env('CartPole-v1', 0, 0, False, "Eval_Run_0")#gym.make('CartPole-v1',render_mode="human")
    env = gym.make('LunarLander-v3', render_mode="human")
    obs_shape = np.prod(env.observation_space.shape)
    n_actions = env.action_space.n
    policy = QNetwork(obs_shape, n_actions)
    dummy_input = np.expand_dims(env.reset()[0], axis=0).astype(np.float32)
    policy(dummy_input)

    policy.load_weights(path)
    obs, _ = env.reset()
    r = 0
    steps = 0
    rew = 0
    term = False
    trunc = False
    while True:
        obs_tensor = np.expand_dims(obs, axis=0).astype(
            np.float32)  # add batch dim
        vals = policy(obs_tensor)
        action = int(np.argmax(vals.numpy()))
        obs, rew, term, trunc, _ = env.step(action)
        r += rew
        steps += 1
        if term or trunc or steps >= 500:
            break
    print("Number Steps: ", steps, " Final Reward: ", r)
