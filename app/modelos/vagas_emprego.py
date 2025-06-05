from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS vagas_emprego (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                empresa_id INTEGER,
                titulo TEXT,
                descricao TEXT,
                tipo_contrato TEXT,  -- CLT, PJ, estágio, temporário, etc.
                modalidade TEXT,     -- remoto, híbrido, presencial
                salario TEXT,
                local_trabalho TEXT,
                requisitos TEXT,
                beneficios TEXT,
                carga_horaria TEXT,
                horario TEXT,
                publicado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ativo BOOLEAN DEFAULT 1,
                aprovado BOOLEAN DEFAULT 0,
                FOREIGN KEY (empresa_id) REFERENCES empresas(id)
            )
        """)
        conn.commit()