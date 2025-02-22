class Urls:
    MAIN_SITE = "https://stellarburgers.nomoreparties.site"
    LOGIN = "/login"
    ORDER_HISTORY_URL = "/account/order-history"
    ORDER_LIST_URL = "/feed"
    PROFILE_URL = "/account/profile"  # ссылка на личный кабинет

    FORGOT_PASSWORD_URL = "/forgot-password"  # ссылка на страницу ввода email для восстановления пароля
    RESET_PASSWORD_URL = "/reset-password"  # ссылка на страницу ввода нового пароля и кода из письма

    BASE_API = "https://stellarburgers.nomoreparties.site"
    CREATE_USER = "/api/auth/register"  # POST создание пользователя
    DELETE_USER = "/api/auth/user"  # DELETE удаление пользователя
