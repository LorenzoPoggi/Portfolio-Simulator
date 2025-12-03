# models.py
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.database import Base

# ----------------------------------------------------------------
# Tablas de la Base de Datos
# ----------------------------------------------------------------

class User(Base):
    __tablename__ = "Usuarios"
    # ID unico asignado a cada usuario
    id = Column(Integer, primary_key=True, index=True)
    # Datos Personales
    fullname = Column(String, unique=False) 
    email = Column(String, unique=True, index=True)
    password = Column(String)
    # Datos Secundarios
    is_active = Column(Boolean, default= True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # Relacion: El usuario tiene su propio portfolio
    portfolio = relationship('User_Portfolio', back_populates='usuario')

class Stock(Base):
    __tablename__ = "Stock"
    # ID unico asignado a cada activo
    id = Column(Integer, primary_key=True, index=True)
    # Informacion de cada activo
    name = Column(String, unique=True)
    symbol = Column(String, unique=True)
    sector = Column(String) # OPTIONAL
    # Parametros de cada activo
    price = Column(Float) 
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    currency = Column(String, default='USD')
    # Relacion: El activo pertenece al portfolio de cada usuario
    portfolio = relationship('User_Portfolio', back_populates='stock')

class User_Portfolio(Base):
    __tablename__ = "User_Portfolio"
    # ID unico asignado a cada portfolio
    id = Column(Integer, primary_key=True, index=True)
    # Caracterisiticas personales del portfolio
    user_id = Column(Integer, ForeignKey('Usuarios.id'))
    stock_id = Column(Integer, ForeignKey('Stock.id'))
    # Caracteristicas generales del portfolio
    quantity = Column(Integer)
    buy_price = Column(Float)
    total_invested = Column(Float)
    buy_date = Column(DateTime(timezone=True), server_default=func.now())
    average_price = Column(Float)
    # Relacion: El usuario tiene su propio Portfolio
    usuario = relationship("User", back_populates='portfolio')
    stock = relationship("Stock", back_populates='portfolio')