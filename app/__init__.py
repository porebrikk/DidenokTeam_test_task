from flask import Flask

from app.core import api, db, Base
from app.password.password_rst import controller


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite3"

api.init_app(app)
db.init_app(app)

api.add_namespace(controller)

with app.app_context():
    Base.metadata.create_all(db.engine)
