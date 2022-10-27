#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
import os
import models
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(
        String(128),
        nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship(
            'City',
            backref='state',
            cascade='all, delete, delete-orphan'
        )
    else:
        @property
        def cities(self):
            """returns list of city instances"""
            towns = []
            for town in models.storage.all(City).values():
                if town.state_id == self.id:
                    towns.append(town)
            return towns
