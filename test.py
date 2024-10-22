import requests
from bs4 import BeautifulSoup

# URL de la página que deseas scrapear
url = "https://www.farmatodo.com.co/"

# Hacer la solicitud HTTP para obtener el contenido de la página
response = requests.get(url)
web_content = response.text

# Parsear el contenido HTML con BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup)
# Encontrar la sección específica
section = soup.find('section', class_='main-body-images-static-content')

# Si la sección existe, buscar todas las imágenes dentro de ella
if section:
    images = section.find_all('img')
    
    # Extraer los enlaces de las imágenes
    image_urls = [img['src'] for img in images if 'src' in img.attrs]
    
    for index, image_url in enumerate(image_urls, 1):
        print(f"Imagen {index}: {image_url}")
else:
    print("No se encontró la sección.")

