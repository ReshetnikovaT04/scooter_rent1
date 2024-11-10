#Решетникова Татьяна 23 когорта 11 спринт
# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
from http.client import responses

import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

def test_create_order_get_success_response():
    response = sender_stand_request.post_orders(body=data.order_body)
    number_track=response.json()['track']
    order_details_response=sender_stand_request.get_orders_details(track=number_track)
    print(number_track)
    # Проверка, что код ответа равен 200
    assert order_details_response.status_code == 200






