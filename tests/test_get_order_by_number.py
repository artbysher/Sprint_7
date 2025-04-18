import allure

from generators import generate_order_body

from methods.order_methods import OrdersMethods


class TestGetOrderByNomber:

    @allure.title('Тест на успешное принятие заказа')
    def test_success_get_order(self):
        #Создаем заказ и получаем трек номер
        new_order = OrdersMethods.create_order(generate_order_body(["BLACK"]))
        track = new_order.json().get("track")
        get_response = OrdersMethods.get_order(track)
        assert get_response.status_code == 200 and "order" in get_response.json()

    @allure.title('Тест получение ошибки при запросе без номера заказа')
    def test_without_nomber_order(self):
        track = ''
        get_response = OrdersMethods.get_order(track)
        assert get_response.status_code == 400 and get_response.json().get("message") == "Недостаточно данных для поиска"

    @allure.title('Тест получение ошибки при запросе c несуществующим номером заказа')
    def test_invalid_nomber_order(self):
        track = 000000
        get_response = OrdersMethods.get_order(track)
        assert get_response.status_code == 404 and get_response.json().get(
            "message") == "Заказ не найден"