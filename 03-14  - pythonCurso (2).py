import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

#print("Versión de TensorFlow: ", tf.__version__) mirar la version de keras y se está instalado

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
"""
print("cantidad de imagenes de entrenamento", len(x_train))
print("cantidad de imagenes de entrenamento", len(y_train))
"""
x_train, x_test =x_train/255.0,x_test/255.0
"""  
plt.imshow(x_train[0],cmap="gray") # muestra el numero 5
plt.show()
"""
#Definir la rede neuronal
modelo = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dense(10,activation='softmax')])

modelo.compile(
    optimizer='adam', 
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

modelo.fit(x_train,y_train, epochs=4)

predicciones=modelo.predict(np.expand_dims(x_test[0],axis=0))
print(f"la IA predice {np.argmax(predicciones)}")
#print(x_test,"\n\n",x_train)
