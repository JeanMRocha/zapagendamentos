from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS modulos_ativos (
                nome_modulo TEXT PRIMARY KEY,
                ativo BOOLEAN DEFAULT 0,
                visivel BOOLEAN DEFAULT 1,
                tipo_usuarios TEXT DEFAULT 'todos',
                observacao TEXT
            )
        """)
        conn.commit()

def modulo_ativo(nome):
    with conectar() as conn:
        c = conn.cursor()
        c.execute("SELECT ativo FROM modulos_ativos WHERE nome_modulo = ?", (nome,))
        resultado = c.fetchone()
        return resultado and resultado[0] == 1