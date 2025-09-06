from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from core.config import settings

engine=create_engine(settings.DATABASE_URL)

session=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"error of type {type(e).__name__)} occured :  {e}")
        raise
    finally:
        db.close()
        
def create_tables():
    Base.metadata.create_all(bind=engine)
    
