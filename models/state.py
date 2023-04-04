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
        cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """getter method for cities"""
        cityl = []
        all_cities = storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                cityl.append(city)
        return cityl

    def __str__(self):
        return "[State] ({}) {}".format(self.id, {
            'name': self.name,
            'id': self.id,
            'updated_at': self.updated_at,
            'created_at': self.created_at
        })


