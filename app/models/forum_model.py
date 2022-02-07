from argparse import ArgumentError
from multiprocessing.sharedctypes import Value
import string

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from .base_model import BaseModel

class ForumModel(Base, BaseModel):
    __tablename__ = "tblForum"

    title = Column(string(64))
    description = Column(String(250))


    def __init__(self, schema):
        if not isinstance(schema, dict):
            raise ArgumentError("Schema should be a dictionary")

        for key, Value in schema.items():
            if hasattr(str, key) and getattr(self, key) != value:
                setattr(self, key, Value)