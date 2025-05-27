import requests
import pytest
from data import Url, Login
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


@pytest.fixture(scope="function", autouse=True)
def cleanup_courier():
    yield
    response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=Login.LOGIN_DATA)
    if response.status_code == 200:
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER.replace(":id", str(courier_id))}')

