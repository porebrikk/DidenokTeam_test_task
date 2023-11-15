from flask.testing import FlaskClient
from pytest import mark, param
from werkzeug.test import TestResponse

from app.password.password_db import Hint
from app.core import db


@mark.order(0)
@mark.parametrize(
    ("service_name", "password", "code", "response"),
    [
        param("first_service", "valid", 200, {"password": "valid"}),
        param("wrong_service", None, 400, {"message": "No password entered"}),
    ]
)
def test_create(
        client: FlaskClient,
        service_name: str,
        password: str,
        code: int,
        response: dict[str, str],
):
    result: TestResponse = client.post(
        f"/password/{service_name}",
        json={"password": password},
    )
    assert result.status_code == code
    assert result.json == response

    if code == 200:
        hint: Hint = Hint.find_by_name(service_name)
        assert hint.password == password
        hint.delete()
    assert Hint.find_by_name(service_name) is None


@mark.order(1)
@mark.parametrize(
    ("password", "expect"),
    [
        param("new_pass", "new_pass"),
        param(None, "test_pass")
    ]
)
def test_update(
        client: FlaskClient,
        test_hint: Hint,
        password: str | None,
        expect: str,
):
    print(test_hint)
    result: TestResponse = client.post(
        f"/password/{test_hint.service_name}",
        json={"password": password},
    )

    assert result.status_code == 200
    assert result.json == {"password": expect}

    hint = Hint.find_by_name(test_hint.service_name)
    assert hint.password == expect


@mark.order(2)
def test_get(
        client: FlaskClient,
        test_hint: Hint,
):
    result: TestResponse = client.get(f"/password/{test_hint.service_name}")
    result_list: TestResponse = client.get(
        f"/password/?service_name={test_hint.service_name[0:len(test_hint.service_name)-2]}"
    )
    expect_dict = {
        "service_name": test_hint.service_name,
        "password": test_hint.password
    }

    assert result.status_code == 200
    assert result.json == expect_dict

    assert isinstance(result_list.json, list)
    assert result_list.json[0] == expect_dict


