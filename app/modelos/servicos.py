
from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS servicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                empresa_id INTEGER,
                nome TEXT,
                descricao TEXT,
                preco REAL,
                duracao_min INTEGER,
                categoria TEXT,
                tipo TEXT,
                bairro_id INTEGER,
                distrito_id INTEGER,
                endereco_detalhado TEXT,
                disponivel_hoje BOOLEAN DEFAULT 0,
                aprovado BOOLEAN DEFAULT 0,
                destaque BOOLEAN DEFAULT 0,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (empresa_id) REFERENCES empresas(id)
            )
        """)
        conn.commit()
