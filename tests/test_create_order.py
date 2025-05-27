import pytest
import requests
import allure
from copy import deepcopy
from data import Url, DataForOrderActions


@allure.feature('Создание заказа')
class TestOrderCreation:
    @allure.title('Проверка создания заказа с разными цветами: {color}')
    @pytest.mark.parametrize(
        'color',
        DataForOrderActions.ORDER_COLORS,
        ids=DataForOrderActions.COLOR_IDS
    )
    def test_create_order_with_colors(self, color, created_order):
        order_data = deepcopy(DataForOrderActions.CREATE_ORDER_BODY)
        order_data["color"] = color

        track = created_order(order_data)

        response = requests.get(f"{Url.BASE_URL}{Url.ORDER_URL}/{track}")
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует track-номер"

    @allure.title('Создание заказа без указания цвета')
    def test_create_order_without_color(self, created_order):
        order_data = DataForOrderActions.CREATE_ORDER_BODY.copy()
        del order_data["color"]

        track = created_order(order_data)

        response = requests.get(f"{Url.BASE_URL}{Url.ORDER_URL}/{track}")
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует track-номер"