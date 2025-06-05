from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS achados_perdidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone TEXT,
                tipo TEXT, -- 'achado' ou 'perdido'
                titulo TEXT,
                descricao TEXT,
                local TEXT,
                local_entrega TEXT, -- onde o item foi entregue ou pode ser retirado
                foto TEXT,
                status TEXT DEFAULT 'ativo',
                aprovado BOOLEAN DEFAULT 0,
                obs_privada TEXT,
                tentativas_diarias INT DEFAULT 1,
                data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()