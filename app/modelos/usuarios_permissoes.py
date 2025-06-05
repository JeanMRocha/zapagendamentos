from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS usuarios_permissoes (
                telefone TEXT PRIMARY KEY,
                tipo_usuario TEXT DEFAULT 'visitante', -- admin, moderador, empresa, visitante
                ativo BOOLEAN DEFAULT 1,
                FOREIGN KEY (telefone) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()