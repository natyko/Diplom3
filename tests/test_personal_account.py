import allure

from pages.personal_account_page import PersonalAccountPage

from tests.conftest import driver_signed_in


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.description("Переход по клику на «Личный кабинет»")
    def test_profile_is_opened_success(self, driver_signed_in):
        profile_button = PersonalAccountPage(driver_signed_in)
        profile_button.click_on_personal_account_button()
        profile_button.wait_for_log_out_button()
        assert profile_button.in_personal_account_page()

    @allure.description("Переход в раздел «История заказов")
    def test_order_history_is_displayed(self, driver_signed_in):
        order_history = PersonalAccountPage(driver_signed_in)
        order_history.click_on_personal_account_button()
        order_history.wait_for_log_out_button()
        order_history.click_on_order_history_button()
        order_history.wait_for_order_history_is_displayed()
        assert order_history.order_history_is_displayed()

    @allure.description("Выход из аккаунта")
    def test_log_out(self, driver_signed_in):
        log_out = PersonalAccountPage(driver_signed_in)
        log_out.click_on_personal_account_button()
        log_out.wait_for_log_out_button()
        log_out.click_log_out_button()
        log_out.wait_for_log_in_button_is_displayed()
        assert log_out.login_button_is_displayed()