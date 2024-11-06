import psycopg2

# Define el precio por 1000 tokens para el modelo (ajustar según el modelo específico)
PRICE_PER_1000_TOKENS = 0.02  # Precio de ejemplo, actualiza según los valores de OpenAI

def calculate_token_cost(tokens_used):
    # Calcula el costo en USD basado en el número de tokens utilizados
    cost = (tokens_used * PRICE_PER_1000_TOKENS) / 1000
    return round(cost, 4)  # Redondea a 4 decimales

def update_prompt_usage_cost(id, tokens_used):
    cost_usd = calculate_token_cost(tokens_used)
    
    # Conectar a la base de datos
    conn = psycopg2.connect(
        host="netapp.postgres.database.azure.com",
        database="mom_db",
        user="netadmin",
        password="Colombia2023*"
    )
    cur = conn.cursor()
    
    # Actualizar el registro con el costo calculado
    cur.execute(
        """
        UPDATE prompt_usage_log
        SET cost_usd = %s
        WHERE id = %s
        """,
        (cost_usd, id)
    )
    
    conn.commit()
    cur.close()
    conn.close()

# Ejemplo de uso
# Suponiendo que `tokens_used` y `id` del registro están disponibles
tokens_used = 500  # Reemplaza con el valor real de tokens usados
registro_id = 1  # Reemplaza con el ID del registro correspondiente
update_prompt_usage_cost(registro_id, tokens_used)
