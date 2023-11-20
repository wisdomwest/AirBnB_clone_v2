#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents a database storage engine

    Attributes:
        __engine: engine.
        __session: session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a DBStorage instance"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session(self.__session)
        all objects depending of the class name (argument cls)
        if not cls query all types of objects(User...)
        Return:
            Dict lasses in format <class name>.<obj id> = obj
        """
        classes = {
                'State': State, 'City': City, 'User': User,
                'Place': Place, 'Review': Review, 'Amenity': Amenity,
        }
        objects = {}

        if cls is None:
            for class_name, class_type in classes.items():
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        elif cls in classes:
            query = self.__session.query(classes[cls])
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj

        return objects


    def new(self, obj):
        """Add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in db and init"""
        Base.metadata.create_all(self.__engine)
        session_f = sessionmaker(bind=self.__engine,
                                 expire_on_commit=False)
        Session = scoped_session(session_f)
        self.__session = Session()
