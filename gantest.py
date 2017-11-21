import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, activation_funtion=None):
    #add one more layer and return the output of the layer
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_plus_b=tf.matmul(inputs,Weights)+biases
    if activation_funtion is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_funtion(Wx_plus_b)
    return outputs

#make up some real data

x_data=np.linspace(-1,1,300)[:,np.newaxis]
noise=np.random.normal(0,0.05,x_data.shape)
y_data=np.square(x_data)-0.5+noise

#define placeholder for inputs to network
xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])


#add hidden layer
l1=add_layer(xs,1,10,activation_funtion=tf.nn.relu)
prediction=add_layer(l1,10,1,activation_funtion=None)


#the error between prediction and real data

loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))

#train optimizer
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#initialization
init=tf.initialize_all_variables()
sess=tf.Session()

sess.run(init)

for i in range(1000):
    sess.run(train_step,feed_dict={xs: x_data, ys:y_data})
    if i%50 == 0:
        print sess.run(loss,feed_dict={xs:x_data,ys:y_data})
