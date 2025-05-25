import pytest
import requests
import allure
from data import Url, DataForOrderList


@allure.feature("Получение списка заказов")
class TestGetOrders:
    @allure.title("Проверка списка заказов")
    def test_get_order_list(self):
        params = DataForOrderList.CREATE_ORDER_LIST

        response = requests.get(Url.ORDERS, params=params)
        assert response.status_code == 200
        assert isinstance(response.json().get("orders", []), list)
