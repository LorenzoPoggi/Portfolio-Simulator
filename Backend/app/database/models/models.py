# models.py
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base

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
    symbol = Column(String, unique=True, index=True)
    name = Column(String, unique=True)
    exchange = Column(String)
    currency = Column(String, default='USD')
    sector = Column(String, nullable=True)
    # Parametros de cada activo
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # Relacion: El activo pertenece al portfolio de cada usuario
    portfolio = relationship('User_Portfolio', back_populates='stock')

class Price(Base):
    __tablename__ = 'Price'
    # ID unico asignado a casa precio de los activos
    id = Column(Integer, primary_key=True, index=True)
    # Informacion de volatilidad de los precios
    stock_id = Column(Integer, ForeignKey('Stock.id'))
    price = Column(Float)
    change = Column(Float)
    change_percent = Column(Float)
    # Parametros de los precios
    timestamp = Column(DateTime(timezone=True))
    # Relacion: El precio pertenece a un Stock especifico
    stock = relationship("Stock")

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