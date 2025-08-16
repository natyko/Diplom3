from selenium.webdriver.common.by import By
#
#
# class BasePageLocators:
#     LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
#     CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
#     FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
#     PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
#
#
# class LoginPageLocators(BasePageLocators):
#     EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
#     PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
#     LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary')]")
#     FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(., 'Восстановить пароль')]")
#     REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
#     PASSWORD_VISIBILITY_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
#
#
# class RegisterPageLocators(BasePageLocators):
#     NAME_INPUT = (By.XPATH, "//input[@name='name']")
#     EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
#     PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
#     REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
#     LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
#     PASSWORD_VISIBILITY_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
#
#
# class PasswordRecoveryPageLocators(BasePageLocators):
#     EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
#     RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
#     LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
#     RESET_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
#     PASSWORD_VISIBILITY_ICON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
#
#
# class MainPageLocators(BasePageLocators):
#     BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
#     SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
#     FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
#     INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
#     INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
#     INGREDIENT_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
#     ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
#     ORDER_DETAILS = (By.XPATH, "//p[text()='идентификатор заказа']")
#     ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
#     BURGER_CONSTRUCTOR = (By.XPATH, "//ul[contains(@class, 'basket__list')]")
#
#
# class ProfilePageLocators(BasePageLocators):
#     ORDER_HISTORY_BUTTON = (By.CSS_SELECTOR, "a[href='/profile/orders']")
#     LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.logout")
#     NAME_INPUT = (By.XPATH, "//input[@name='name']")
#     EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
#     SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
#     CANCEL_BUTTON = (By.XPATH, "//button[text()='Отмена']")
#     ORDER_HISTORY_BLOCK = (By.CLASS_NAME, "OrderHistory_list")
#
#
# class FeedPageLocators(BasePageLocators):
#     ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//a")
#     ORDER_NUMBER_TEXT = (By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]")
#     TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
#     ORDERS_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
#     IN_PROGRESS_COLUMN = (By.XPATH, "//div[contains(text(), 'В работе')]/following-sibling::div")
#     DONE_COLUMN = (By.XPATH, "//div[contains(text(), 'Готовы')]/following-sibling::div")
#     FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")

class ForgetPasswordLocators:
    RESTORE_PASSWORD_BUTTON = By.XPATH, "//button[text()='Восстановить']"
    INPUT_EMAIL = By.XPATH, "//input[@name='name']"
    EYE_BUTTON = By.XPATH, '//div[@class="input__icon input__icon-action"]/*[name()="svg"]'
    ACTIVE_PASSWORD_FIELD = By.XPATH, '//div[contains(@class,"input_status_active")]'
    PASSWORD_FIELD = By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]'