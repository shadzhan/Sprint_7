import requests
import json
import requests
import pytest
import allure
from data import Url



class GetListOfOrders:


    @staticmethod
    def get_orders(courier_id=None, nearest_station=None, limit=30, page=0):
        params = {}
        if courier_id is not None:
            params['courierId'] = courier_id
        if nearest_station is not None:
            filter_obj = {"nearestStation": nearest_station}
            params['nearestStation'] = json.dumps(filter_obj)
        params['limit'] = limit
        params['page'] = page

        response = requests.get(f'{Url.BASE_URL}{Url.ORDER_URL}', params=params)
        return response
