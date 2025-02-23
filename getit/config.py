import secrets

# Configurações da aplicação
class Config:
    # Gera uma chave secreta forte de 32 bytes (256 bits)
    SECRET_KEY = secrets.token_hex(32)
    
    # Configurações do SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///notes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False