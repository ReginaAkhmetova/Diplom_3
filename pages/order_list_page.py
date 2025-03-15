import allure

from locators.all_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):
    @allure.step('Ждем открытия страницы "Лента заказов"')
    def wait_for_page_loaded(self):
        return self.wait_for_element_presence(OrderPageLocators.HL_ORDER_LIST)

    @allure.step("Получить номер заказа")
    def get_order_nums(self):
        self.wait_for_element_presence(OrderPageLocators.ORDER_NUM_IN_HISTORY)
        elements = self.find_elements(OrderPageLocators.ORDER_NUM_IN_HISTORY)
        return [element.text for element in elements]

    @allure.step('Получить номер заказа "В работе" в ленте заказов')
    def get_order_num_in_work(self):
        num = self.wait_for_element_presence(OrderPageLocators.NUM_IN_WORK)
        return int(num.text)

    @allure.step('Получить значение счетчика "Выполнено за сегодня"')
    def get_num_orders_today(self):
        number = self.wait_for_element_presence(OrderPageLocators.ORDER_COUNTER_TODAY)
        return int(number.text)

    @allure.step('Ожидаем значение счетчика "Выполнено за сегодня" отличное от старого')
    def wait_num_orders_today_differ(self, value):
        self.wait_for_element_presence(OrderPageLocators.ORDER_COUNTER_TODAY)
        by, loc = OrderPageLocators.ORDER_COUNTER_TODAY_VALUE
        loc = loc.format(value)
        locator = by, loc
        self.wait_for_element_hide(locator)
        element = self.find_element(OrderPageLocators.ORDER_COUNTER_TODAY)
        return int(element.text)

    @allure.step("Проверка идентификатора заказа в ленте заказов")
    def find_order_nums_in_orders(self, order_nums):
        self.wait_for_element_presence(OrderPageLocators.ORDERS_HISTORY)
        elements = self.find_elements(OrderPageLocators.ORDERS_HISTORY)
        order_nums_in_orders_list = [element.text for element in elements]
        return all(order_num in order_nums_in_orders_list for order_num in order_nums)

    @allure.step("Открыть карточку заказа кликом по ней")
    def click_and_open_order_card(self):
        self.wait_for_visible(OrderPageLocators.ORDER_CARD).click()

    @allure.step("Получение количества заказов")
    def get_all_orders_counter(self):
        return self.get_text_element(OrderPageLocators.TOTAL_COUNTER)

    @allure.step("Ждем количества заказов не равное старому значению")
    def wait_all_orders_counter_differ(self, value):
        self.wait_for_element_presence(OrderPageLocators.TOTAL_COUNTER)
        by, loc = OrderPageLocators.TOTAL_COUNTER_VALUE
        loc = loc.format(value)
        locator = by, loc
        self.wait_for_element_hide(locator)
        return self.get_text_element(OrderPageLocators.TOTAL_COUNTER)

    @allure.step('Появление поп-апа c составом заказа"')
    def popup_with_order_structure(self):
        self.wait_for_visible(OrderPageLocators.ORDER_STRUCTURE)
        return self.get_text_element(OrderPageLocators.ORDER_STRUCTURE)

    @allure.step("Подождать появления состава")
    def get_presence_structure(self):
        return self.wait_for_element_presence(OrderPageLocators.ORDER_STRUCTURE)

    @allure.step('Ожидание появления заказа в "В работе"')
    def wait_for_order_in_work(self, order_num):
        by, loc = OrderPageLocators.ORDER_IN_WORK_BY_NUM
        loc = loc.format(order_num.lstrip("0"))
        locator = (by, loc)
        return self.wait_for_element_presence(locator)
