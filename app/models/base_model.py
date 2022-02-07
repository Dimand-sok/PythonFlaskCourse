from argparse import ArgumentError
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, func, true 

class BaseModel:
    id = Column(Integer,primary_key=True, autoincrement=true)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())