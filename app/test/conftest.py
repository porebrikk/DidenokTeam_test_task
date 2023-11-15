from pytest import fixture

from app.password.password_db import Hint
from app import app


@fixture(scope="session", autouse=True)
def application_context() -> None:
    with app.app_context():
        yield


@fixture
def client():
    return app.test_client()


@fixture
def test_hint_data() -> dict[str, str]:
    return {"service_name": "test_name", "password": "test_pass"}


@fixture
def test_hint(test_hint_data: dict[str, str]) -> Hint:
    hint: Hint = Hint.create(**test_hint_data)

    # check of creation
    assert Hint.find_by_name(test_hint_data["service_name"]) is not None

    yield hint

    # clear db
    hint.delete()
