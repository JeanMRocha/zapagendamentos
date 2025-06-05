
from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS eventos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT,
                data_inicio TEXT,
                data_fim TEXT,
                local TEXT,
                bairro_id INTEGER,
                distrito_id INTEGER,
                gratuito BOOLEAN DEFAULT 1,
                faixa_etaria TEXT,
                tipo TEXT,
                categoria TEXT,
                contato TEXT,
                aprovado BOOLEAN DEFAULT 0,
                destaque BOOLEAN DEFAULT 0,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
