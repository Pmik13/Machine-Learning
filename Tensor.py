import random
import tensorflow as tf
import numpy as np

np.random.seed(50)

def init():
    N = 1
    X = tf.Variable(np.random.uniform(-N, N), trainable=True)
    Y = tf.Variable(np.random.uniform(-N, N), trainable=True)
    return X, Y

def function(X, Y):
    return (3 * X**4 + 4 * X**3 - 12 * X**2 + 12 * Y**2 - 24 * Y)

X, Y = init()
min_value = function(X.numpy(), Y.numpy())

for i in range(5):
    optimizer = tf.optimizers.SGD(learning_rate=0.01, momentum=0.0)

    for epoch in range(1000):
        with tf.GradientTape() as tape:
            loss = function(X, Y)
        grads = tape.gradient(loss, [X, Y])
        clipped_grads = [tf.clip_by_value(g, -10.0, 10.0) for g in grads]
        optimizer.apply_gradients(zip(clipped_grads, [X, Y]))

    print(f"\nFinal: X={X.numpy()}, Y={Y.numpy()}, f(X,Y)={function(X, Y).numpy()}")
    X, Y = init()
