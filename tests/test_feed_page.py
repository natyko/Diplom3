from pages.feed_page import FeedPage

from tests.conftest import driver_signed_in
import allure


@allure.feature("Лента заказов")
class TestFeedPage:

    @allure.description("При клике на заказ открывается всплывающее окно с деталями")
    def test_order_info_is_displayed(self, driver):
        order_info = FeedPage(driver)
        order_info.click_on_feed()
        order_info.wait_for_order_feed()
        order_info.click_on_first_order()
        assert order_info.order_info_is_displayed()

    @allure.description("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_my_order_is_visible_in_order_feed(self, driver_signed_in):
        order = FeedPage(driver_signed_in)
        order.click_on_feed()
        order.wait_for_order_feed()
        order.scroll_to_order()
        assert order.my_order_is_visible()

    @allure.description(
        "При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_quantity_orders_for_all_time_correct(self, driver_signed_in):
        order = FeedPage(driver_signed_in)
        order.click_on_feed()
        order.wait_for_order_feed()
        quantity_before_order = int(order.orders_for_all_time_())
        order.click_on_constructor()
        order.drag_and_drop_bun()
        order.make_order()
        order.wait_for_modal_window_to_be_closed()
        order.close_modal_window()
        order.click_on_feed()
        order.wait_for_order_feed()
        quantity_after_order = int(order.orders_for_all_time_())
        assert quantity_after_order > quantity_before_order

    @allure.description(
        "При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_orders_for_today_correct(self, driver_signed_in):
        order = FeedPage(driver_signed_in)
        order.click_on_feed()
        order.wait_for_order_feed()
        quantity_before_order = int(order.orders_for_today())
        order.click_on_constructor()
        order.drag_and_drop_bun()
        order.make_order()
        order.wait_for_modal_window_to_be_closed()
        order.close_modal_window()
        order.click_on_feed()
        order.wait_for_order_feed()
        quantity_after_order = int(order.orders_for_today())
        assert quantity_after_order > quantity_before_order

    @allure.description(
        "После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_process_correct(self, driver_signed_in):
        order = FeedPage(driver_signed_in)
        order.click_on_constructor()
        order.drag_and_drop_bun()
        order.make_order()
        order.wait_for_modal_window_to_be_closed()
        number_of_order = int(order.get_order_in_main_page())
        order.close_modal_window()
        order.click_on_feed()
        order.wait_for_order_feed()
        number_in_feed = None
        if order.wait_for_order_number():
            number_in_feed = int(order.get_order_in_feed())
        assert number_of_order == number_in_feed