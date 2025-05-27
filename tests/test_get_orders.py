import pytest
import requests
import allure
from data import Url, DataForOrderList



@allure.feature("Получение списка заказов")
class TestGetOrders:
    @allure.title("Проверка списка заказов")
    def test_get_order_list(self):
        params = DataForOrderList.CREATE_ORDER_LIST

        response = requests.get(f"{Url.BASE_URL}{Url.ORDER_URL}", params=params)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        response_json = response.json()
        assert "orders" in response_json, "Ответ не содержит ключ 'orders'"
        assert isinstance(response_json["orders"], list), "Ключ 'orders' не является списком"
