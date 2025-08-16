# import pytest
# import os
# from dotenv import load_dotenv
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from api.user_api import UserAPI
# from pages.main_page import MainPage
#
# load_dotenv()
#
# BASE_URL = os.getenv("BASE_URL", "https://stellarburgers.nomoreparties.site")
# LOGIN_URL = f"{BASE_URL}/login"
#
#
# def _initialize_browser(browser_name, headless):
#     """Initialize the browser based on the given name and headless mode."""
#     if browser_name == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--window-size=1920,1080")
#         if headless:
#             options.add_argument("--headless")
#         return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#     elif browser_name == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--width=1920")
#         options.add_argument("--height=1080")
#         if headless:
#             options.add_argument("--headless")
#         return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")
#
#
# @pytest.fixture(scope="function")
# def driver(request):
#     """Fixture to initialize and quit the browser."""
#     browser = request.config.getoption("--browser", default="chrome").lower()
#     headless = os.getenv("HEADLESS", "false").lower() == "true"
#     drv = _initialize_browser(browser, headless)
#     drv.implicitly_wait(10)
#     yield drv
#     drv.quit()
#
#
# @pytest.fixture(scope="function")
# def registered_user():
#     """Fixture to create and clean up a registered user."""
#     api = UserAPI()
#     user = api.generate_test_user()
#     response = api.register_user(user)
#     assert response.status_code == 200, f"Failed to register: {response.text}"
#     yield user
#     api.login_user(user)
#     api.delete_user()
#
#
# @pytest.fixture(scope="function")
# def logged_in_user(driver, registered_user):
#     """Fixture to log in a user and return the user data."""
#     login_page = LoginPage(driver, LOGIN_URL)
#     login_page.open()
#     login_page.login(registered_user["email"], registered_user["password"])
#     api = UserAPI()
#     token_response = api.login_user(registered_user)
#     assert token_response.status_code == 200, "Failed to retrieve token"
#     registered_user["token"] = token_response.json().get("accessToken")
#     return registered_user
#
#
# @pytest.fixture(scope="function")
# def create_order(driver, logged_in_user):
#     """Fixture to create an order and return the order number."""
#     main_page = MainPage(driver, BASE_URL)
#     main_page.open()
#     assert main_page.is_element_present(main_page.locators.BURGER_CONSTRUCTOR, timeout=10), \
#         "Burger constructor is not visible"
#     main_page.add_ingredient_to_burger()
#     main_page.click_place_order_button()
#     order_number = main_page.get_order_number()
#     assert order_number, "Order number must be retrieved"
#     return order_number.replace("#", "").strip()


import pytest
from selenium import webdriver
from data import Data
from locators.login_page_locators import LoginPageLocators


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None

    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()

    driver.get(Data.BURGERS_URL_LOGIN)

    yield driver
    driver.execute_script('window.localStorage.clear();')

    driver.quit()


@pytest.fixture(params=['chrome', 'firefox'])
def driver_signed_in(request):
    driver = None

    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()

    driver.get(Data.BURGERS_URL_LOGIN)
    driver.find_element(*LoginPageLocators.INPUT_EMAIL_AUTH).send_keys("ivanova_18@gmail.com")
    driver.find_element(*LoginPageLocators.INPUT_PASSWORD_AUTH).send_keys("dddddd")
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()

    yield driver
    driver.execute_script('window.localStorage.clear();')

    driver.quit()