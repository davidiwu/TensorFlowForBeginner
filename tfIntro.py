import numpy as np
import tensorflow as tf

x = tf.constant([[1], [2], [3], [4]], dtype=tf.float32)
y_true = tf.constant([[0], [-1], [-2], [-3]], dtype=tf.float32)

linear_model = tf.layers.Dense(units=1)

y_pred = linear_model(x)
loss = tf.losses.mean_squared_error(labels=y_true, predictions=y_pred)

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

# `sess.graph` provides access to the graph used in a `tf.Session`.
# run cmd to launch tensorboard: tensorboard --logdir=/tmp/log/
writer = tf.summary.FileWriter("/tmp/log/", sess.graph)

for i in range(100):
  loss_value = sess.run((train, loss))
  print(loss_value)

print(sess.run(y_pred))

writer.close()