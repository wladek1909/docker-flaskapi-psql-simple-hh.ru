from __init__ import db
from sqlalchemy import Column, DateTime, Integer, MetaData, Table
from dataclasses import dataclass
from sqlalchemy.sql import func


@dataclass
class Question(db.Model):
    idanswer: str
    question: str
    answer: str
    created_at: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.String(1000))
    answer = db.Column(db.String(1000))
    question = db.Column(db.String(100000))
    idanswer = db.Column(db.String(1000), unique=True)