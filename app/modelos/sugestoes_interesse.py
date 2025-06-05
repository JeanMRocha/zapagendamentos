from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS sugestoes_interesse (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_interesse TEXT, -- saúde, turismo, eventos, pets, etc.
                palavras_chave TEXT, -- separadas por vírgula
                resposta_sugerida TEXT,
                link_acao TEXT, -- slug, url interna, comando ou ID
                ativo BOOLEAN DEFAULT 1
            )
        """)

        conn.commit()