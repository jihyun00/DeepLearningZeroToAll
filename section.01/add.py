import tensorflow as tf


# 3 이라는 상수의 node를 만듦
node1 = tf.constant(3.0, tf.float32)
# 4 라는 노드 생성
node2 = tf.constant(4.0)
# 더하기 노드를 만듦
node3 = tf.add(node1, node2)

# 그냥 각각이 node 이므로 node 에 대한 내용 출력
print("node1 : ",  node1, "node2 : ", node2)
print("node3 : ", node3)

# session을 만들어서 실행시켜야 우리가 원하는 값이 보임
sess = tf.Session()
print("sess.run(node1, node2): ", sess.run([node1, node2]))
print("sess.run(node3): ", sess.run(node3))
