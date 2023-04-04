#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id', ondelete='CASCADE'), nullable=False)
    places = relationship('Place', back_populates='cities', cascade='all, delete')

    def __init__(self, *args, **kwargs):
        """Custom constructor for City class"""
        super().__init__(*args, **kwargs)
        if "state_id" in kwargs:
            self.state_id = kwargs["state_id"]

    def __str__(self):
        return "[City] ({}) {}".format(self.id, {
            'name': self.name,
            'id': self.id,
            'state_id': self.state_id,
            'updated_at': self.updated_at,
            'created_at': self.created_at
        })

