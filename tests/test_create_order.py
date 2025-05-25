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
    def test_create_order_with_colors(self, color):
        order_data = deepcopy(DataForOrderActions.CREATE_ORDER_BODY)
        order_data["color"] = color
        response = requests.post(
            f'{Url.BASE_URL}{Url.ORDER_URL}',
            json=order_data
        )

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('Создание заказа без указания цвета')

    def test_create_order_without_color(self):
        order_data = DataForOrderActions.CREATE_ORDER_BODY.copy()
        del order_data["color"]

        with allure.step("Создаем заказ без цвета"):
            response = requests.post(
                f"{Url.BASE_URL}{Url.ORDER_URL}",
                json=order_data
            )

        with allure.step("Проверяем ответ"):
            assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
            assert "track" in response.json(), "В ответе отсутствует track-номер"

        with allure.step("Отменяем заказ"):
            track = response.json()["track"]
            cancel_response = requests.put(f'{Url.BASE_URL}{Url.CANCEL_ORDER}{track}')
            assert cancel_response.status_code == 200, "Не удалось отменить заказ"

