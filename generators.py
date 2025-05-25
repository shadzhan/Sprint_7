from faker import Faker
import random
from datetime import datetime, timedelta
import string
from data import Url
import requests


fake = Faker()

def generate_courier_body():
    return {
        "login": fake.user_name(),
        "password": fake.password(length=8),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_courier_data():
    return {
        "login": f"courier_{generate_random_string(8)}",
        "password": generate_random_string(12),
        "firstName": generate_random_string(8)
    }


def register_new_courier():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json=payload)
    if response.status_code == 201:
        return login, password, first_name
    return None

def generate_order_body(colors=None):

    delivery_date = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")

    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.street_address(),
        "metroStation": str(random.randint(1, 250)),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 7),
        "deliveryDate": delivery_date,
        "comment": fake.sentence(nb_words=5),
        "color": colors if colors else random.choice([
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ])
    }



def generate_invalid_order(missing_field):

    order = generate_order_body()
    del order[missing_field]
    return order
