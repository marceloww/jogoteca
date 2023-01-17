from urllib.parse import quote
import os

SECRET_KEY = 'alura'

senha = quote('Telecom@30')

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = senha,
        servidor = 'localhost',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'