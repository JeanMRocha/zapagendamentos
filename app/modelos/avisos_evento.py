from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS avisos_evento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curso_id INTEGER,
                texto TEXT,
                data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (curso_id) REFERENCES cursos(id)
            )
        """)
        conn.commit()