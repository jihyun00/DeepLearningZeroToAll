import tensorflow as tf

# a, b가 각각 placeholder 라는 노드
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

# a, b 노드를 이용해서 a + b 라는 새로운 노드를 만듦
adder_node = a + b

sess = tf.Session()

# feed_dict 를 통해서 값을 넘겨줌
print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4]}))
