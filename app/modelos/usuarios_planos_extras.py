# Modificações complementares a serem aplicadas em modelos existentes
# Arquivo: app/modelos/usuarios.py e app/modelos/planos.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

# Em usuarios.py — Adições na classe Usuario:

agendamentos_mes = Column(Integer, default=0)
agendamentos_total = Column(Integer, default=0)
categoria_atual = Column(String(50))
ranking_posicao = Column(Integer)
telefone_confirmado = Column(Boolean, default=False)
email_confirmado = Column(Boolean, default=False)
chave_pix = Column(String(120))
badge = Column(String(100))

# Relacionamentos complementares
bonus = relationship("Bonus", back_populates="usuario")
conquistas = relationship("ConquistaUsuario")

# Em planos.py — Adições na classe Plano:

limite_creditos_mensal = Column(Integer)
val_recompensa = Column(Integer)
val_validade_credito = Column(Integer)  # dias
bonus_primeira_compra = Column(Integer)
bonus_recorrencia = Column(Integer)
limite_acumulo_creditos = Column(Integer)

# Sugestão: centralizar políticas por tipo de plano com uma tabela auxiliar (ex: PoliticasPlano)
# ou definir isso diretamente no CRUD do painel administrativo
