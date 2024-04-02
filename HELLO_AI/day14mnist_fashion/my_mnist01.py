import tensorflow as tf
from tensorflow import keras
# 0 : T-shirt/top
# 1 : Trouser
# 2 : Pullover
# 3 : Dress
# 4 : Coat
# 5 : Sandal
# 6 : Shirt
# 7 : Sneaker
# 8 : Bag
# 9 : Ankel boot
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0
print(x_train)
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation=tf.nn.tanh),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train,epochs=1)

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)