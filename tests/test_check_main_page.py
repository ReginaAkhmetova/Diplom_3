import allure

from locators.all_locators import MainPageLocators
from pages.main_page import MainPage
from urls import Urls


class TestCheckMainPage:
    @allure.title('проверка перехода по клику на "Лента заказов"')
    def test_click_on_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_site()
        main_page.click_and_go_to_order_list()
        assert main_page.wait_for_url(f"{Urls.MAIN_SITE}{Urls.ORDER_LIST_URL}")

    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_click_on_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_site()
        main_page.click_and_go_to_order_list()
        main_page.open_constructor()
        assert main_page.wait_for_url(f"{Urls.MAIN_SITE}/")

    @allure.title("Проверка что если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_chek_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_site()
        main_page.click_ingredient()
        text = main_page.popup_with_ingredient_details()
        assert text == "Детали ингредиента"

    @allure.title("Проверка что всплывающее окно закрывается кликом по крестику")
    def test_check_ingredient_popup_close(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_site()
        main_page.click_ingredient()
        main_page.popup_with_ingredient_details()
        main_page.close_popup()
        assert main_page.wait_ingredient_popup_is_invisible()

    @allure.title("Проверка что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_change_counter_when_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_site()
        count = main_page.get_count_ingredient()
        main_page.drag_and_drop_bun()
        new_count = main_page.wait_count_ingredient("2")
        assert count == "0" and new_count == "2"

    @allure.title("Проверка что залогиненный пользователь может оформить заказ")
    def test_create_order_wiht_authorized_user(self, driver, login):
        main_page = MainPage(driver)
        main_page.drag_and_drop_bun()
        main_page.find_and_click_order_btn()
        assert main_page.get_text_element(MainPageLocators.HL_ORDER_STATUS) == "Ваш заказ начали готовить"
