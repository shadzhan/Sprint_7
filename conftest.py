import requests
import pytest
from data import Url
from courier_auth import register_new_courier_and_return_login_password
from create_order import OrderActions
from generators import register_new_courier



@pytest.fixture
def registered_courier():
    login, password, _ = register_new_courier()
    return {"login": login, "password": password}


@pytest.fixture
def created_order(order_data):
    order = OrderActions.create_order(order_data)
    order_track = order.json()["track"]
    yield order_track
    OrderActions.cancel_order(order_track)

@pytest.fixture
def delete_courier_data():

    login_pass = register_new_courier_and_return_login_password()
    yield {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data=login_pass)
    if response.status_code == 200:
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}{courier_id}')


@pytest.fixture(scope="function", autouse=True)
def cleanup_function():
    yield
    login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data={
        "login": "test_courier",
        "password": "test_password"
    })
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        if courier_id:
            requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}{courier_id}')