from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from seletools.actions import drag_and_drop


class MainFunctions(BasePage):
    BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    BUTTON_ORDER_LIST = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']/div/p[@class='counter_counter__num__3nue1']")
    POPUP_WINDOW_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    ORDER_BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    CONFIRMATION_TEXT = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")

    @allure.step('Клик по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.click(self.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_button_order_list(self):
        self.click(self.BUTTON_ORDER_LIST)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_button_account(self):
        self.click(self.BUTTON_ACCOUNT)

    @allure.step('Клик по ингредиенту"')
    def click_ingredient(self):
        self.click(self.INGREDIENT)

    @allure.step('Ищем заголовок всплывающего окна')
    def wait_and_find_header(self):
        name = self.wait_and_find_element(self.POPUP_WINDOW_HEADER)
        return name

    @allure.step('Кликаем по крестику, чтобы закрыть всплывающее окно')
    def click_close_window(self):
        self.click(self.CLOSE_BUTTON)

    @allure.step('Находим невидимый крестик для закрытия окна')
    def cross_not_is_displayed(self):
        name = self.wait_and_find_element_invisible(self.CLOSE_BUTTON)
        return not name.is_displayed()

    @allure.step('Перетаскиваем ингредиент в корзину покупателя')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_and_find_element(self.INGREDIENT)
        basket = self.wait_and_find_element(self.ORDER_BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Ищем текст по локатору ингредиента')
    def counter_ingredient_text(self):
        return self.find_text(self.INGREDIENT)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_make_order(self):
        self.click(self.BUTTON_MAKE_ORDER)

    @allure.step('Ищем текст о подтверждении заказа')
    def wait_and_find_confirmation(self):
        name = self.wait_and_find_element(self.CONFIRMATION_TEXT)
        return name

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

    @allure.step('Завершить логин пользователя и оформит заказ')
    def finish_login_and_make_order(self):
        self.click_enter_button()
        self.put_ingredient_into_basket()
        self.click_make_order()
