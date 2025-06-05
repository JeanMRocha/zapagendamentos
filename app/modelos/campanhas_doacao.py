from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS campanhas_doacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone TEXT,
                nome TEXT,
                descricao TEXT,
                tipos_aceitos TEXT,
                meta TEXT,
                local_entrega TEXT,
                data_inicio TEXT,
                data_fim TEXT,
                status TEXT DEFAULT 'ativa',
                patrocinada BOOLEAN DEFAULT 0,
                aprovado BOOLEAN DEFAULT 0,
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()