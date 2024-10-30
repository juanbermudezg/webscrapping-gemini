import requests

# URL de la página que deseas descargar
url = "https://www.larebajavirtual.com"

# Hacer la solicitud HTTP para obtener el contenido de la página
response = requests.get(url)
print(response.text)
# Guardar el HTML en un archivo local
with open("farmatodo.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("HTML guardado en 'main.html'")
