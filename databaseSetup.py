# -*- coding: utf-8 -*-
import os
import sys
from sqlalchemy import create_engine, engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class MenuItem(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(String)
    course = Column(String)
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.bind = engine
Base.metadata.create_all(engine)
