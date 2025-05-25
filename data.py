class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = '/api/v1/courier'
    LOGIN_URL = '/api/v1/courier/login'
    ORDER_URL = '/api/v1/orders'
    CANCEL_ORDER = "/api/v1/orders/cancel"

class DataForCourierCreation:
    CREATE_COURIER_BODY = {
    "login" : "mamba",
    "password" : "4569",
    "firstName" : 'zumba'
    }

class DataForAuth:
    REGISTER_NEW_COURIER_AND_RETURN_LOGIN_PASSWORD = {
    "login" : "mamba",
    "password" : "4569"
    }


class DataForOrderActions:
    CREATE_ORDER_BODY = {
        "firstName": "Petrov",
        "lastName": "Igor",
        "address": "Zinina, 148 apt.",
        "metroStation": 9,
        "phone": "+7 897 391 35 89",
        "rentTime": 5,
        "deliveryDate": "2025-06-06",
        "comment": "Mamba, call twice",
        "color": ["BLACK"]
    }

    ORDER_COLORS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]

    COLOR_IDS = ["black", "grey", "both_colors", "no_color"]

    CREATE_ORDER_WITHOUT_COLOR = {
        "firstName": "Mark",
        "lastName": "Volkov",
        "address": "Zorge 1",
        "metroStation": 9,
        "phone": "+79174859633",
        "rentTime": 5,
        "deliveryDate": "2025-05-24",
        "comment": "Welcome!"
    }


class DataForOrderList:
    CREATE_ORDER_LIST = {

             "courierId": "damba",
             "nearestStation": ['1', '2'],
             "limit": 10,
             "page": 1
    }


class Data:
    INVALID_TEST_DATA = {

              "login": "сталкер",
              "password": "один"
    }