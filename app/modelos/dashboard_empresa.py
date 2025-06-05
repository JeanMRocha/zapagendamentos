from app.banco import conectar

def criar_tabela():
    with conectar() as conn:
        c = conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS dashboard_empresa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_prestador INTEGER,
                data_referencia DATE,
                total_visitas INTEGER DEFAULT 0,
                total_interacoes INTEGER DEFAULT 0,
                total_pedidos INTEGER DEFAULT 0,
                total_cancelamentos INTEGER DEFAULT 0,
                produto_mais_visto TEXT,
                horario_pico TEXT,
                origem_maior_acesso TEXT, -- ex: WhatsApp, link direto, busca
                FOREIGN KEY (id_prestador) REFERENCES usuarios(id)
            )
        """)

        conn.commit()