
from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS empresa_detalhes (
                empresa_id INTEGER PRIMARY KEY,
                natureza_juridica TEXT,
                porte TEXT,
                cnae_principal TEXT,
                data_abertura DATE,
                responsavel_legal TEXT,
                FOREIGN KEY (empresa_id) REFERENCES empresas(id)
            )
        """)
        conn.commit()
