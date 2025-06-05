from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT,
                data_inicio TEXT,
                data_fim TEXT,
                horario TEXT,
                local TEXT,
                capacidade INTEGER,
                requisitos TEXT,
                precisa_levar TEXT,
                gratuito BOOLEAN DEFAULT 1,
                certificado_url TEXT,
                aprovado BOOLEAN DEFAULT 0,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()