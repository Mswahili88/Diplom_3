import pytest
import allure
import helper
import requests
from selenium import webdriver
from data import URL


@allure.step('Запуск драйвера сразу для двух браузеров - "Firefox" и "Chrome"')
@pytest.fixture(params=['firefox', 'chrome'])
def driver_both(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    driver.get(URL.BASE_PAGE)

    yield driver
    driver.quit()


@allure.step('Создание уникального пользователя и его регистрация с последующим удалением данных')
@pytest.fixture(scope='function')
def default_user():
    payload = helper.TestMethodsHelper.create_random_login_password()
    response = requests.post(URL.API_URL_BASE + URL.API_URL_REG_USER, data=payload)
    yield payload
    token = response.json()["accessToken"]
    requests.delete(URL.API_URL_BASE + URL.API_URL_DELETE_USER, data=payload, headers={"Authorization": token})

