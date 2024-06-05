import allure
from pages.personal_account_page import PersonalAccount
from data import URL


class TestPersonalAccount:

    @allure.title('Вход в личный кабинет зарегистрированным пользователем')
    @allure.description('Создаем и регистрируем пользователя, логинимся им и входим в его личный кабинет')
    def test_enter_personal_account(self, default_user, driver_both):
        email = default_user["email"]
        password = default_user["password"]
        test_personal_account = PersonalAccount(driver_both)
        test_personal_account.click_button_personal_account()
        test_personal_account.set_email_input(email)
        test_personal_account.set_password_input(password)
        test_personal_account.click_enter_personal_account_wait_pages_changes()
        assert test_personal_account.save_button_present() == 'Сохранить'

    @allure.title('Вход в раздел "История заказов')
    @allure.description('Регистрируем пользователя, логинимся, входим в личный кабинет, открываем "Историю заказов"')
    def test_click_history_profile(self, default_user, driver_both):
        email = default_user["email"]
        password = default_user["password"]
        test_personal_account = PersonalAccount(driver_both)
        test_personal_account.click_button_personal_account()
        test_personal_account.set_email_input(email)
        test_personal_account.set_password_input(password)
        test_personal_account.click_enter_personal_account_wait_pages_changes()
        test_personal_account.click_history_profile()
        assert test_personal_account.get_current_url() == URL.HISTORY_ORDER_PAGE

    @allure.title('Выход из личного кабинета')
    @allure.description('Создаем, регистрируем пользователя, логинимся, входим в личный кабинет и выходим из него')
    def test_exit_account(self, default_user, driver_both):
        email = default_user["email"]
        password = default_user["password"]
        test_personal_account = PersonalAccount(driver_both)
        test_personal_account.click_button_personal_account()
        test_personal_account.set_email_input(email)
        test_personal_account.set_password_input(password)
        test_personal_account.click_enter_personal_account_wait_pages_changes()
        test_personal_account.click_exit_button()
        test_personal_account.wait_for_url_changes_profile_account()
        assert test_personal_account.get_current_url() == URL.LOGIN_PAGE




