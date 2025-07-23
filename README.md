# Sprint_7
## <h>Project:API о сервиса Яндекс Самокат. </h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла        | Содержание файла                                    |
|-----------------------|-----------------------------------------------------|
| courier_metods.py     | Методы для тестов курьеров                          |
| order_metods.py       | методы для тестов по заказам                   
| tests dir             | Директория с тестами                                |
| test_accept_the_order | Тесты на принятие заказа курьером                   |
| test_create_courier.py | Тесты на создание курьера                           |
| test_create_order.py  | Тесты на создание заказа                            |
| test_delete_courier.py | Тесты на удаление курьера                           |
| test_get_order_by_number.py | Тесты на получение заказа по номеру                 |
| test_list_of_order.py | Тесты на получение списка заказов                   |
| test_login_courier.py | Тесты на авторизацию курьера                        |
| data.py               | Фаил с URL, эндепоинтами,данными для параметризации |
| generators.py         | Генераторы данных для тела запросов                 |
| confest.py            | Фикстура                                            |
| requirements.txt      | Файл с зависимостями                                |
| allure_results.dir    | Папка с отчетами Allure                             
