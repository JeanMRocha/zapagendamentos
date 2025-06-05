from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS doacoes_avulsas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone TEXT,
                titulo TEXT,
                descricao TEXT,
                tipo TEXT, -- animal, móvel, roupa, alimento, etc.
                condicao TEXT, -- novo, usado, etc.
                foto TEXT,
                local_retirada TEXT,
                status TEXT DEFAULT 'disponivel', -- disponivel, entregue, cancelado
                data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()