import allure

from selenium import webdriver
from seletools.actions import drag_and_drop
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.all_locators import (
    MainPageLocators,
    PersonalAccountPageLocators,
    LoginPageLocators,
    OrderPageLocators,
    RecoveryPasswordLocators,
)
from data import Settings


class StellarBurgersTestcase:
    main_page = MainPageLocators()
    login_page = LoginPageLocators()
    order_page = OrderPageLocators()
    account_page = PersonalAccountPageLocators()
    recovery_password = RecoveryPasswordLocators()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def open_site(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Найти и кликнуть по элементу")
    def find_and_click_element(self, locator):
        self.wait_for_element_presence(locator)
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        return element

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=Settings.global_timeout):
        element = self.wait_for_visible(locator, timeout)
        # Есть некоторые отличия в работе Chrome и Firefox, поэтому мы в этом месте для
        # Chrome используем метод click() элемента, а для Firefox нам на этом сайте чаще
        # приходится использовать ActionChains и нажимать на элемент таким образом, чтобы
        # исключать ошибку проверки перекрытия другим слоем, стоящим выше по оси Z (zIndex)
        if isinstance(self.driver, webdriver.Chrome):
            element.click()
        elif isinstance(self.driver, webdriver.Firefox):
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
        else:
            raise RuntimeError("unsupported webdriver")
        return element

    @allure.step("Подождать пока элемент не станет невидимым")
    def wait_for_element_hide(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Подождать пока элемент станет видимым")
    def wait_for_visible(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=Settings.global_timeout):
        element = self.wait_for_visible(locator, timeout)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Подождать пока элемен станет кликабельным")
    def wait_for_clickable(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Подождать загрузки сраницы")
    def wait_for_url(self, url, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step("Подождать появления элемента")
    def wait_for_element_presence(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Подождать пока элемент станет видимым и кликабельным")
    def wait_for_element_clickable(self, locator, time=Settings.global_timeout):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step("Получить текст элемента")
    def get_text_element(self, locator, timeout=Settings.global_timeout):
        element = self.wait_for_visible(locator, timeout)
        return element.text

    @allure.step("Подождать невидимости элемента")
    def wait_invisibility_element(self, locator, timeout=Settings.global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, sourse, target):
        source_element = self.driver.find_element(*sourse)
        target_element = self.driver.find_element(*target)
        drag_and_drop(self.driver, source_element, target_element)

    @allure.step("Кликаем на элемент, перекрытый другим элементом выше по zIndex")
    def click_overlapped(self, locator):
        element = self.wait_for_element_presence(locator)
        return self.driver.execute_script("arguments[0].click();", element)
