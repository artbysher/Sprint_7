import allure

from generators import generate_courier_body
from methods.courier_methods import CourierMethods



class TestCreateCourier:

    @allure.title('Тест на успешное создание курьера')
    @allure.description('Создаем курьера и проверяем запрос возвращает правильный код ответа и {"ok":true}')
    def test_success_create_courier(self, generate_courier_data):
        courier = CourierMethods.create_courier(generate_courier_data[0])
        assert courier.status_code == 201 and courier.json() == { "ok": True }

    @allure.title('Тест на получение ошибки при попытке создании двух одинаковых курьеров')
    @allure.description('Создаем последовательно двух курьеров передавая одинаковые данные логин, пароль, имя и проверяем что возвращается ошибка')
    def test_create_duplicate_courier(self, generate_courier_data):
        courier1 = CourierMethods.create_courier(generate_courier_data[0])
        courier2 = CourierMethods.create_courier(generate_courier_data[0])
        assert courier1.status_code == 201 and courier2.status_code == 409 and courier2.json().get("message") == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Тест на получение ошибки при попытке создания курьеров с одинаковыми логинами')
    @allure.description(
        'Создаем последовательно двух курьеров передавая одинаковые логины и проверяем, что возвращается ошибка')
    def test_create_duplicate_courier(self, generate_courier_data):
        courier1 = CourierMethods.create_courier(generate_courier_data[0])
        body2 = generate_courier_body() #генерируем тело для второго курьера
        body2["login"] = generate_courier_data[1] # заменяем логин, на логин первого курьера
        courier2 = CourierMethods.create_courier(body2)

        assert courier1.status_code == 201 and courier2.status_code == 409 and courier2.json().get(
            "message") == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Тест на получение ошибки при попытке создания курьера без логина')
    @allure.description('Пытаемся создать курьера передавая тело без логина и проверяем, что возвращается ошибка')
    def test_create_courier_without_login(self):
        courier_body = generate_courier_body()
        courier_body.pop("login")
        courier = CourierMethods.create_courier(courier_body)

        assert courier.status_code == 400 and courier.json().get(
            "message") == "Недостаточно данных для создания учетной записи"

    @allure.title('Тест на получение ошибки при попытке создания курьера без пароля')
    @allure.description('Пытаемся создать курьера передавая тело без пароля и проверяем, что возвращается ошибка и сообщение Недостаточно данных для создания учетной записи')
    def test_create_courier_without_password(self):
        courier_body = generate_courier_body()
        courier_body.pop("password")
        courier = CourierMethods.create_courier(courier_body)

        assert courier.status_code == 400 and courier.json().get(
            "message") == "Недостаточно данных для создания учетной записи"