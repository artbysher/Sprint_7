import random

import allure

from generators import generate_courier_body
from methods.courier_methods import CourierMethods


class TestDeleteCourier:
    @allure.title('Тест на успешное уудаление курьера')
    @allure.description('Создаем курьера, получаем его id и проверяем успешное удаление, код 200, сообщение {ok: true} ')
    def test_delete_courier(self):
        courier_body = generate_courier_body()
        login = courier_body['login']
        password = courier_body['password']
        courier = CourierMethods.create_courier(courier_body)
        courier_id = CourierMethods.get_courier_id(login,password)
        deleted_courier = CourierMethods.delete_courier(courier_id)

        assert deleted_courier.status_code == 200 and deleted_courier.json() == { "ok": True }

    @allure.title('Тест на получение ошибки при запросе без id')

    def test_delete_courier(self):
        deleted_courier = CourierMethods.delete_courier(None)

        assert deleted_courier.status_code == 400 and deleted_courier.json().get("message") == "Недостаточно данных для удаления курьера"

    @allure.title('Тест на получение ошибки при запросе с несуществующим id')
    def test_delete_courier(self):
        deleted_courier = CourierMethods.delete_courier(random.randint(100, 999))

        assert deleted_courier.status_code == 404 and deleted_courier.json().get(
                "message") == "Курьера с таким id нет."

