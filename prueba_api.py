import os
from dotenv import load_dotenv
import google.generativeai as genai

print("Iniciando script...")

# Cargar variables del entorno
load_dotenv()

# Obtener clave API
api_key = os.getenv("API_KEY")
print(f"API Key detectada: {api_key[:10]}..." if api_key else "¡ERROR: No se encontró API_KEY en el .env!")

try:
    # Configurar Gemini
    genai.configure(api_key=api_key)

    # Cargar el modelo
    model = genai.GenerativeModel("gemini-1.5-flash")

    print("Enviando petición a Gemini...")
    response = model.generate_content("Hola, ¿puedes responder?")
    print("Respuesta recibida:")
    print(response.text)

except Exception as e:
    print(f"Ocurrió un error al conectar: {e}")