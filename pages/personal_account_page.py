import allure

from data import UserData
from locators.all_locators import PersonalAccountPageLocators, LoginPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step("Ждем пока страница пользователя откроется")
    def wait_for_profile_page(self):
        self.wait_for_element_presence(PersonalAccountPageLocators.LOG_OUT_BUTTON)

    @allure.step("Вести в поле email почту")
    def enter_email(self, email=UserData.EMAIL):
        self.find_and_click_element(LoginPageLocators.EMAIL).send_keys(email)

    @allure.step("Ввести в поле пароль пароль")
    def enter_password(self, password=UserData.PASSWORD):
        self.find_and_click_element(LoginPageLocators.PASSWORD).send_keys(password)

    @allure.step("Авторизация")
    def login(self, data):
        email, password, name = data
        self.wait_for_element_presence(LoginPageLocators.HL_LOGIN)
        self.enter_email(email)
        self.enter_password(password)
        self.find_and_click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Переход на страницу пользователя")
    def go_to_personal_account(self):
        self.wait_for_visible(PersonalAccountPageLocators.PROFILE_BUTTON).click()
        return self.get_current_url()

    @allure.step("Клик по кнопке Выход из аккаунта")
    def log_out_personal_account(self):
        self.click_on_element(PersonalAccountPageLocators.LOG_OUT_BUTTON)

    @allure.step("Кликнуть по кнопке История заказов")
    def click_order_history_btn(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Найти кнопку Сохранить")
    def find_save_btn(self):
        self.wait_for_visible(PersonalAccountPageLocators.SAVE_BUTTON)
