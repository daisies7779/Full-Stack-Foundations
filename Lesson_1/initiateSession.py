# This script initiates session
# import dependencies from sqlachemy and db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

#let's our program know which db engine we want to
#communicate with
engine = create_engine('sqlite:///restaurantmenu.db')

#bind the engine to the base class
#makes connections between our class defenitions
#and correspondin tables within db
Base.metadata.bind = engine 
#create session maker object to establish a link
#between code execution and creted engine.
#session is an interface whic allows to write commands
# we want to execute but not send them to db before commit
DBSession = sessionmaker(bind=engine)

#create instance of DBSession and call it session
session = DBSession()
