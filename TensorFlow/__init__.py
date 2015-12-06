import tensorflow as tf

#1x2 matrix
matrix1 = tf.constant([[3., 3.]])

#2x1 matrix
matrix2 = tf.constant([[2.],[2.]])

#multiply
product = tf.matmul(matrix1,matrix2)
product_rev = tf.matmul(matrix2,matrix1)

sess = tf.InteractiveSession()

result = sess.run(product)
print(result)

result2 = sess.run(product_rev)
print(result2)

x = tf.Variable([1.0,2.0])
a = matrix1

#Have to initialize before using the variable
x.initializer.run()

sub = tf.sub(x,a)

# Variables
state = tf.Variable(0,name="counter")
one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)

init_op = tf.initialize_all_variables()

sess.run(init_op)
print(state.eval())

for i in range (3):
    sess.run(update)
    print(state.eval())

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = input2 + input3
mul = input1 * intermed

sess.run([mul,intermed])

input1 = tf.placeholder(tf.types.float32)
input2 = tf.placeholder(tf.types.float32)
output = tf.mul(input1, input2)

sess.run([output],feed_dict = {input1:[3],input2:[7.]})