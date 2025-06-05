from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS aulas_programadas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curso_id INTEGER,
                data TEXT,
                hora_inicio TEXT,
                hora_fim TEXT,
                local_detalhado TEXT,
                observacao TEXT,
                status TEXT DEFAULT 'ativo',
                FOREIGN KEY (curso_id) REFERENCES cursos(id)
            )
        """)
        conn.commit()