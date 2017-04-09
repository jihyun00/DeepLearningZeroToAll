import tensorflow as tf


# hello 라는 tensorflow Node를 만들고
hello = tf.constant('Hello, Tensorflow!')

# session 을 통해서
sess = tf.Session()

# 실행시킴
print(sess.run(hello))
