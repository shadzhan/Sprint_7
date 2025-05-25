import pytest
import allure
import requests
from generators import register_new_courier
from data import Url



@allure.feature('Создание курьера')
class CreateCourier:

    @staticmethod
    @allure.title('Успешное создание курьера')
    def create_courier_success(login, password, first_name="Rumba"):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json={
            "login": login,
            "password": password,
            "firstName": first_name
        })
        return response

    @staticmethod
    @allure.title('Создание дубликата курьера')
    def create_duplicate_courier(login, password):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json={
            "login": login,
            "password": password,
            "firstName": "Duplicate"
        })
        return response

    @staticmethod
    @allure.title('Создание курьера без обязательных полей')
    def create_courier_with_missing_fields():
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json={})
        return response
