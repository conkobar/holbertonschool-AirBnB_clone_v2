#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
import os
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
       # amenities = relationship("Amenity", secondary="place_amenity",
        #                         viewonly=False, backref="place_amenities")
    else:
        @property
        def reviews(self):
            """att for filestorage"""
            from models import storage
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]

        #@property
        #def amenities(self):
            #"""getter for amenity when use filestorage"""
            #from models import storage
            #return [amenity for amenity in storage.all(Amenity).values()
                   # if amenity.id in self.amenity_ids]

       # @amenities.setter
        #def amenities(self, obj):
         #   """adds an ammenity to list"""
          #  from models import storage
           # if isinstance(value, Amenity):
            #    amenity_ids.append(value_id)
