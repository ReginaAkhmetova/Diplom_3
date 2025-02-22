import allure

from locators.all_locators import LoginPageLocators, RecoveryPasswordLocators
from pages.base_page import BasePage
from urls import Urls


class RecoveryPassword(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open_site_login(self):
        self.open_site(f"{Urls.MAIN_SITE}{Urls.LOGIN}")
        return self.wait_for_element_presence(LoginPageLocators.HL_LOGIN)

    @allure.step("Клик по ссылке Восстановить пароль")
    def click_recovery_link(self):
        return self.click_on_element(RecoveryPasswordLocators.FORGOT_PASSWORD)

    @allure.step("Клик по кнопке Восстановить")
    def click_recovery_btn(self):
        return self.click_on_element(RecoveryPasswordLocators.RESET_BUTTON)

    @allure.step("Ввести почту в поле восстановления пароля")
    def enter_more_email(self, email):
        self.find_and_click_element(LoginPageLocators.INPUT_EMAIL).send_keys(email)

    @allure.step("Клик по кнопке Показать/Скрыть пароль")
    def click_on_unhide_btn(self):
        return self.click_on_element(RecoveryPasswordLocators.UNHIDE_BTN)

    @allure.step("Найти активное поле Пароль")
    def find_active_input_password(self):
        return self.wait_for_visible(RecoveryPasswordLocators.INPUT_PASSWORD_ACTIV)

    @allure.step("Ввод нового пароля")
    def enter_new_password(self):
        return self.click_on_element(RecoveryPasswordLocators.INPUT_NEW_PASSWORD)
