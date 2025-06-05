from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS murais_avisos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                mensagem TEXT,
                autor TEXT,
                tipo TEXT,
                publico_alvo TEXT,
                cidade TEXT DEFAULT 'Santa Maria Madalena',
                distrito TEXT,
                bairro TEXT,
                segmento_alvo TEXT, -- categorias_preferencia.id (CSV ou JSON)
                grupo_alvo TEXT, -- produtores, mães, idosos, comerciantes etc.
                restrito_a_bairro TEXT,
                restrito_a_distrito TEXT,
                data_inicio TEXT,
                data_fim TEXT,
                urgente BOOLEAN DEFAULT 0,
                aprovado BOOLEAN DEFAULT 0,
                destaque BOOLEAN DEFAULT 0,
                visivel BOOLEAN DEFAULT 1,
                link_externo TEXT,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()