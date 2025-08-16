# # from .base_page import BasePage
# # from locators.forgetPasswordLocators import MainPageLocators
# #
# # class MainPage(BasePage):
# #     def __init__(self, driver, base_url):
# #         super().__init__(driver, base_url)
# #         self.locators = MainPageLocators
# #
# #     def add_ingredient_to_burger(self):
# #         self.drag_and_drop(self.locators.INGREDIENT, self.locators.BASKET_LIST)
# #
# #     def click_place_order_button(self):
# #         self.click_element(self.locators.PLACE_ORDER_BUTTON)
# #
# #     def get_order_number(self):
# #         return self.find_element(self.locators.ORDER_NUMBER).text.strip()
# #
# #     def click_profile_button(self):
# #         self.click_element(self.locators.PROFILE_BUTTON)
# #
# #     def is_constructor_visible(self):
# #         return self.is_element_visible(self.locators.BUNS_TAB)
#
# from locators.main_page_locators import MainPageLocators
# from pages.base_page import BasePage
# import allure
#
#
# class MainPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.main_page_locators = MainPageLocators()
#
#     @allure.step("Кликнуть на кнопку Конструктор")
#     def click_in_constructor(self):
#         self.click_on_element(self.main_page_locators.CONSTRUCTOR_LINK)
#
#     @allure.step("Булочка видна")
#     def buns_link_is_visible(self):
#         return self.visibility_of_element(self.main_page_locators.BUNS_LINK)
#
#     @allure.step("Кликнуть на ленту заказов")
#     def click_in_order_feed(self):
#         self.click_on_element(self.main_page_locators.ORDER_FEED_LINK)
#
#     @allure.step("Заголовок Лента заказов виден")
#     def order_feed_header_is_visible(self):
#         return self.visibility_of_element(self.main_page_locators.ORDER_FEED_HEADER)
#
#     @allure.step("Ожидание заголовка Ленты заказов")
#     def wait_for_order_feed_header(self):
#         self.wait_visibility_of_element(self.main_page_locators.ORDER_FEED_HEADER)
#
#     @allure.step("Кликнуть на булку")
#     def click_on_crater_bun(self):
#         self.click_on_element(self.main_page_locators.CRATER_BUN)
#
#     @allure.step("Закрыть модально окно с номером заказа")
#     def close_modal_window(self):
#         self.click_on_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)
#
#     @allure.step("Ожидание появления элемента закрытия окна")
#     def wait_for_modal_window(self):
#         self.wait_visibility_of_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)
#
#     @allure.step("Ожидание повления элемента булочки")
#     def wait_for_bun(self):
#         self.wait_visibility_of_element(self.main_page_locators.CRATER_BUN)
#
#     @allure.step("Кнопка закрытия модального окна видна")
#     def close_modal_window_button_is_visible(self):
#         return self.visibility_of_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)
#
#     @allure.step("Перемещение булочки в корзину")
#     def drag_and_drop_bun(self):
#         self.move_element(self.main_page_locators.CRATER_BUN,
#                           self.main_page_locators.BURGER_INGREDIENTS)
#
#     @allure.step("Количество булочек")
#     def bun_counter_is_visible(self):
#         return self.visibility_of_element(self.main_page_locators.BUN_COUNTER)
#
#     @allure.step("Клинкуть на кнопку Оформить заказ")
#     def make_order(self):
#         self.click_on_element(self.main_page_locators.BUTTON_MAKE_ORDER)
#
#     @allure.step("Ожидание видимости номера заказа")
#     def wait_for_made_order_modal_window(self):
#         self.wait_visibility_of_element(self.main_page_locators.ORDER_ID)
#
#     @allure.step("Номер заказа виден")
#     def order_id_is_visible(self):
#         return self.visibility_of_element(self.main_page_locators.ORDER_ID)

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_page_locators = MainPageLocators()

    @allure.step("Кликнуть на кнопку Конструктор")
    def click_in_constructor(self):
        self.click_on_element(self.main_page_locators.CONSTRUCTOR_LINK)

    @allure.step("Булочка видна")
    def buns_link_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.BUNS_LINK)

    @allure.step("Кликнуть на ленту заказов")
    def click_in_order_feed(self):
        self.click_on_element(self.main_page_locators.ORDER_FEED_LINK)

    @allure.step("Заголовок Лента заказов виден")
    def order_feed_header_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_FEED_HEADER)

    @allure.step("Ожидание заголовка Ленты заказов")
    def wait_for_order_feed_header(self):
        self.wait_visibility_of_element(self.main_page_locators.ORDER_FEED_HEADER)

    @allure.step("Кликнуть на булку")
    def click_on_crater_bun(self):
        self.click_on_element(self.main_page_locators.CRATER_BUN)

    @allure.step("Закрыть модально окно с номером заказа")
    def close_modal_window(self):
        self.click_on_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step("Ожидание появления элемента закрытия окна")
    def wait_for_modal_window(self):
        self.wait_visibility_of_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step("Ожидание повления элемента булочки")
    def wait_for_bun(self):
        self.wait_visibility_of_element(self.main_page_locators.CRATER_BUN)

    @allure.step("Кнопка закрытия модального окна видна")
    def close_modal_window_button_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step("Перемещение булочки в корзину")
    def drag_and_drop_bun(self):
        self.move_element(self.main_page_locators.CRATER_BUN,
                          self.main_page_locators.BURGER_INGREDIENTS)

    @allure.step("Количество булочек")
    def bun_counter_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.BUN_COUNTER)

    @allure.step("Клинкуть на кнопку Оформить заказ")
    def make_order(self):
        self.click_on_element(self.main_page_locators.BUTTON_MAKE_ORDER)

    @allure.step("Ожидание видимости номера заказа")
    def wait_for_made_order_modal_window(self):
        self.wait_visibility_of_element(self.main_page_locators.ORDER_ID)

    @allure.step("Номер заказа виден")
    def order_id_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_ID)