# from .base_page import BasePage
# from locators.forgetPasswordLocators import PasswordRecoveryPageLocators
#
# class PasswordRecoveryPage(BasePage):
#     def submit_recovery_email(self, email):
#         self.send_keys_to_element(PasswordRecoveryPageLocators.EMAIL_INPUT_RECOVERY, email)
#         self.click_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)
#
#     def is_recovery_form_displayed(self):
#         return self.is_element_visible(PasswordRecoveryPageLocators.EMAIL_INPUT_RECOVERY) and \
#                self.is_element_visible(PasswordRecoveryPageLocators.RECOVER_BUTTON)

import allure
from locators.forget_password_locators import ForgetPasswordLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class RestorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_locators = LoginPageLocators()
        self.restore_page_locators = ForgetPasswordLocators()

    @allure.step("Клик по ссылке восстановления пароля на странице авторизациии")
    def click_on_restore_link(self):
        self.click_on_element(self.login_locators.FORGET_PASSWORD_LINK)

    @allure.step("Отображается кнопка Восстановить пароль")
    def restore_button_is_visible(self):
        self.wait()
        return self.visibility_of_element(self.restore_page_locators.RESTORE_PASSWORD_BUTTON)

    @allure.step("Заполнить поле почты")
    def fill_email_field(self):
        self.fill_input(self.restore_page_locators.INPUT_EMAIL, "ivanova_18@gmail.com")

    @allure.step("Клик на кнопку восстановления пароля")
    def click_on_restore_button(self):
        self.click_on_element(self.restore_page_locators.RESTORE_PASSWORD_BUTTON)

    @allure.step("Кнопка выключения видимости пароля видна")
    def eye_button_is_visible(self):
        return self.visibility_of_element(self.restore_page_locators.EYE_BUTTON)

    @allure.step("Подождать видимость кнопки выклчения видимости пароля")
    def wait_visibility_of_eye_button(self):
        self.wait_visibility_of_element(self.restore_page_locators.EYE_BUTTON)

    @allure.step("Кликнуть на поле ввода пароля")
    def click_password_field(self):
        self.click_on_element(self.restore_page_locators.PASSWORD_FIELD)

    @allure.step("Поле ввода пароля активно")
    def field_is_active(self):
        return self.visibility_of_element(self.restore_page_locators.ACTIVE_PASSWORD_FIELD)