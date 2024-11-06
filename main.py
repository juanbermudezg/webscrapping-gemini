from imageRecognitionGemini import main_function_imageRecognitionGemini
from imageRecognitionChatGPT import main_function_imageRecognitionChatGPT
from utilities import main_function_utilities
from utils import log_message
import os
import time


def main():
    log_message('Started main function in main.py')
    base_directory = 'src/img'
    file_path = 'output/finalCHATGPT.xlsx'
    responses = []
    for root, dirs, files in os.walk(base_directory):
        for filename in files:
            if filename.endswith('.png'):
                image_path = os.path.join(root, filename)
                time.sleep(3)
                response = main_function_imageRecognitionChatGPT(image_path)
                responses.append(response)
                main_function_utilities(file_path, response, image_path)       
    for response in responses:
        print(response)
    for response in responses:
        print(response)
    log_message('Finished main function in main.py')

"""
def main():
    log_message('Started main function in main.py')
    base_directory  = 'src/img'
    file_path = 'output/finalGemini.xlsx'
    responses = []
    for root, dirs, files in os.walk(base_directory):
        for filename in files:
            if filename.endswith('.png'):
                image_path = os.path.join(root, filename)
                time.sleep(3)
                response = main_function_imageRecognitionGemini(image_path)
                responses.append(response)
                main_function_utilities(file_path, response, image_path)       
    for response in responses:
        print(response)
    log_message('Finished main function in main.py')
"""
if __name__ == "__main__":
    main()