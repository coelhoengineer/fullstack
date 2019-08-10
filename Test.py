from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from databaseSetup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBConnection = sessionmaker(bind=engine)
session = DBConnection()

menuItens = session.query(MenuItem)
for i in menuItens:
    print(i.id)
    print(i.name)
    print(i.price)