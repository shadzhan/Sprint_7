import requests
from data import Url
from data import DataForOrderActions


class OrderActions:
    @staticmethod
    def create_order(order_body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=order_body)
