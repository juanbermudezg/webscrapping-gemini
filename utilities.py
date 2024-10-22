from utils import log_message, log_products
import pandas as pd
import numpy as np
import re
import os

def main_function_utilities(filePath, geminiResponse, imgPath):
    try:
        log_message('Started main_function_utilities function in utilities.py')
        df = load_file(filePath)
        product, discount, startDate, endDate = match_text(geminiResponse)
        add_product(df, product, discount, startDate, endDate, filePath)
        log_message('Finished main_function_utilities function in utilities.py')
        log_products(product, discount, startDate, endDate, imgPath)
    except Exception as e:
        log_message(f"An error has occurred using load_file function in utilities.py. More details: {e}")
        
def load_file(filePath):
    try:
        log_message('Started load_file function in utilities.py')
        if os.path.exists(filePath):
            df = pd.read_excel(filePath)
        else:
            df = pd.DataFrame(columns=['Producto', 'Descuento', 'Fecha Inicio', 'Fecha Fin'])
            df.to_excel(filePath, index=False)
        log_message('Finished load_file function in utilities.py')
        return df
    except Exception as e:
        log_message(f"An error has occurred using load_file function in utilities.py. More details: {e}")
        return None

def match_text(geminiResponse):
    try:
        log_message('Started match_text function in utilities.py')
        pattern = r'^(.*?)[|](.*?)[|] Inicio: (.*?)[.]+ Fin: (.*?)\.$'
        match = re.match(pattern, geminiResponse.strip())
        if match:
            product = match.group(1).strip()
            discount = match.group(2).strip()
            startDate = match.group(3).strip()
            endDate = match.group(4).strip()
        else:
            raise Exception('The string format is incorrect.')
        log_message('Finished match_text function in utilities.py')
        return product, discount, startDate, endDate
    except Exception as e:
        log_message(f"An error has occurred using match_text function in utilities.py. More details: {e}")
        return None

def add_product(df, product, discount, startDate, endDate, filePath):
    try:
        log_message('Started add_product function in utilities.py')
        newProduct = {
            'Producto': product if product != 'Null' else None,
            'Descuento': discount if discount != 'Null' else np.nan,
            'Fecha Inicio': startDate if startDate != 'Null' else None,
            'Fecha Fin': endDate if endDate != 'Null' else None
        }
        newProduct_df = pd.DataFrame([newProduct])
        df = pd.concat([df, newProduct_df], ignore_index=True)
        df.to_excel(filePath, index=False)
        log_message('Finished add_product function in utilities.py')
    except Exception as e:
        log_message(f"An error has occurred using add_product function in utilities.py. More details: {e}")