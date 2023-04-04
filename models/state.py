#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # have cities attribute
        cities = relationship('City', backref='state', cascade='all, delete')
    
    # for fileStorage
    else:
        @property
        def cities(self):
            """getter method for cities"""
            
            cityl= []
            for city in list(storage.all(City).values()):
                    if city.state_id == self.id:
                        cityl.append(city)
            return cityl
    
        
