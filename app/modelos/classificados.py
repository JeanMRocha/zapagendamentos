from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS classificados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone TEXT,
                titulo TEXT,
                descricao TEXT,
                categoria TEXT,
                preco TEXT,
                tipo_negocio TEXT, -- venda, troca, doacao
                fotos TEXT,
                bairro_id INTEGER,
                distrito_id INTEGER,
                destaque_ate TEXT, -- até quando fica em destaque
                tipo_destaque TEXT, -- home, categoria, geral
                data_finalizacao TEXT, -- se foi vendido ou retirado
                status TEXT DEFAULT 'ativo',
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()