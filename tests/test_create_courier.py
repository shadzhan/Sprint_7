import pytest
import allure
import requests
from generators import register_new_courier
from data import Url
from create_courier import CreateCourier



class TestCreateCourier:
    @pytest.fixture
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, create_courier):
        response, login, password = create_courier
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Создание дубликата курьера")
    def test_create_duplicate(self):
        login, password, _ = register_new_courier()
        CreateCourier.create_courier(login, password, "AnyName")
        response = CreateCourier.create_courier(login, password, "AnyName")
        assert response.status_code == 409
        assert "уже используется" in response.json()["message"]


    @allure.title("Отсутствие обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_missing_fields(self, missing_field):
        data = {"login": "test", "password": "123", "firstName": "name"}
        del data[missing_field]
        response = requests.post(Url.CREATE_COURIER_URL, json=data)
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json()["message"]
