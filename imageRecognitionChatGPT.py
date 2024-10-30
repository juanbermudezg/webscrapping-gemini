from openai import OpenAI
from utils import log_message
import os
import PIL.Image
import base64

def main_function_imageRecognitionChatGPT(image_path):
    try:
        log_message('Started main_function_imageRecognitionChatGPT function in imageRecognitionChatGPT.py')
        client = chatgpt_usage()
        base64Img = image_load(image_path)
        finalResponse = prompt_usage(base64Img, image_path, client)
        if finalResponse is None or not finalResponse:
            raise Exception('finalResponse is None, please check the logger.')
        log_message('Finished main_function_imageRecognitionChatGPT function in imageRecognitionChatGPT.py')
        return finalResponse
    except Exception as e:
        log_message(f"An error has occurred using main_function_imageRecognitionChatGPT function in imageRecognitionChatGPT.py. More details: {e}")
        return f"Error: {e}"

def chatgpt_usage():
    try:
        log_message('Started gemini_usage function in imageRecognitionGemini.py')
        CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')
        client = OpenAI(api_key=CHATGPT_API_KEY)
        log_message('Finished gemini_usage function in imageRecognitionGemini.py')
        return client
    except Exception as e:
        log_message(f"An error has occurred using gemini_usage function in imageRecognitionGemini.py. More details: {e}")
        return None

def image_load(imagePath):
    try:
        log_message('Started image_load function in imageRecognitionGemini.py')
        with open(imagePath, "rb") as image_file:
            log_message('Finished image_load function in imageRecognitionGemini.py')
            return base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        log_message(f"An error has occurred using image_load function in imageRecognitionGemini.py. More details: {e}")
        return None

def prompt_usage(base64Img, image_path, client):
    try:
        log_message(f'Started prompt_usage function in imageRecognitionGemini.py. Detailes: {image_path}')
        MODEL="gpt-4o"
        prompt_str = f"""
                Imagina que eres un analista de marketing en Colombia especializado en droguerías y establecimientos similares. Se te ha enviado un anuncio y debes extraer la siguiente información:
                - Categoría/marca de productos ofrecidos (si es más de 1, agrúpalos bajo la categoría que corresponda).
                - Fechas de la oferta.
                - Porcentaje de descuento ofrecido (si hay más de un porcentaje, escoge el menor).
                - Si no es un anuncio de descuento, responde con: "Null | NaN | Inicio: Null. Fin: Null".

                El formato de respuesta deberá ser el siguiente:
                [Categoría de productos] | [Porcentaje de descuento] | Inicio: [Fecha de inicio]. Fin: [Fecha de fin].

                Ejemplo:
                Medicamentos para la gripe | 20% | Inicio: 17/10/2024. Fin: 24/10/2024.
            """
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": prompt_str},
                {"role": "user", "content": [
                    {"type": "text", "text": "Dime qué ves en la imagen, basandote en las reglas anteriormente descritas"},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/png;base64,{base64Img}"}
                    }
                ]}
            ],
            temperature=0.0,
        )
        finalResponse = response.choices[0].message.content
        log_message(f'Finished prompt_usage function in imageRecognitionGemini.py. Detailes: {image_path}')
        return finalResponse
    except Exception as e:
        log_message(f"An error has occurred using prompt_usage function in imageRecognitionGemini.py. More details: {e}")
        return None

