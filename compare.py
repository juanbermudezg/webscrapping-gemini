from PIL import Image
import numpy as np

def comparar_imagenes(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    img1_array = np.array(img1)
    img2_array = np.array(img2)
    if img1_array.shape != img2_array.shape:
        return False
    comparison = np.array_equal(img1_array, img2_array)
    return comparison

imagen1 = 'img/prueba2.jpg'
imagen2 = 'img/unnamed.webp'

if comparar_imagenes(imagen1, imagen2):
    print("Las imágenes son exactamente iguales")
else:
    print("Las imágenes son diferentes")
