import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.data_url import Urls

class TestCheckRedirect:
    @allure.title('Проверка редиректа на dzen.ru через кнопки хедера после заказа')
    @allure.description('Тест-кейс на проверку перенаправления на dzen.ru после успешного оформления заказа через верхнюю и среднюю кнопку заказа на сайте')
    @pytest.mark.parametrize("start_order", ["click_top_order_button", "click_middle_order_button"])
    def test_redirect_to_dzen_page_after_order(self, driver, start_order):
        main_page = MainPage(driver)
        main_page.open_main_page()
        # Старт заказа
        getattr(main_page, start_order)()

        """Делаем заказ"""
        # Первая страница заказа
        order_page = OrderPage(driver)
        order_page.fill_first_name_field()
        order_page.fill_last_name_field()
        order_page.fill_city_field()
        order_page.fill_metro_station_field()
        order_page.fill_number_phone_field()
        order_page.click_next_button()

        # Вторая страница заказа
        order_page.fill_date_for_the_order_field()
        order_page.fill_rental_period_field()
        order_page.fill_color_scooter_field()
        order_page.click_order_button()
        order_page.click_yes_button()
        order_page.click_button_check_status()

        main_page.click_yandex_button_on_header()

        assert Urls.dzen_url in order_page.get_current_url()

    @allure.title('Проверка редиректа на главную страницу через кнопки хедера после заказа')
    @allure.description('Тест-кейс на проверку перенаправления на главную страницу после успешного оформления заказа через верхнюю и среднюю кнопку заказа на сайте')
    @pytest.mark.parametrize("start_order", ["click_top_order_button", "click_middle_order_button"])
    def test_redirect_to_main_page_after_order(self, driver, start_order):
        main_page = MainPage(driver)
        main_page.open_main_page()
        # Старт заказа
        getattr(main_page, start_order)()

        """Делаем заказ"""
        # Первая страница заказа
        order_page = OrderPage(driver)
        order_page.fill_first_name_field()
        order_page.fill_last_name_field()
        order_page.fill_city_field()
        order_page.fill_metro_station_field()
        order_page.fill_number_phone_field()
        order_page.click_next_button()

        # Вторая страница заказа
        order_page.fill_date_for_the_order_field()
        order_page.fill_rental_period_field()
        order_page.fill_color_scooter_field()
        order_page.click_order_button()
        order_page.click_yes_button()
        order_page.click_button_check_status()

        main_page.click_scooter_button_on_header()

        assert order_page.get_current_url() == Urls.qa_scooter_main_url
