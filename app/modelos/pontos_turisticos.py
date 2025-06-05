from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS pontos_turisticos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT,
                tipo TEXT,
                bairro_id INTEGER,
                distrito_id INTEGER,
                endereco TEXT,
                coordenadas TEXT,
                gratuito BOOLEAN DEFAULT 1,
                publico BOOLEAN DEFAULT 1,
                status TEXT,
                capacidade INTEGER,
                contato TEXT,
                links_midias TEXT,
                agencia_responsavel_id INTEGER,
                aprovado BOOLEAN DEFAULT 0,
                destaque BOOLEAN DEFAULT 0,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()