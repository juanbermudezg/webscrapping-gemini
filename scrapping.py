import requests
from bs4 import BeautifulSoup
import os
import urllib.request

# URL de la página web
url = 'https://www.larebajavirtual.com'

# Crear una carpeta para guardar las imágenes
if not os.path.exists('imagenes_banner'):
    os.makedirs('imagenes_banner')

# Obtener el contenido de la página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Usar select para buscar el img dentro de cualquier cantidad de divs con la clase que mencionaste
img_tag = soup.select_one('div.vtex-slider-layout-0-x-slide--slider-main img')

# Si se encuentra la imagen en el banner
if img_tag:
    # Obtener el título y el texto alternativo (alt)
    img_title = img_tag.get('title') or 'banner'
    img_alt = img_tag.get('alt')

    # Obtener la URL de la imagen
    img_url = img_tag.get('src')

    # Si la URL es relativa, convertirla en absoluta
    if img_url.startswith('/'):
        img_url = url + img_url

    # Definir el nombre del archivo usando el título o el alt
    img_name = f"{img_alt or img_title}.jpg"
    img_path = os.path.join('imagenes_banner', img_name)

    # Descargar la imagen
    urllib.request.urlretrieve(img_url, img_path)
    print(f"Imagen descargada: {img_name}")

else:
    print("No se encontró ninguna imagen en el banner visible.")
