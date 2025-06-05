from app.banco import conectar
from app.modelos.atualizar_interesses import atualizar_interesses_automaticamente
from app.modelos.respostas_automaticas import criar_tabela as criar_tabela_respostas
from app.modelos.conversas_recentes import criar_tabela as criar_tabela_conversas
from app.modelos.sugestoes_interesse import criar_tabela as criar_tabela_sugestoes
from app.modelos.interesses_usuario import criar_tabela as criar_tabela_interesses
from app.modelos.preferencias_usuario import criar_tabela as criar_tabela_preferencias

# Cria todas as tabelas ao iniciar o sistema
def iniciar_banco():
    criar_tabela_respostas()
    criar_tabela_conversas()
    criar_tabela_sugestoes()
    criar_tabela_interesses()
    criar_tabela_preferencias()

def buscar_resposta_automatica(mensagem, id_usuario):
    texto = mensagem.lower()
    resposta = None

    with conectar() as conn:
        c = conn.cursor()

        # Primeiro: tenta resposta automática por palavra-chave
        c.execute("""
            SELECT resposta_automatica FROM respostas_automaticas
            WHERE ativo = 1 AND instr(?, palavras_chave) > 0
            ORDER BY id DESC LIMIT 1
        """, (texto,))
        resultado = c.fetchone()
        if resultado:
            resposta = resultado[0]

        # Se encontrou resposta, registra a conversa
        if resposta:
            c.execute("""
                INSERT INTO conversas_recentes (id_usuario, mensagem, resposta, origem)
                VALUES (?, ?, ?, ?)
            """, (id_usuario, mensagem, resposta, 'cliente_logado'))
            conn.commit()
            return resposta

        # Se não encontrou, procura sugestão por interesse
        c.execute("""
            SELECT resposta_sugerida FROM sugestoes_interesse
            WHERE ativo = 1 AND instr(?, palavras_chave) > 0
            ORDER BY id DESC LIMIT 1
        """, (texto,))
        sugestao = c.fetchone()
        if sugestao:
            resposta = sugestao[0]
        else:
            resposta = "Ainda não tenho uma resposta exata, mas posso te ajudar com: saúde, turismo, eventos ou serviços. Sobre o que você quer saber?"

        # Registra a conversa mesmo sem resposta automática
        c.execute("""
            INSERT INTO conversas_recentes (id_usuario, mensagem, resposta, origem)
            VALUES (?, ?, ?, ?)
        """, (id_usuario, mensagem, resposta, 'cliente_logado'))
        conn.commit()

    return resposta

def processar_mensagem(id_usuario, mensagem):
    # Atualiza interesses com base no texto
    atualizar_interesses_automaticamente(id_usuario, mensagem)

    # Busca resposta automatizada ou sugestão
    return buscar_resposta_automatica(mensagem, id_usuario)

# Exemplo de teste direto
if __name__ == "__main__":
    iniciar_banco()
    usuario_teste = 1
    mensagem_teste = "Você sabe onde tem dentista aqui?"
    resposta = processar_mensagem(usuario_teste, mensagem_teste)
    print("Resposta:", resposta)