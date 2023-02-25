from pytest_voluptuous import S

import schemas.schemas
from utils.base_session import regres


def test_create_user():
    create_user = regres.post("/users", {"name": "Irina", "job": "QA"})

    assert create_user.status_code == 201
    assert create_user.json()["name"] == "Irina"
    assert create_user.json()["job"] == "QA"
    assert S(schemas.schemas.create_single_user) == create_user.json()


def test_update_user():
    update_user = regres.put("/users/2", {"name": "Irina Rogova", "job": "tester"})

    assert update_user.status_code == 200
    assert update_user.json()["name"] == "Irina Rogova"
    assert update_user.json()["job"] == "tester"
    assert update_user.json()["updatedAt"] is not None
    assert S(schemas.schemas.update_single_user) == update_user.json()


def test_delete_user():
    delete_user = regres.delete("/users/2")

    assert delete_user.status_code == 204


def test_login_successful():
    login_successfully = regres.post("/login", {"email": "eve.holt@reqres.in", "password": "cityslicka"})

    assert login_successfully.status_code == 200
    assert login_successfully.json()["token"] is not None
    assert S(schemas.schemas.login_successfully) == login_successfully.json()


def test_login_unsuccessful():
    login_unsuccessful = regres.post("/login", {"email": "neit.@f"})

    assert login_unsuccessful.status_code == 400
    assert len(login_unsuccessful.content) != 0