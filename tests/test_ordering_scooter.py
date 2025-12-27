import pytest
import allure
from pages.main_page import MainPage
from pages.order_registration_page_one import FirstPageOrdering
from pages.order_registration_page_two import SecondPageOrdering
from data.data_url import Url

class TestOrderingScooter:
    @allure.title('Проверка заказа самоката')
    @allure.description('Тест-кейс на проверку успешного заказа через верхнюю и среднюю кнопку заказа на сайте')
    @pytest.mark.parametrize("start_order", ["wait_and_click_top_order_button", "scroll_and_click_middle_order_button"])
    def test_order_scooter(self, driver, start_order):
        driver.get(Url.qa_scooter_main_url)
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

        # Проверка успешного оформления заказа
        assert "Заказ оформлен" in SPO.get_success_order_text()
