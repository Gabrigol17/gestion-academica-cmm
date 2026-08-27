import os
from dotenv import load_dotenv

# Encuentra y carga el archivo .env
load_dotenv()

class Config:
    """Configuración base extraída del archivo .env"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
