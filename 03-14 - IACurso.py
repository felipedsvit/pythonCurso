import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image

imagen_path = "at.jpg"  # Especifica la ruta de tu archivo PNG

imagen = Image.open(imagen_path).convert('L')  # Convertir a escala de grises

imagen = imagen.resize((28, 28))

imagen_array = np.array(imagen)

imagen_array = imagen_array / 255.0

imagen_array = np.expand_dims(imagen_array, axis=0)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

modelo = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

modelo.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

modelo.fit(x_train, y_train, epochs=4)

predicciones = modelo.predict(imagen_array)

print(f"La IA predice: {np.argmax(predicciones)}")

