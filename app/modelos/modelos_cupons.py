from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Enum, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from app.database import Base

class Cupom(Base):
    __tablename__ = "cupons"
    id = Column(Integer, primary_key=True)
    codigo = Column(String(20), unique=True, nullable=False)
    tipo = Column(Enum("indicacao", "campanha", "desconto", name="tipo_cupom"), nullable=False)
    criado_por_usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    valor_creditos = Column(Integer, default=0)
    validade = Column(DateTime)
    usos_maximos = Column(Integer, default=1)
    usos_atuais = Column(Integer, default=0)
    descricao = Column(String(255))

    criado_por = relationship("Usuario", backref="cupons_criados")
    usos = relationship("UsoCupom", back_populates="cupom")


class UsoCupom(Base):
    __tablename__ = "usos_cupom"
    id = Column(Integer, primary_key=True)
    cupom_id = Column(Integer, ForeignKey("cupons.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    data_uso = Column(DateTime, default=datetime.utcnow)

    cupom = relationship("Cupom", back_populates="usos")
    usuario = relationship("Usuario", backref="cupons_usados")


class CampanhaIndicacao(Base):
    __tablename__ = "campanhas_indicacao"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text)
    ativo = Column(Boolean, default=True)
    data_inicio = Column(DateTime, default=datetime.utcnow)
    data_fim = Column(DateTime, nullable=True)
    bonus_indicador = Column(Integer, default=0)
    bonus_indicado = Column(Integer, default=0)
    uso_limite_por_usuario = Column(Integer, default=1)


class BrindeIndicacao(Base):
    __tablename__ = "brindes_indicacao"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    campanha_id = Column(Integer, ForeignKey("campanhas_indicacao.id"))
    tipo = Column(String(50))  # Ex: "primeira_compra", "recorrencia"
    creditos = Column(Integer, default=0)
    entregue = Column(Boolean, default=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", backref="brindes_recebidos")
    campanha = relationship("CampanhaIndicacao", backref="brindes")
