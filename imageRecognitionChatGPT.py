from openai import OpenAI
from utils import log_message
import os
import base64
import psycopg2
from datetime import datetime

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
        log_message('Started chatgpt_usage function in imageRecognitionChatGPT.py')
        CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')
        client = OpenAI(api_key=CHATGPT_API_KEY)
        log_message('Finished chatgpt_usage function in imageRecognitionChatGPT.py')
        return client
    except Exception as e:
        log_message(f"An error has occurred using chatgpt_usage function in imageRecognitionChatGPT.py. More details: {e}")
        return None

def image_load(imagePath):
    try:
        log_message('Started image_load function in imageRecognitionChatGPT.py')
        with open(imagePath, "rb") as image_file:
            log_message('Finished image_load function in imageRecognitionChatGPT.py')
            return base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        log_message(f"An error has occurred using image_load function in imageRecognitionChatGPT.py. More details: {e}")
        return None



def log_prompt_usage(prompt, image_path, tokens_used, cost_usd):
    conn = psycopg2.connect(
        host="netapp.postgres.database.azure.com",
        database="mom_db",
        user="netadmin",
        password="Colombia2023*"
    )
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO prompt_usage_log (prompt, image_path, tokens_used, cost_usd, created_at)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (prompt, image_path, tokens_used, cost_usd, datetime.now())
    )
    conn.commit()
    cur.close()
    conn.close()

def prompt_usage(base64Img, image_path, client):
    try:
        log_message(f'Started prompt_usage function in imageRecognitionChatGPT.py. Details: {image_path}')
        MODEL = "gpt-4o"
        
        # Define the prompt string
        prompt_str = """
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

        # Send the prompt to the client
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

        # Get the final response content
        finalResponse = response.choices[0].message.content

        # Estimate tokens used and calculate cost in USD
        tokens_used = response.usage.total_tokens if hasattr(response, 'usage') else 0
        cost_per_1k_tokens = 0.06  # Example rate in USD per 1000 tokens for GPT-4-turbo
        cost_usd = (tokens_used / 1000) * cost_per_1k_tokens if tokens_used else 0

        # Log the prompt usage in the database
        log_prompt_usage(prompt_str, image_path, tokens_used, cost_usd)
        
        log_message(f'Finished prompt_usage function in imageRecognitionChatGPT.py. Details: {image_path}')
        return finalResponse

    except Exception as e:
        log_message(f"An error has occurred using prompt_usage function in imageRecognitionChatGPT.py. More details: {e}")
        return None


    except Exception as e:
        log_message(f"An error has occurred using prompt_usage function in imageRecognitionChatGPT.py. More details: {e}")
        return None
