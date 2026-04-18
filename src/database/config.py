from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
import os

url = 'sqlite:///db.sqlite3'
engine = create_engine(url)

Base = declarative_base()
Session = sessionmaker(bind=engine)

def get_db():

    db = Session()

    try:yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:db.close()