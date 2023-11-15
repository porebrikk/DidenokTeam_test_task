from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
api = Api()

secret_key = "X)6-JxhnP:qMxGgj4th[W/@FKFG/x("
