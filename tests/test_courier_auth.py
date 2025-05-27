import requests
import pytest
import allure
from data import Url, Data

@allure.title('Авторизация курьера')
class TestLoginCourier:
    @allure.title('Успешная авторизация')
    def test_login_courier_success(self, registered_courier):
        response = requests.post(f"{Url.BASE_URL}{Url.LOGIN_URL}", json={
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        })
        assert response.status_code == 200
        response_data = response.json()
        assert "id" in response_data, "Ответ должен содержать ID курьера"
        assert isinstance(response_data["id"], int), "ID курьера должен быть числом"

    @allure.title('Авторизация с неверным паролем')
    def test_login_wrong_password(self, registered_courier):
        response = requests.post(f"{Url.BASE_URL}{Url.LOGIN_URL}", json={
            "login": registered_courier["login"],
            "password": "неверный_пароль"
        })
        assert response.status_code == 404
        assert response.json() == {"message": "Учетная запись не найдена"}, "Неверное сообщение об ошибке"

    @allure.title('Авторизация с некорректными данными')
    @pytest.mark.parametrize("invalid_data", Data.INVALID_TEST_DATA)
    def test_login_invalid_credentials(self, invalid_data):
        response = requests.post(f"{Url.BASE_URL}{Url.LOGIN_URL}", json=invalid_data)
        assert response.status_code == 400
        assert "message" in response.json(), "Ответ должен содержать поле message"

    @allure.title("Авторизация без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_fields(self, registered_courier, missing_field):
        data = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        del data[missing_field]

        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=data)
        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для входа"}, "Неверное сообщение об ошибке"