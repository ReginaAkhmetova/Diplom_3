import allure

from locators.all_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    @allure.step("Открыть сайт")
    def open_main_site(self):
        return self.open_site(Urls.MAIN_SITE)

    @allure.step("Дождаться загрузки страницы")
    def main_page_loading_wait(self):
        return self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Переход в личный кабинет")
    def click_and_go_to_lk(self):
        return self.click_on_element(MainPageLocators.MN_PERSONAL_ACCOUNT)

    @allure.step("Переход на страницу Лента заказов")
    def click_and_go_to_order_list(self):
        return self.click_on_element(MainPageLocators.ORDER_LIST)

    @allure.step("Переход по клику в конструктор")
    def open_constructor(self):
        self.click_on_element(MainPageLocators.MN_CONSTRUCTOR)
        return self.wait_for_visible(MainPageLocators.MN_CONSTRUCTOR)

    @allure.step("Кликнуть по инредиенту")
    def click_ingredient(self):
        self.wait_for_clickable(MainPageLocators.BUN_INGREDIEN)
        return self.click_on_element(MainPageLocators.BUN_INGREDIEN)

    @allure.step('Появление поп-апа "Детали ингредиента"')
    def popup_with_ingredient_details(self):
        self.wait_for_visible(MainPageLocators.POPUP_INGREDIENT_DETAILS)
        return self.get_text_element(MainPageLocators.POPUP_INGREDIENT_DETAILS)

    @allure.step("Закрываем поп-ап кликом на крестик")
    def close_popup(self):
        return self.click_overlapped(MainPageLocators.CLOSE_BUTTON)

    @allure.step("Ждем пока появится поп-ап заказа")
    def wait_for_order_popup(self):
        return self.wait_for_element_presence(MainPageLocators.HL_ORDER_STATUS)

    @allure.step("Ждем модального бекстейджа (спиннера) попапа заказа")
    def wait_for_order_spinning(self):
        return self.wait_for_element_presence(MainPageLocators.ORDER_MODAL_SPINNER)

    @allure.step("Ждем скрытия бекстейджа (спиннера) попапа заказа")
    def wait_for_order_spinning_hide(self):
        return self.wait_for_element_hide(MainPageLocators.ORDER_MODAL_SPINNER)

    @allure.step("Проверить что поп-ап с заказом невидим")
    def wait_order_popup_is_invisible(self):
        return self.wait_invisibility_element(MainPageLocators.HL_ORDER_STATUS)

    @allure.step("Проверить что поп-ап с деталями ингридиента невидим")
    def wait_ingredient_popup_is_invisible(self):
        return self.wait_invisibility_element(MainPageLocators.POPUP_INGREDIENT_DETAILS)

    @allure.step("Получить количество ингредиентов из счётчика")
    def get_count_ingredient(self):
        self.wait_for_element_presence(MainPageLocators.INGREDIENT_COUNTER)
        counter_element = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
        return counter_element.text

    @allure.step("Ожидаем, пока количество ингридиентов в счётчике станет равным ожидаемому")
    def wait_count_ingredient(self, count):
        by, loc = MainPageLocators.INGREDIENT_COUNTER_VALUE
        loc = loc.format(count)
        locator = by, loc
        self.wait_for_element_presence(locator)
        counter_element = self.find_element(locator)
        return counter_element.text

    @allure.step("Найти и кликнуть кнопку Оформить заказ")
    def find_and_click_order_btn(self):
        return self.find_and_click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Перетащить булку в корзину")
    def drag_and_drop_bun(self):
        self.wait_for_clickable(MainPageLocators.BUN_INGREDIEN)
        self.drag_and_drop_element(MainPageLocators.BUN_INGREDIEN, MainPageLocators.BASKET)
        return self.wait_for_element_presence(MainPageLocators.ORDER_PRICE_READY)

    @allure.step("Ждем пока глобальный бекдроп перестанет быть открытым")
    def wait_backdrop_hide(self):
        return self.wait_for_element_hide(MainPageLocators.MODAL_BACKDROP_OPENED)

    @allure.step("Заказываем, ждем окно заказа и закрываем его")
    def order(self):
        self.find_and_click_order_btn()
        self.wait_for_order_popup()
        self.wait_for_element_presence(MainPageLocators.ORDER_MODAL_NUMBER_INVALID)
        self.wait_for_order_spinning()
        self.wait_for_element_hide(MainPageLocators.ORDER_MODAL_NUMBER_INVALID)
        self.wait_for_order_spinning_hide()
        self.wait_for_element_presence(MainPageLocators.ORDER_MODAL_NUMBER)
        order_number = self.get_text_element(MainPageLocators.ORDER_MODAL_NUMBER)
        self.wait_for_order_spinning_hide()
        self.close_popup()
        self.wait_order_popup_is_invisible()
        self.wait_backdrop_hide()
        return order_number
