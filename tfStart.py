
# this is a comment

"""
this is a multiple line comments?
I hope so

"""

import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')

sess = tf.Session()

temp = sess.run(hello)

print(temp)