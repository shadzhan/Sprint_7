import requests
import pytest
import allure
import random
from data import Url
from data import Data



@allure.title('Авторизация курьера')
class TestLoginCourier:
    @allure.step("Успешная авторизация")
    def test_login_courier_success(self, registered_courier):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json={
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.step("Авторизация с неверным паролем")
    def test_login_wrong_password(self, registered_courier):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json={
            "login": registered_courier["login"],
            "password": "один"
        })
        assert response.status_code == 404

    @allure.step("Авторизация с неверными данными")
    @pytest.mark.parametrize("invalid_data",Data.INVALID_TEST_DATA)
    def test_login_invalid_credentials(self, invalid_data):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=invalid_data)
        assert response.status_code == 404

    @allure.step("Авторизация без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_fields(self, registered_courier, missing_field):
        data = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        del data[missing_field]

        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=data)
        assert response.status_code == 400