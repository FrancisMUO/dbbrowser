from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from src.modelo.declarative_base import Base

class NRC(Base):
    __tablename__ = 'nrcs'

    id = Column(Integer, primary_key=True)
    codigo = Column(String, nullable=False)  # Código del NRC (ej: NRC1001)
    nombre_curso = Column(String, nullable=False)  # Nombre del curso
    detalles = relationship("DetalleNRC", back_populates="nrc", cascade="all, delete-orphan")


class DetalleNRC(Base):
    __tablename__ = 'detalles_nrc'

    id = Column(Integer, primary_key=True)
    aula = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    cupo = Column(Integer, nullable=False)
    nrc_id = Column(Integer, ForeignKey('nrcs.id'))
    nrc = relationship("NRC", back_populates="detalles")



