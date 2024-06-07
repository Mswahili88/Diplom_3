import allure
from pages.main_functions_page import MainFunctions
from data import URL
from pages.order_list_page import OrderList
from pages.personal_account_page import PersonalAccount


class TestMainFunctions:

    @allure.title('Проверка перехода по кнопке "Конструктор"')
    @allure.description('Кликаем на кнопку "Личный кабинет" и далее переходим по кнопке "Конструктор"')
    def test_click_button_constructor(self, driver_both):
        test_main_functions_page = MainFunctions(driver_both)
        personal_account_page = PersonalAccount(driver_both)
        personal_account_page.click_button_personal_account()
        test_main_functions_page.click_button_constructor()
        assert test_main_functions_page.get_current_url() == URL.BASE_PAGE

    @allure.title('Проверка перехода по кнопке "Лента заказов"')
    @allure.description('Кликаем на кнопку "Лента заказов" и переходим на страницу с заказами')
    def test_click_button_order_list(self, driver_both):
        test_main_functions_page = MainFunctions(driver_both)
        test_order_list_page = OrderList(driver_both)
        test_order_list_page.click_order_list()
        assert test_main_functions_page.get_current_url() == URL.BASE_PAGE + URL.ORDER_LIST_PAGE

    @allure.title('Проверка появления всплывающего окна при клике на ингредиент')
    @allure.description('Кликаем на любой ингредиент и получаем всплывающее окно')
    def test_popup_window(self, driver_both):
        test_main_functions_page = MainFunctions(driver_both)
        test_main_functions_page.click_ingredient()
        name = test_main_functions_page.wait_and_find_header()
        assert name.is_displayed()

    @allure.title('Проверка закрытия модального окна')
    @allure.description('Кликаем на крестик чтобы закрыть модальное окно')
    def test_close_popup_window(self, driver_both):
        test_main_functions_page = MainFunctions(driver_both)
        test_main_functions_page.click_ingredient()
        test_main_functions_page.click_close_window()
        assert test_main_functions_page.cross_not_is_displayed()

    @allure.title('Проверка изменения счетчика заказа')
    @allure.description('Перетаскиваем ингредиент в корзину и проверяем изменения счетчика заказа')
    def test_put_ingredient_into_basket(self, driver_both):
        test_main_functions_page = MainFunctions(driver_both)
        test_main_functions_page.put_ingredient_into_basket()
        result_new = test_main_functions_page.counter_ingredient_text()
        assert result_new == '2'

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    @allure.description('Проверяем, что залогиненный пользователь может добавить в корзину ингредиент и оформить заказ')
    def test_make_order_confirmed(self, default_user, driver_both):
        email = default_user["email"]
        password = default_user["password"]
        test_main_functions_page = MainFunctions(driver_both)
        test_personal_account_page = PersonalAccount(driver_both)
        test_personal_account_page.click_button_personal_account()
        test_personal_account_page.set_email_input(email)
        test_personal_account_page.set_password_input(password)
        test_main_functions_page.finish_login_and_make_order()
        name = test_main_functions_page.wait_and_find_confirmation()
        assert name.is_displayed()
