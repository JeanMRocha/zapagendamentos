from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Enum, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class CategoriaUso(Base):
    __tablename__ = "categorias_uso"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True, nullable=False)  # Ex: Iniciante, Engajado, Profissional
    min_agendamentos = Column(Integer, nullable=False)
    max_agendamentos = Column(Integer, nullable=True)  # Pode ser NULL para "sem limite superior"
    recompensa_creditos = Column(Integer, default=0)
    validade_dias = Column(Integer, default=15)
    selo = Column(String(100))  # caminho do badge ou nome de selo simbólico
    destaque_publico = Column(Boolean, default=False)


class Bonus(Base):
    __tablename__ = "bonus"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo = Column(String(50))  # Ex: "recorrencia", "categoria", "ranking", "meta"
    valor_creditos = Column(Integer)
    validade = Column(DateTime)
    descricao = Column(String(255))
    criado_em = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="bonus")


class Conquista(Base):
    __tablename__ = "conquistas"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    agendamentos_necessarios = Column(Integer, nullable=False)
    beneficio = Column(String(100))  # ex: 10 créditos, plano PRO grátis etc.
    icone = Column(String(100))
    descricao = Column(Text)


class ConquistaUsuario(Base):
    __tablename__ = "conquistas_usuarios"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    conquista_id = Column(Integer, ForeignKey("conquistas.id"))
    data_conquista = Column(DateTime, default=datetime.utcnow)


class RankingMensal(Base):
    __tablename__ = "rankings_mensais"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    cidade = Column(String(100))
    mes = Column(String(7))  # formato AAAA-MM
    posicao = Column(Integer)
    destaque = Column(Boolean, default=False)

# Relacionamentos complementares em Usuario (a serem adicionados):
# bonus = relationship("Bonus", back_populates="usuario")
# conquistas = relationship("ConquistaUsuario")
# agendamentos_mes, agendamentos_total, categoria_atual, ranking_posicao = novos campos em Usuario
