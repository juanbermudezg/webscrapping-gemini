import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar Selenium para abrir el navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Si no quieres que se abra el navegador de forma visual
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL del sitio web
url = 'https://www.farmatodo.com.co'

# Navegar a la página con Selenium
driver.get(url)

# Obtener el contenido de la página
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Buscar el carrusel de imágenes (asumiendo que el div tiene la clase "app-banner")
carousel = soup.find('div', class_='app-banner')

# Crear una carpeta para guardar las imágenes
if not os.path.exists('imagenes_carrusel'):
    os.makedirs('imagenes_carrusel')

# Encontrar todas las imágenes dentro del carrusel
if carousel:
    images = carousel.find_all('img')  # Encontrar todas las etiquetas img
    for index, img in enumerate(images):
        img_url = img.get('src')  # Obtener la URL de la imagen
        if img_url:
            # Descargar la imagen
            img_data = requests.get(img_url).content
            # Guardar la imagen en la carpeta
            with open(f'imagenes_carrusel/imagen_{index + 1}.jpg', 'wb') as img_file:
                img_file.write(img_data)
            print(f'Imagen {index + 1} descargada: {img_url}')
else:
    print('No se encontró el carrusel con la clase "app-banner".')

# Cerrar el navegador
driver.quit()
