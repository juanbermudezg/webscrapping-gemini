from imageRecognitionGemini import main_function_imageRecognitionGemini
from utilities import main_function_utilities
from utils import log_message
import os
import time

"""
def main():
    log_message('Started main function in main.py')
    image_path = 'img/1.webp'
    file_path = 'src/final.xlsx'
    response = main_function_imageRecognitionGemini(image_path)
    print(response)
    main_function_utilities(file_path, response)
    log_message('Finished main function in main.py')
"""

def main():
    log_message('Started main function in main.py')
    directory = 'src/img'
    file_path = 'src/final.xlsx'
    responses = []
    for filename in os.listdir(directory):
        time.sleep(5)
        if filename.endswith(('.jpg', '.jpeg', '.png', '.webp')):
            image_path = os.path.join(directory, filename)
            response = main_function_imageRecognitionGemini(image_path)
            responses.append(response)
            main_function_utilities(file_path, response, image_path)
    for response in responses:
        print(response)
    log_message('Finished main function in main.py')

if __name__ == "__main__":
    main()