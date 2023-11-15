from typing import Self

from flask_restx import fields
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

from core import db, api, secret_key


class Hint(db.Model):
    __tablename__ = "hints"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    service_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[StringEncryptedType] = mapped_column(
        StringEncryptedType(
            String,
            secret_key,
            AesEngine,
            "pkcs5",
        ),
        nullable=False,
    )

    @classmethod
    def find_by_name(cls, service_name: str) -> Self | None:
        return db.session.query(cls).filter_by(service_name=service_name).first()

    @classmethod
    def find_by_part(cls, service_name: str) -> list[Self]:
        pass_list = db.session.query(cls).filter(cls.service_name.like(f"{service_name}%")).all()
        return pass_list

    @classmethod
    def create(cls, service_name: str, password: str) -> Self:
        new_hint = cls(
            service_name=service_name,
            password=password,
        )
        db.session.add(new_hint)
        db.session.commit()
        return new_hint

    def update(self, password: str) -> Self:
        if self.password != password and password is not None:
            self.password = password
            db.session.add(self)
            db.session.commit()
        return self

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()


hint_model = api.model("Hint", {
    "service_name": fields.String,
    "password": fields.String,
})

password_model = api.model("Hint",{
    "password": fields.String,
})

