import allure

from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from urls import Urls


class TestPersonalAccount:
    @allure.title("Переход по клику на Личный кабинет")
    def test_go_to_personal_account(self, driver, user_data):
        main_page = MainPage(driver)
        main_page.click_and_go_to_lk()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login(user_data)

        main_page.main_page_loading_wait()
        main_page.click_and_go_to_lk()
        assert personal_account_page.wait_for_url(f"{Urls.MAIN_SITE}{Urls.PROFILE_URL}")

    @allure.title('Переход в раздел "История заказов"')
    def test_from_lk_to_the_constructor(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_and_go_to_lk()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_order_history_btn()

        current_url = personal_account_page.get_current_url()
        assert current_url == f"{Urls.MAIN_SITE}{Urls.ORDER_HISTORY_URL}"

    @allure.title("Выход из аккаунта")
    def test_get_out_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_and_go_to_lk()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_for_profile_page()
        personal_account_page.log_out_personal_account()

        assert personal_account_page.wait_for_url(f"{Urls.MAIN_SITE}{Urls.LOGIN}")
