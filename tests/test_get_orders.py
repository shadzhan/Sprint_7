import requests
import pytest
import allure
from data import Url
from data import Data






def test_get_order_list():
    response = get_orders()
    assert response.status_code == 200
    assert isinstance(response.json(), list)
