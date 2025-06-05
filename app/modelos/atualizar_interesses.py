from app.banco import conectar
from datetime import datetime

def atualizar_interesses_automaticamente(id_usuario, mensagem):
    # Define categorias e palavras-chave associadas
    categorias = {
        'saude': ['hospital', 'dentista', 'clínica', 'remédio', 'posto de saúde'],
        'turismo': ['cachoeira', 'trilha', 'pico', 'hotel', 'pousada'],
        'eventos': ['festa', 'evento', 'show', 'feira', 'reunião'],
        'empregos': ['vaga', 'emprego', 'trabalhar', 'currículo', 'contratação'],
        'pets': ['cachorro', 'gato', 'adoção', 'pet shop', 'desaparecido'],
        'doacoes': ['doar', 'doação', 'campanha', 'ajuda'],
        'esportes': ['jiu-jitsu', 'futebol', 'capoeira', 'esporte', 'academia'],
        'compras': ['comprar', 'produto', 'classificado', 'venda'],
        'educacao': ['curso', 'escola', 'oficina', 'professor', 'aula'],
        'servicos': ['conserto', 'manutenção', 'serviço', 'reparo', 'profissional'],
        'alertas_publicos': ['enchente', 'obras', 'interdição', 'comunicado'],
    }

    # Normaliza e analisa a mensagem
    texto = mensagem.lower()

    with conectar() as conn:
        c = conn.cursor()

        for categoria, palavras in categorias.items():
            if any(palavra in texto for palavra in palavras):
                campo = f"interesse_{categoria}"
                c.execute(f"""
                    INSERT INTO preferencias_usuario (id_usuario, {campo})
                    VALUES (?, 1)
                    ON CONFLICT(id_usuario) DO UPDATE SET {campo} = 1, atualizado_em = ?
                """, (id_usuario, datetime.now()))

        conn.commit()