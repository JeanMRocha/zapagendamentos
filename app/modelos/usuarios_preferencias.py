from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS usuarios_preferencias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                id_categoria INTEGER NOT NULL,
                ativo BOOLEAN DEFAULT 1,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
                FOREIGN KEY (id_categoria) REFERENCES categorias_preferencia(id)
            )
        """)
        conn.commit()