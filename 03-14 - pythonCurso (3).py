import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Cargar el modelo previamente entrenado (asumimos que ya tienes el modelo entrenado y guardado como 'modelo.h5')
modelo = keras.datasets.mnist.load_data()  # Carga tu modelo aquí

# Función para cargar y preprocesar la imagen
def preparar_imagen(imagen_path):
    # Cargar la imagen
    img = Image.open(imagen_path).convert('L')  # Convertir la imagen a escala de grises
    img = img.resize((28, 28))  # Redimensionar la imagen a 28x28 píxeles
    img_array = np.array(img)  # Convertir la imagen a un arreglo de numpy
    
    # Normalizar la imagen a un rango de 0 a 1
    img_array = img_array / 255.0
    
    # Asegurar que tiene la forma correcta (1, 28, 28, 1)
    img_array = np.expand_dims(img_array, axis=-1)  # Agregar una dimensión extra para canal de color
    img_array = np.expand_dims(img_array, axis=0)  # Hacer que la forma sea (1, 28, 28, 1)
    
    return img_array

# Ruta de la imagen que deseas predecir
ruta_imagen = 'C:\\Intel\\at.png'  # Cambia esto con la ruta de tu imagen

# Preprocesar la imagen
imagen_preprocesada = preparar_imagen(ruta_imagen)

# Hacer la predicción con el modelo
prediccion = modelo.predict(imagen_preprocesada)

# Obtener el índice de la clase con la mayor probabilidad
prediccion_clase = np.argmax(prediccion)

# Mostrar la imagen y la predicción
plt.imshow(imagen_preprocesada[0], cmap=plt.cm.binary)
plt.title(f"Predicción: {prediccion_clase}")
plt.show()
