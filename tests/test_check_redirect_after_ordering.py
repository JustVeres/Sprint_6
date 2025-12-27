import pytest
import allure
from pages.main_page import MainPage
from pages.order_registration_page_one import FirstPageOrdering
from pages.order_registration_page_two import SecondPageOrdering
from pages.order_status_page import OrderStatusPage

class TestCheckRedirect:
    @allure.title('Проверка редиректа на dzen.ru через кнопки хедера после заказа')
    @allure.description('Тест-кейс на проверку перенаправления на dzen.ru после успешного оформления заказа через верхнюю и среднюю кнопку заказа на сайте')
    @pytest.mark.parametrize("start_order", ["wait_and_click_top_order_button", "scroll_and_click_middle_order_button"])
    def test_redirect_to_dzen_page_after_order(self, driver, website, start_order):
        driver.get(website)
        main = MainPage(driver)
        # Старт заказа
        getattr(main, start_order)()

        # Первая страница заказа
        FPO = FirstPageOrdering(driver)
        FPO.fill_first_name_field()
        FPO.fill_last_name_field()
        FPO.fill_city_field()
        FPO.fill_metro_station_field()
        FPO.fill_number_phone_field()
        FPO.click_next_button()

        # Вторая страница заказа
        SPO = SecondPageOrdering(driver)
        SPO.fill_date_for_the_order_field()
        SPO.fill_rental_period_field()
        SPO.fill_color_scooter_field()
        SPO.click_order_button()
        SPO.click_yes_button()
        SPO.click_button_check_status()

        # Страница статуса заказа
        OSP = OrderStatusPage(driver)
        OSP.click_yandex_button_on_header()
        # Проверка открытия страницы dzen.ru
        assert "dzen.ru" in driver.current_url

    @allure.title('Проверка редиректа на главную страницу через кнопки хедера после заказа')
    @allure.description('Тест-кейс на проверку перенаправления на главную страницу после успешного оформления заказа через верхнюю и среднюю кнопку заказа на сайте')
    @pytest.mark.parametrize("start_order", ["wait_and_click_top_order_button", "scroll_and_click_middle_order_button"])
    def test_redirect_to_main_page_after_order(self, driver, website, start_order):
        driver.get(website)
        main = MainPage(driver)
        # Старт заказа
        getattr(main, start_order)()

        # Первая страница заказа
        FPO = FirstPageOrdering(driver)
        FPO.fill_first_name_field()
        FPO.fill_last_name_field()
        FPO.fill_city_field()
        FPO.fill_metro_station_field()
        FPO.fill_number_phone_field()
        FPO.click_next_button()

        # Вторая страница заказа
        SPO = SecondPageOrdering(driver)
        SPO.fill_date_for_the_order_field()
        SPO.fill_rental_period_field()
        SPO.fill_color_scooter_field()
        SPO.click_order_button()
        SPO.click_yes_button()
        SPO.click_button_check_status()

        # Страница статуса заказа
        OSP = OrderStatusPage(driver)
        OSP.click_scooter_button_on_header()
        # Проверка открытия главной страницы
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
