import tensorflow as tf

with tf.Session() as sess:
    p = tf.placeholder(tf.float32)
    t = p + 1.0
    print(sess.run(t, feed_dict={p:2.0}))
    #t.eval()  # This will fail, since the placeholder did not get a value.
    print(t.eval(feed_dict={p:3.0}))  # This will succeed because we're feeding a value
                            # to the placeholder.
    print(t)