#!/usr/bin/python3
"""new HBNB storage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage(Base):
    """storage class for storing"""
    __engine = None
    __session = None

    def __init__(self):
        """on initialization"""
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "{}+{}://{}:{}@{}/{}".format(
                dialect, driver, user, passwd, host, db
            ), pool_pre_ping=True
        )
        if os.getenv("HBNB_ENV") in ("test", "dev"):
            Base.metadata.drop_all(self.__engine)
