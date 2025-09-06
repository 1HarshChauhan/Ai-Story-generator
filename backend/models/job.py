from sqlalchemy import Column,Integer,Boolean,DateTime,String
from sqlalchemy.sql import func

from db.database import Base

class StoryJob(Base):
    __tablename__="Story_jobs"
    
    id=Column(Integer,primary_key=True)
    job_id=Column(String,unique=True)
    session_id=Column(String,nullable=False)
    theme=Column(String)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    completed_job=Column(DateTime(timezone=True),nullable=True)
    error=Column(String,nullable=True)
    status=Column(String) 