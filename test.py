import tensorflow as tf
import os

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#
# result = tf.constant("Tensorflow is EZ!!")
# sess = tf.Session()
# print(str(sess.run(result),encoding='utf8'))

# y = tf.constant(3)
# sess = tf.Session()
# result = sess.run(y)
# print(result)

var_1 = tf.Variable(3)
var_2 = tf.Variable(10)
result_sum = var_1 + var_2
init = tf.global_variables_initializer()     # 초기화 함수 추가
sess = tf.Session()
sess.run(init)                 	      # 초기화된 결과를 세센에 전달
print(sess.run(result_sum))


