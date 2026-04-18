# ------- This script was made here to reinforce thr security of the application so far ----
# Things like , methods like hashing password , jwt security and check password
import os

import jwt
from passlib.context import  CryptContext
from dotenv import load_dotenv

load_dotenv()

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# ------ So here are the methods for increasing the security , hash and check password
def hashing_password(password:str):
    return pwd_context.hash(password)

def check_password(hashed_password:str, password:str):
    return pwd_context.verify(password, hashed_password)

# ------- Jwt tokenization ------

import jwt
import datetime
from passlib.context import CryptContext

# Configuração do contexto de senha
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Configurações para o JWT (Devem ser tratadas como sensíveis)
SECRET_KEY = "sua_chave_secreta_aqui"
ALGORITHM = "HS256"


# ------ Métodos de Password ------

def hashing_password(password: str):
    return pwd_context.hash(password)


def check_password(hashed_password: str, password: str):
    # O verify recebe (senha_plana, senha_hash)
    return pwd_context.verify(password, hashed_password)


# ------- Jwt tokenization ------

def encode_token(data: dict):
    """
    Recebe um dicionário de dados (payload) e retorna o JWT assinado.
    """
    to_encode = data.copy()

    # Define a expiração (ex: 30 minutos a partir de agora)
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

    to_encode.update({"exp": expire})

    # Gera o token assinado
    encoded_jwt = jwt.encode(to_encode, os.getenv('secret_key'), algorithm=ALGORITHM)
    return encoded_jwt

