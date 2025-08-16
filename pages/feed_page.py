from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_page_locators = MainPageLocators()

    @allure.step("Кликнуть на кнопку Лента заказов")
    def click_on_feed(self):
        self.click_on_element(self.main_page_locators.ORDER_FEED_LINK)

    @allure.step("Кликнуть на первый заказ в ленте заказов")
    def click_on_first_order(self):
        self.click_on_element(self.main_page_locators.FIRST_ORDER_IN_FEED)

    @allure.step("Отображается номер заказа")
    def order_info_is_displayed(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_INFO)

    @allure.step("Ожидание появления ленты заказов")
    def wait_for_order_feed(self):
        self.wait_visibility_of_element(self.main_page_locators.FIRST_ORDER_IN_FEED)

    @allure.step("Скролл до заказа")
    def scroll_to_order(self):
        self.scroll_to_element(self.main_page_locators.MY_ORDER_IN_ORDER_FEED)

    @allure.step("Заказ отображается")
    def my_order_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.MY_ORDER_IN_ORDER_FEED)

    @allure.step("Количество заказов за все время")
    def orders_for_all_time_(self):
        return self.text_of_element(self.main_page_locators.ORDERS_FOR_ALL_TIME)

    @allure.step("Клоличество заказов за сегодня")
    def orders_for_today(self):
        return self.text_of_element(self.main_page_locators.ORDERS_FOR_TODAY)

    @allure.step("Переместить ингредиент в корзину")
    def drag_and_drop_bun(self):
        self.move_element(self.main_page_locators.CRATER_BUN,
                          self.main_page_locators.BURGER_INGREDIENTS)

    @allure.step("Кликнуть на кнопку Оформить заказ")
    def make_order(self):
        self.click_on_element(self.main_page_locators.BUTTON_MAKE_ORDER)

    @allure.step("Закрыть модальное окно с номером заказа")
    def close_modal_window(self):
        self.click_on_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step("Кликнуть на кнопку Конструктор на главной странице")
    def click_on_constructor(self):
        self.click_on_element(self.main_page_locators.CONSTRUCTOR_LINK)

    @allure.step("Ожидание закрытия модального окна")
    def wait_for_modal_window_to_be_closed(self):
        self.wait_order_modal_window_closed(self.main_page_locators.EXTRA_ORDER_MODAL_WINDOW)

    @allure.step("Получить номер заказа в работе на ленте заказов")
    def get_order_in_feed(self):
        return self.text_of_element(self.main_page_locators.ORDER_IN_PROCESS_IN_FEED)

    @allure.step("Получить номер только что оформленного заказа")
    def get_order_in_main_page(self):
        return self.text_of_element(self.main_page_locators.ORDER_IN_MODAL_WINDOW)

    @allure.step("Ожидание видимости номера заказа")
    def wait_for_order_number(self):
        return self.wait_visibility_of_element(self.main_page_locators.ORDER_IN_PROCESS_IN_FEED)


