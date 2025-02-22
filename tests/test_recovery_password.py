import allure

from pages.recovery_password_page import RecoveryPassword
from urls import Urls
from data import UserData


class TestRecoveryPassword:
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль» ")
    def test_go_to_the_btn_to_recovery_password(self, driver):
        recovery_password = RecoveryPassword(driver)
        recovery_password.open_site_login()
        recovery_password.click_recovery_link()

        assert recovery_password.wait_for_url(f"{Urls.MAIN_SITE}{Urls.FORGOT_PASSWORD_URL}")

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    def test_input_password_and_click_btn_recovery(self, driver):
        recovery_password = RecoveryPassword(driver)
        recovery_password.open_site_login()
        recovery_password.click_recovery_link()
        recovery_password.enter_more_email(UserData.EMAIL)
        recovery_password.click_recovery_btn()

        assert recovery_password.wait_for_url(f"{Urls.MAIN_SITE}{Urls.RESET_PASSWORD_URL}")

    @allure.title("Проверка что клик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_on_unhide_btn(self, driver):
        recovery_password = RecoveryPassword(driver)
        recovery_password.open_site_login()
        recovery_password.click_recovery_link()
        recovery_password.enter_more_email(UserData.EMAIL)
        recovery_password.click_recovery_btn()
        recovery_password.click_on_unhide_btn()
        assert recovery_password.find_active_input_password()
