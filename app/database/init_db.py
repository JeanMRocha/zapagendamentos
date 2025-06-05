# Arquivo: app/database/init_db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

# Substitua pela URL correta do seu banco
DATABASE_URL = "sqlite:///zapagendamentos.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Importa todos os modelos para garantir que sejam criados
from app.modelos import (
    modelos_gamificacao,
    modelos_cupons,
    modelos_organizacoes,
    usuarios_planos_extras
)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("✅ Banco de dados inicializado com sucesso.")
