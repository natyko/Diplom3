import allure

from pages.main_page import MainPage
from tests.conftest import driver_signed_in


@allure.feature("Главная страница")
class TestMainPage:
    @allure.description("Переход по клику на «Конструктор»")
    def test_constructor_link(self, driver):
        constructor_link = MainPage(driver)
        constructor_link.click_in_constructor()
        assert constructor_link.buns_link_is_visible()

    @allure.description("Переход по клику на «Лента заказов»")
    def test_order_feed(self, driver):
        order_feed = MainPage(driver)
        order_feed.click_in_order_feed()
        order_feed.wait_for_order_feed_header()
        assert order_feed.order_feed_header_is_visible()

    @allure.description("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_modal_window_is_seen(self, driver):
        modal_window = MainPage(driver)
        modal_window.click_in_constructor()
        modal_window.wait_for_bun()
        modal_window.click_on_crater_bun()
        modal_window.wait_for_modal_window()
        assert modal_window.close_modal_window_button_is_visible()

    @allure.description("Всплывающее окно закрывается кликом по крестику")
    def test_close_modal_window(self, driver):
        modal_window = MainPage(driver)
        modal_window.click_in_constructor()
        modal_window.wait_for_bun()
        modal_window.click_on_crater_bun()
        modal_window.wait_for_modal_window()
        modal_window.close_modal_window()
        assert modal_window.buns_link_is_visible()

    @allure.description("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_counter(self, driver):
        counter = MainPage(driver)
        counter.click_in_constructor()
        counter.wait_for_bun()
        counter.drag_and_drop_bun()
        assert counter.bun_counter_is_visible()

    @allure.description(
        "Залогиненный пользователь может оформить заказ")
    def test_make_order_success(self, driver_signed_in):
        order = MainPage(driver_signed_in)
        order.wait_for_bun()
        order.drag_and_drop_bun()
        order.make_order()
        order.wait_for_made_order_modal_window()
        assert order.order_id_is_visible()