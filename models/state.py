#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import relationship

class State(BaseModel, Base):
    """"Represents city 
    Attributes:
        __tablename__: The name of table states
        name: name of state
        cities: cities
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', credits='delete')
    else:
        @property
        def cities(self):
            """returns the list of City instances"""
            cList = []
            for city in list(models.storage.all(City).values()):
                if city.state.id == self.id:
                    cList.append(city)
            return cList
                    
                

