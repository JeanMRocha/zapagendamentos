import sqlite3
from modelos import (
    usuarios, empresas, servicos, eventos,
    empresa_detalhes, empresa_socios, empresa_funcionarios,
    cursos, aulas_programadas, fichas_inscricao, inscritos, respostas_inscritos, avisos_evento,
    pontos_turisticos, guias_local, ponto_guia_relacao,
    roteiros_comerciais, roteiros_ponto_relacao,
    vagas_emprego, perguntas_vaga, candidatos_vaga, respostas_candidato,
    solicitacoes_servico, respostas_solicitacao
)

def conectar():
    return sqlite3.connect("zap.db")

def criar_tabelas():
    usuarios.criar_tabela()
    empresas.criar_tabela()
    servicos.criar_tabela()
    eventos.criar_tabela()
    empresa_detalhes.criar_tabela()
    empresa_socios.criar_tabela()
    empresa_funcionarios.criar_tabela()
    cursos.criar_tabela()
    aulas_programadas.criar_tabela()
    fichas_inscricao.criar_tabela()
    inscritos.criar_tabela()
    respostas_inscritos.criar_tabela()
    avisos_evento.criar_tabela()
    pontos_turisticos.criar_tabela()
    guias_local.criar_tabela()
    ponto_guia_relacao.criar_tabela()
    roteiros_comerciais.criar_tabela()
    roteiros_ponto_relacao.criar_tabela()
    vagas_emprego.criar_tabela()
    perguntas_vaga.criar_tabela()
    candidatos_vaga.criar_tabela()
    respostas_candidato.criar_tabela()
    solicitacoes_servico.criar_tabela()
    respostas_solicitacao.criar_tabela()

if __name__ == "__main__":
    criar_tabelas()
    print("Tabelas criadas com sucesso.")