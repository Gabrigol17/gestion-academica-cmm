from flask import Flask
from flask_mysqldb import MySQL
from config import Config
from Routes.__init__ import CargarRutas

app = Flask(__name__)

app.config.from_object(Config)
mysql = MySQL(app)

app.mysql = mysql

CargarRutas(app)

app.run(debug=True, port=3000, host="0.0.0.0")
