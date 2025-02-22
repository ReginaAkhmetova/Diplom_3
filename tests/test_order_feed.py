import allure

from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderListPage:
    @allure.title("Проверка что если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_and_go_to_order_list()
        order_list_page = OrderListPage(driver)
        order_list_page.click_and_open_order_card()
        assert order_list_page.get_presence_structure()

    @allure.title('Проверка что заказы из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_order_history_is_in_order_list(self, driver, login):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        main_page.drag_and_drop_bun()
        main_page.order()

        main_page.click_and_go_to_lk()
        personal_account_page.wait_for_profile_page()
        personal_account_page.click_order_history_btn()
        order_nums = order_list_page.get_order_nums()

        main_page.click_and_go_to_order_list()
        assert order_list_page.find_order_nums_in_orders(order_nums)

    @allure.title('Проверка что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_when_create_order_counter_increases_for_all_time(self, driver, login):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_and_go_to_order_list()
        order_list_page.wait_for_page_loaded()
        order_counter = order_list_page.get_all_orders_counter()

        main_page.open_constructor()
        main_page.drag_and_drop_bun()
        main_page.order()

        main_page.click_and_go_to_order_list()
        order_list_page.wait_for_page_loaded()
        order_counter2 = order_list_page.wait_all_orders_counter_differ(order_counter)

        assert int(order_counter) < int(order_counter2)

    @allure.title('Проверка что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_when_create_order_today_counter_increases(self, driver, login):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_and_go_to_order_list()
        order_list_page.wait_for_page_loaded()
        order_counter = order_list_page.get_num_orders_today()

        main_page.open_constructor()
        main_page.drag_and_drop_bun()
        main_page.order()
        main_page.click_and_go_to_order_list()
        order_list_page.wait_for_page_loaded()
        order_counter2 = order_list_page.wait_num_orders_today_differ(order_counter)

        assert order_counter < order_counter2

    @allure.title("Проверка что после оформления заказа его номер появляется в разделе В работе")
    def test_order_listed_in_work(self, driver, login):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        main_page.drag_and_drop_bun()
        order_number = main_page.order()
        main_page.click_and_go_to_order_list()
        order_list_page.wait_for_page_loaded()
        assert order_list_page.wait_for_order_in_work(order_number)
