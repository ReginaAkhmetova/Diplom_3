## Дипломный проект. Задание 3: UI-тесты
<hr>

## <h> Project: Stellar Burgers UI</h>

## <h> Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h.

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


## <h3> Project files and description:</h3>
| Название                  | Содержание файла                                |
|---------------------------|-------------------------------------------------|
| Locators dir              | Директория с локаторами                         |
| Pages dir                 | Директория с методами                           |
| base_page.py              | Методы для общих элементов                      |
| main_page.py              | Методы для  главной страницы                    |
| order_list_page.py        | Методы для раздела "Лента заказов"              |
| personal_account_page.py  | Методы для личного кабинета                     |
| recovery_password.py      | Методы для раздела восстановления пароля        |
| Tests dir                 | Директория с тестами                            |
| test_check_main_page.py   | Тесты на проверку основного функционала         |
| test_order_feed.py        | Тесты на проверку раздела "Лента заказов"       |
| test_personal_account.py  | Тесты на проверку личного кабинета              |
| test_recovery_password.py | Тесты на проверку раздела восстановления пароля |
| conftest.py               | Файл с фикстурами                               |
| helpers.py                | Генератор данных пользователя                   |
| data.py                   | Файл с данными пользователя                     |
| urls.py                   | Файл с Url и эндпоинтами                        |
| requirements.txt          | Файл с зависимостями                            |
| allure_results.dir        | Файл с отчетами Allure                          |
