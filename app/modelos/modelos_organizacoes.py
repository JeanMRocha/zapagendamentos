from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Enum, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Organizacao(Base):
    __tablename__ = "organizacoes"
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    tipo = Column(Enum("associacao", "cooperativa", "ong", name="tipo_organizacao"))
    descricao = Column(Text)
    cnpj = Column(String(18), unique=True)
    ativa = Column(Boolean, default=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)

    membros = relationship("OrganizacaoMembro", back_populates="organizacao")
    relatorios = relationship("RelatorioFinanceiro", back_populates="organizacao")


class OrganizacaoMembro(Base):
    __tablename__ = "organizacoes_membros"
    id = Column(Integer, primary_key=True)
    organizacao_id = Column(Integer, ForeignKey("organizacoes.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    funcao = Column(String(50))  # Ex: presidente, conselheiro, associado
    direito_voto = Column(Boolean, default=False)
    acesso_total = Column(Boolean, default=False)  # Se pode ver todas as movimentações
    data_entrada = Column(DateTime, default=datetime.utcnow)
    data_saida = Column(DateTime)

    organizacao = relationship("Organizacao", back_populates="membros")
    usuario = relationship("Usuario", backref="organizacoes")


class RelatorioFinanceiro(Base):
    __tablename__ = "relatorios_financeiros"
    id = Column(Integer, primary_key=True)
    organizacao_id = Column(Integer, ForeignKey("organizacoes.id"))
    periodo_inicio = Column(DateTime)
    periodo_fim = Column(DateTime)
    descricao = Column(Text)
    total_receitas = Column(Integer)
    total_despesas = Column(Integer)
    publicado = Column(Boolean, default=False)

    organizacao = relationship("Organizacao", back_populates="relatorios")
