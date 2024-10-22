from datetime import datetime
from config import log_file, log_products_file

def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f"{timestamp} - {message}\n")
        
def log_products(product, discount, startDate, endDate, imgPath):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_products_file, 'a') as f:
        f.write(f"{imgPath}:\t{product} - {discount} - {startDate} - {endDate} --- {timestamp}\n")