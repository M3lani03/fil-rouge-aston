# coding: utf-8
# !/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, ForeignKey

MYSQL_HOST = "db"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = "root"
MYSQL_DB = "users"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER,
                                                                  MYSQL_PWD,
                                                                  MYSQL_HOST,
                                                                  MYSQL_PORT,
                                                                  MYSQL_DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def get_all_users():
    try:
        result = session.query(User).filter_by()
        return result
    except Exception as e:
        print(e)
        return False


def get_user_by_id(User):
    try:
        result = session.query(User).filter_by(email=User.email).first()
        return result
    except Exception as e:
        print(e)
        return False


def add_user(email, nom, prenom, telephone):
    try:
        user = User(email=email,
                    nom=nom,
                    prenom=prenom,
                    telephone=telephone)

        session.add(user)
        session.commit()
        return True

    except Exception as e:
        print(e)
        return False


class User(Base):
    """
    Cette classe correspond à la version objet de notre table user
    """
    __tablename__ = 'user'
    email = Column(String(120), unique=True, nullable=False, primary_key=True)
    nom = Column(String(80), nullable=False)
    prenom = Column(String(80), nullable=False)
    telephone = Column(String(80), nullable=False)

    def delete_user_by_id(self):
        try:
            user_to_delete = self.get_user_by_id()
            if user_to_delete:
                session.delete(user_to_delete)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def update_attribute(self, attributes):
        try:
            user_to_update = self.get_user_by_id()
            if user_to_update:
                for k, v in attributes.items():
                    setattr(user_to_update, k, v)
                    session.commit()
                return user_to_update
            else:
                return False
        except Exception as e:
            print(e)
            return False
