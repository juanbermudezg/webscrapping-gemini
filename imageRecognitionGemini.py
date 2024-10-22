import google.generativeai as genai
from utils import log_message
import os
import PIL.Image

model = None

def main_function_imageRecognitionGemini(image_path):
    try:
        log_message('Started main_function_imageRecognitionGemini function in imageRecognitionGemini.py')
        gemini_usage()
        img = image_load(image_path)
        finalResponse = prompt_usage(img, image_path)
        if finalResponse is None or not finalResponse:
            raise Exception('finalResponse is None, please check the logger.')
        log_message('Finished main_function_imageRecognitionGemini function in imageRecognitionGemini.py')
        return finalResponse
    except Exception as e:
        log_message(f"An error has occurred using main_function_imageRecognitionGemini function in imageRecognitionGemini.py. More details: {e}")
        return f"Error: {e}"

def gemini_usage():
    try:
        log_message('Started gemini_usage function in imageRecognitionGemini.py')
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        global model
        if model is not None:
            return model
        genai.configure(api_key = GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        log_message('Finished gemini_usage function in imageRecognitionGemini.py')
        return model
    except Exception as e:
        log_message(f"An error has occurred using gemini_usage function in imageRecognitionGemini.py. More details: {e}")
        return None

def image_load(imagePath):
    try:
        log_message('Started image_load function in imageRecognitionGemini.py')
        img = PIL.Image.open(imagePath)
        log_message('Finished image_load function in imageRecognitionGemini.py')
        return img
    except Exception as e:
        log_message(f"An error has occurred using image_load function in imageRecognitionGemini.py. More details: {e}")
        return None

def prompt_usage(img, image_path):
    try:
        log_message(f'Started prompt_usage function in imageRecognitionGemini.py. Detailes: {image_path}')
        prompt_str = f"""
                Imagina que eres un analista de marketing en colombia en droguerías y establecimientos parecidos en Colombia. Se te ha hecho envio de un anuncio en el cual deberás encontrar los siguientes parámetros:
                - Producto ofrecido (si es más de 1, la categoría).
                - Fechas de la oferta.
                - Porcentaje de descuento ofrecido.
                La respuesta deberá seguir el siguiente formato:
                Colgate | 20% | Inicio: 24 de mayo de 2024. Fin: 29 de mayo de 2024.
                Si la imagen no expone explicitamente un anuncio de oferta de descuento o falta información, responde de la siguiente forma:
                Null | NaN | Inicio: Null. Fin: Null.
            """
        response = model.generate_content([prompt_str, img], stream=True)
        response.resolve()
        log_message(f'Finished prompt_usage function in imageRecognitionGemini.py. Detailes: {image_path}')
        return response.text
    except Exception as e:
        log_message(f"An error has occurred using prompt_usage function in imageRecognitionGemini.py. More details: {e}")
        return None

