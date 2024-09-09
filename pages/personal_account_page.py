from selenium.webdriver.common.by import By
from data import URL
from pages.base_page import BasePage
import allure


class PersonalAccount(BasePage):

    BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
    BUTTON_HISTORY_PROFILE = (By.XPATH, "//a[text()='История заказов']")
    BUTTON_SAVE = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_profile(self):
        self.click(self.BUTTON_HISTORY_PROFILE)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_button(self):
        self.click(self.EXIT_BUTTON)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_button_personal_account(self):
        self.click(self.BUTTON_ACCOUNT)

    @allure.step('Заполнения поля почты')
    def set_email_input(self, email):
        email_input = self.wait_and_find_element(self.INPUT_EMAIL)
        email_input.send_keys(email)

    @allure.step('Заполнение поля пароля')
    def set_password_input(self, password):
        email_input = self.wait_and_find_element(self.INPUT_PASSWORD)
        email_input.send_keys(password)

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self):
        self.click(self.BUTTON_ENTER)

    @allure.step('Ожидание смены страницы логина')
    def wait_for_url_changes_login(self):
        self.wait_url_changes(URL.BASE_PAGE + URL.LOGIN_PAGE)

    @allure.step('Ожидание смены главной страницы')
    def wait_for_url_changes_main(self):
        self.wait_url_changes(URL.BASE_PAGE)

    @allure.step('Ожидание смены страницы аккаунт')
    def wait_for_url_changes_account(self):
        self.wait_url_changes(URL.BASE_PAGE + URL.ACCOUNT_PROFILE_PAGE)

    @allure.step('Ожидание смены страницы аккаунт-профайл')
    def wait_for_url_changes_profile_account(self):
        self.wait_url_changes(URL.BASE_PAGE + URL.ACCOUNT_PROFILE_PAGE_FINAL)

    @allure.step('Вход в личный кабинет с ожиданием смены необходимых страниц')
    def click_enter_personal_account_wait_pages_changes(self):
        self.click_enter_button()
        self.wait_for_url_changes_login()
        self.click_button_personal_account()
        self.wait_for_url_changes_main()
        self.wait_for_url_changes_account()

    @allure.step('Поиск текста кнопки "Сохранить"')
    def save_button_present(self):
        return self.find_text(self.BUTTON_SAVE)







