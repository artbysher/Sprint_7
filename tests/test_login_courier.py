import random

import allure

from generators import generate_courier_body
from methods.courier_methods import CourierMethods



class TestLoginCourier:

    @allure.title('Тест на успешную авторизацию курьера')
    @allure.description('Создаем курьера и проверяем что с этими логином и паролем курьер может авторизоваться, код 200 и в теле ответа присутсвует id')
    def test_auth_courier(self, generate_courier_data):
        CourierMethods.create_courier(generate_courier_data[0])
        courier_login = CourierMethods.login_courier(generate_courier_data[1],generate_courier_data[2])

        assert courier_login.status_code == 200 and "id" in courier_login.json()

    @allure.title('Тест на ошибку при  авторизации под несуществующим пользователем')
    @allure.description(
        'Вводим логин и пароль несуществующего курьера и проверяем что получаем ошибку 404 и сообщение "Учетная запись не найдена"' )
    def test_auth_with_invalid_user(self):
        courier_body = generate_courier_body()
        login = courier_body['login']
        password = courier_body['password']
        courier_login = CourierMethods.login_courier(login,password)

        assert (courier_login.status_code == 404
                and courier_login.json().get("message") == "Учетная запись не найдена")

    @allure.title('Тест на получение ошибки при авторизации без обязательного поля логин')
    @allure.description(
        'Создаем курьера и передаем на авторизацию только пароль, код 400 и в теле ответа "Недостаточно данных для входа"')
    def test_create_duplicate_courier(self, generate_courier_data):
        courier = CourierMethods.create_courier(generate_courier_data[0])
        courier_login = CourierMethods.login_courier(None, generate_courier_data[2])

        assert (courier_login.status_code == 400
                and courier_login.json().get("message") == "Недостаточно данных для входа")

    @allure.title('Тест на получение ошибки при авторизации без обязательного поля пароль')
    @allure.description(
        'Создаем курьера и передаем на авторизацию только логин, код 400 и в теле ответа "Недостаточно данных для входа"')
    def test_create_duplicate_courier(self, generate_courier_data):
        courier = CourierMethods.create_courier(generate_courier_data[0])
        courier_login = CourierMethods.login_courier(generate_courier_data[1],None)

        assert (courier_login.status_code == 400
                and courier_login.json().get("message") == "Недостаточно данных для входа")

    @allure.title('Тест на получение ошибки при авторизации с неверным паролем')
    @allure.description(
        'Создаем курьера и передаем на авторизацию только логин, код 404 и в теле ответа "Учетная запись не найдена"')
    def test_create_duplicate_courier(self, generate_courier_data):
        courier = CourierMethods.create_courier(generate_courier_data[0])
        courier_login = CourierMethods.login_courier(generate_courier_data[1], random.randint(1000, 9999))

        assert (courier_login.status_code == 404
                and courier_login.json().get("message") == "Учетная запись не найдена")
