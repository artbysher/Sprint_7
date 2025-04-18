import allure
import pytest

from data import color_scooter
from generators import generate_order_body
from methods.order_methods import OrdersMethods


class TestListOrders:

    @allure.title('Тест получения списка заказов')


    def test_get_list_order(self):
        list_order = OrdersMethods.get_list_order()

        assert list_order.status_code == 200 and "orders" in list_order.json()

