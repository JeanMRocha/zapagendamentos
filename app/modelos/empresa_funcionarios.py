
from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS empresa_funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                empresa_id INTEGER,
                usuario_tel TEXT,
                funcao TEXT,
                comissao REAL,
                ativo BOOLEAN DEFAULT 1,
                FOREIGN KEY (empresa_id) REFERENCES empresas(id),
                FOREIGN KEY (usuario_tel) REFERENCES usuarios(telefone)
            )
        """)
        conn.commit()
