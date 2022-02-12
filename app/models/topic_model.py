from argparse import ArgumentError
from email.mime import base

from sqlalchemy import Column,String

from app.database import Base
from .base_model import BaseModel

class TopicModel (Base, BaseModel):

    __tablename__ = "tblTopic"

    title = Column(String(250))


    def __init__(self, schema):
        if not isinstance(schema, dict):
            raise ArgumentError("schema should be a dict")

        for key, value in schema.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)