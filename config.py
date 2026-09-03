import os
from dotenv import load_dotenv

# Encuentra y carga el archivo .env
load_dotenv()

class Config:
    # Configuración de la base de datos
    MYSQL_HOST      = os.getenv('MYSQL_HOST')
    MYSQL_USER      = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD  = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB        = os.getenv('MYSQL_DB')
    MYSQL_PORT      = int(os.getenv('MYSQL_PORT', 3306))
    MYSQL_SSL =     {
        "ca": "/etc/secrets/aiven-ca.pem",
    } 

# Esta clase sirve para cargar la configuración de la base 
# de datos desde un archivo .env y almacenarla en variables de clase.
