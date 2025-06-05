from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS horarios_funcionamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_prestador INTEGER,
                dia_semana TEXT, -- segunda, terça, etc.
                horario_abre TEXT,
                horario_fecha TEXT,
                ativo BOOLEAN DEFAULT 1,
                observacao TEXT,
                FOREIGN KEY (id_prestador) REFERENCES usuarios(id)
            )
        """)

        conn.commit()