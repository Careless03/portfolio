import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers

# ALGO LOGIC: initialize agent here:


class QNetwork(keras.Model):
    def __init__(self, obs_shape, n_actions):
        super().__init__()
        flat_dim = int(np.prod(obs_shape))
        self.net = keras.Sequential(
            [
                layers.Input(shape=(flat_dim,)),
                layers.Dense(256, activation="relu"),
                layers.Dense(128, activation="relu"),
                layers.Dense(64, activation="relu"),
                layers.Dense(n_actions, activation=None),
            ]
        )

    def call(self, x):
        # x expected shape: (batch, *obs_shape)
        x = tf.reshape(x, [tf.shape(x)[0], -1])
        return self.net(x)
