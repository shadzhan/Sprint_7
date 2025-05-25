from data import DataForCourierCreation


def modify_create_courier_body(key, value):
    body = DataForCourierCreation.CREATE_COURIER_BODY.copy()
    body[key] = value
    return body


