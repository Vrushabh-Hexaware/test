from sqlalchemy.orm import sessionmaker
from db.connection import engine

def get_session():
    session = sessionmaker(bind=engine)
    return session()