#!/usr/bin/python3
"""This module defines a class to manage DBstorage for hbnb clone"""

from sqlalchemy import create_engine, MetaData
import os


class DBStorage():
    """This class manages storage of hbnb models to DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Instatntiates"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))
        
        # if os.getenv('HBNB_ENV') == 'test':
            # from models.base_model import Base
            # Base.metadata.drop_all()

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""

        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State
        
        res = {}
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        for cls in classes:
            objs = self.__session.query(cls)
            for obj in objs.all():
                key = '{}.{}'.format(cls.__name__, obj.id)
                res[key] = obj

        query = self.__session.execute("SELECT COUNT(*) FROM states")
        print(query.fetchone()[0])

        return res    
    
    def new(self, obj):
        """Add the object to the current database session"""
        
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        
        if obj is not None:
            self.__session.delete(obj)
        
    def reload(self):
        """create all tables in the database"""

        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State
        from sqlalchemy.orm import sessionmaker, scoped_session

        if os.getenv('HBNB_ENV') == 'test':
            from models.base_model import Base
            Base.metadata.drop_all()

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        '''Close a session'''

        self.__session.close()
