from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS entregas_confirmadas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_doacao INTEGER,
                tipo_origem TEXT, -- 'campanha' ou 'avulsa'
                telefone_doador TEXT,
                telefone_receptor TEXT,
                confirmado BOOLEAN DEFAULT 0,
                data_entrega TEXT,
                foto_comprovante TEXT,
                observacao TEXT,
                FOREIGN KEY (telefone_doador) REFERENCES usuarios(telefone),
                FOREIGN KEY (telefone_receptor) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()