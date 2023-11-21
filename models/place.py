#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=True, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="place")
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            rList = []
            for r in list(models.storage.all(Review).values()):
                if r.place_id == self.id:
                    rList.append(r)
            return rList
        
        @property
        def amenities(self):
            """all Amenity.id linked to the Place"""
            aList = []
            for a in list(models.storage.all(Amenity).values()):
                if a.id in self.amenity_ids:
                    aList.append(a)
            return aList
        
        @amenities.setter
        def amenities(self, data):
            if type(data) == Amenity:
                self.amenity_ids.append(data.id)