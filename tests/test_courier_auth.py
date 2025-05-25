import requests
import pytest
import allure
import random
from data import Url




@allure.title('Успешная авторизация курьера')
class TestLoginCourier:
    def test_login_courier_success(self, registered_courier, BASE_URL=None):
        response = requests.post(BASE_URL + 'api/v1/courier/login', json={
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Авторизация с неверным паролем')
    def test_login_wrong_password(self, registered_courier):
        response = requests.post(API_URL + '/courier/login', json={
            "login": registered_courier["login"],
            "password": "wrong_password"
        })
        assert response.status_code == 404