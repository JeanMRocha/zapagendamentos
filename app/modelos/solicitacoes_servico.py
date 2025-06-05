from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS solicitacoes_servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone TEXT,
                titulo TEXT,
                descricao TEXT,
                tipo_servico TEXT,
                endereco TEXT,
                distrito_id INTEGER,
                data_limite TEXT,
                valor_estimado TEXT,
                status TEXT DEFAULT 'aberta',
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()