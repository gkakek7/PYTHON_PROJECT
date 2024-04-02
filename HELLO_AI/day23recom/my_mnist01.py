import tensorflow as tf
import numpy as np

# 0. 짜장
# 1. 삼겹살
# 2. 전복죽
# 3. 킹크랩
# 4. 라면
x_train = np.array([
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1],
])

y_train = np.array([
    1,2,3,4,0
])

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(5,)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(5, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)



pred = model.predict(x_train)
model.save('recom.h5')

for idx, p in enumerate(pred):
    print(np.argmax(p),p)
    
x_rf = np.array([
    [0,0,1,0,0]
])

pred_rf=model.predict(x_rf)

print(np.argmax(pred_rf))