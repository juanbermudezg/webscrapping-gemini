import google.generativeai as genai
from utils import log_message
import os
import PIL.Image

def main_function_imageRecognitionGemini(image_path):
    try:
        log_message('Started main_function_imageRecognitionGemini function in imageRecognitionGemini.py')
        model = gemini_usage()
        img = image_load(image_path)
        finalResponse = prompt_usage(img, image_path, model)
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

def prompt_usage(img, image_path, model):
    try:
        log_message(f'Started prompt_usage function in imageRecognitionGemini.py. Detailes: {image_path}')
        prompt_str = f"""
                Imagina que eres un analista de marketing en Colombia especializado en droguerías y establecimientos similares. Se te ha enviado un anuncio y debes extraer la siguiente información:
                - Categoría de productos ofrecidos (si es más de 1, agrúpalos bajo la categoría que corresponda).
                - Fechas de la oferta.
                - Porcentaje de descuento ofrecido (si hay más de un porcentaje, enuméralos).
                - Si no es un anuncio de descuento, responde con: "Null | NaN | Inicio: Null. Fin: Null".

                El formato de respuesta deberá ser el siguiente:
                [Categoría de productos] | [Porcentaje de descuento] | Inicio: [Fecha de inicio]. Fin: [Fecha de fin].

                Ejemplo:
                Medicamentos para la gripe | 20%, 30% | Inicio: 17 de octubre de 2024. Fin: 24 de octubre de 2024.
            """
        response = model.generate_content([prompt_str, img], stream=True)
        response.resolve()
        log_message(f'Finished prompt_usage function in imageRecognitionGemini.py. Detailes: {image_path}')
        return response.text
    except Exception as e:
        log_message(f"An error has occurred using prompt_usage function in imageRecognitionGemini.py. More details: {e}")
        return None

