from selenium.webdriver.common.by import By


class MainPageLocators:
    LK_PAGE = (By.XPATH, ".//p[text()='Личный Кабинет']")  # личный кабинет на главной странице
    MN_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, 'a[href="/account"]')  # личный кабинет
    LK_INFO = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__')]/parent::div")
    ORDER_LIST = (By.XPATH, "//p[text()='Лента Заказов']")
    MN_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    BUN_INGREDIEN = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    POPUP_INGREDIENT_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  # Счетчик
    INGREDIENT_COUNTER_VALUE = (
        By.XPATH,
        '//ul[1]/a[1]//p[contains(@class, "num") and text() = "{}"]',
    )  # Счетчик специфик
    BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')  # Идентификатор заказа
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    LOADING_CHECK_BOX = (By.XPATH, ".//img[@alt='tick animation']")
    HL_ORDER_STATUS = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')  # Ваш заказ начали готовить в попапе
    HL_ASSEMBLE_BURGER = (By.XPATH, ".//p[text()='Соберите бургер']")
    MODAL_BACKDROP_OPENED = (By.XPATH, "(//section[contains(@class,'Modal_modal_opened__')])")
    ORDER_MODAL_SPINNER = (By.XPATH, "(//div[contains(@class,'Modal_modal_opened__')])")
    ORDER_MODAL_NUMBER_INVALID = (
        By.XPATH,
        (
            "//h2[contains(@class, 'Modal_modal__title_shadow__')"
            " and contains(@class, 'text_type_digits-large')"
            " and text() = '9999']"
        ),
    )
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title_shadow__') and contains(@class, 'text_type_digits-large')]",
    )
    ORDER_PRICE_READY = (
        By.XPATH,
        (
            "//div[contains(@class, 'BurgerConstructor_basket__totalContainer__')]"
            "//p[contains(@class, 'text_type_digits') and text() != '0']"
        ),
    )


class LoginPageLocators:
    HL_LOGIN = (By.XPATH, ".//h2[text()='Вход']")  # заголовок Вход
    EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input[1]")  # Поле email
    PASSWORD = (By.NAME, "Пароль")  # Поле Пароль
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # кнопка Войти

    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')  # ссылка восстановить пароль
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода почты
    INPUT_PASSWORD_ACTIV = (By.CSS_SELECTOR, ".input.input_status_active")  # активное поле пароля
    HL_PS_RECOVERY = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # восстановление пароля
    INPUT_NEW_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")
    LINK_TO_ENTER = (By.CSS_SELECTOR, 'a[href="/login"]')  # ссылка Войти


class PersonalAccountPageLocators:
    MN_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")  # Конструктор
    LOG_OUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # кнопка Выход
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')  # кнопка "Сохранить"
    PROFILE_BUTTON = (By.LINK_TEXT, "Профиль")  # Кнопка "Профиль"
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, "История заказов")  # Кнопка "История заказов"


class OrderPageLocators:
    HL_ORDER_LIST = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок "Лента заказов"
    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'  # Состав
    ORDER_CARD = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__')])[2]")
    ORDER_LIST_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в Ленте заказов
    ORDERS_HISTORY = (
        By.XPATH,
        "//div[contains(@class, 'OrderHistory_textBox__')]/p[contains(@class, 'text_type_digits-default')]",
    )
    ORDERS_FEED = (
        By.XPATH,
        ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text text_type_digits-default']",
    )
    ORDER_NUM_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TOTAL_COUNTER_VALUE = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[text() = '{}']")
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_COUNTER_TODAY_VALUE = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[text() = '{}']")
    NUM_IN_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")  # Номер "В работе"
    NUM_IN_READY = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default')])[2]")  # номер "В готово"
    ORDER_IN_WORK_BY_NUM = (
        By.XPATH,
        (
            "//div[contains(@class, 'OrderFeed_orderStatusBox__')]"
            "//ul[contains(@class, 'OrderFeed_orderListReady__')]"
            "//li[contains(@class, 'text_type_digits-default') and text() = '{}']"
        ),
    )


class RecoveryPasswordLocators:
    RESET_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка восстановить
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')  # ссылка восстановить пароль
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода почты
    INPUT_PASSWORD_ACTIV = (By.CSS_SELECTOR, ".input.input_status_active")  # активное поле пароля
    HL_PS_RECOVERY = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # восстановление пароля
    INPUT_NEW_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")
    LINK_TO_ENTER = (By.CSS_SELECTOR, 'a[href="/login"]')  # ссылка Войти
    UNHIDE_BTN = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")  # кнопка показать пароль
