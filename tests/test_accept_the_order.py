import allure

from generators import generate_order_body
from methods.courier_methods import CourierMethods
from methods.order_methods import OrdersMethods


class TestAcceptOrder:

    @allure.title('Тест на успешное принятие заказа')
    @allure.description('Создаем курьера, получаем id,создаем заказ и получаем id заказа и проверяем запрос на принятие курьером заказа возвращает правильный код ответа 200 и {"ok":true}')
    def test_success_accept_order(self, generate_courier_data):
        #Создаем курьера и получаем его ID
        CourierMethods.create_courier(generate_courier_data[0])
        courier_id = CourierMethods.get_courier_id(generate_courier_data[1], generate_courier_data[2])
        # Создаем заказ и получаем список заказов а отутда ID заказа
        new_order = OrdersMethods.create_order(generate_order_body(["BLACK"]))
        track = new_order.json().get("track")
        order_id = OrdersMethods.get_order_id(track)

        accept_response = OrdersMethods.accept_order(order_id, courier_id)
        assert accept_response.status_code == 200 and accept_response.json() == {"ok": True}

    @allure.title('Тест на получение ошибки принятии заказа без id курьера')
    def test_accept_order_without_courier_id(self):
        # Создаем заказ и получаем список заказов а отутда ID заказа
        new_order = OrdersMethods.create_order(generate_order_body(["BLACK"]))
        track = new_order.json().get("track")
        order_id = OrdersMethods.get_order_id(track)

        accept_response = OrdersMethods.accept_order(order_id, courier_id='')
        assert accept_response.status_code == 400 and accept_response.json().get("message") == "Недостаточно данных для поиска"


    @allure.title('Тест на получение ошибки приняти заказа без id заказа')
    def test_accept_order_without_order_id(self, generate_courier_data):
        # Создаем курьера и получаем его ID
        CourierMethods.create_courier(generate_courier_data[0])
        courier_id = CourierMethods.get_courier_id(generate_courier_data[1], generate_courier_data[2])
        accept_response = OrdersMethods.accept_order(order_id='',courier_id=courier_id)
        assert accept_response.status_code == 400 and accept_response.json().get(
            "message") == "Недостаточно данных для поиска"

    @allure.title('Тест на получение ошибки приняти заказа c неверным id курьера')
    def test_accept_order_invalid_courier_id(self):
        # Создаем заказ и получаем список заказов а отутда ID заказа
        new_order = OrdersMethods.create_order(generate_order_body(["BLACK"]))
        track = new_order.json().get("track")
        order_id = OrdersMethods.get_order_id(track)
        courier_id = 000000
        accept_response = OrdersMethods.accept_order(order_id, courier_id)
        assert accept_response.status_code == 404 and accept_response.json().get(
            "message") == "Курьера с таким id не существует"

    @allure.title('Тест на получение ошибки приняти заказа с неверным id заказа')
    def test_accept_order_invalid_order_id(self, generate_courier_data):
        # Создаем курьера и получаем его ID
        CourierMethods.create_courier(generate_courier_data[0])
        courier_id = CourierMethods.get_courier_id(generate_courier_data[1], generate_courier_data[2])
        order_id = 000000
        accept_response = OrdersMethods.accept_order(order_id,courier_id)
        assert accept_response.status_code == 404 and accept_response.json().get(
            "message") == "Заказа с таким id не существует"
