import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from data.data_order_page import WhoIsTheScooterFor as WF
from data.data_order_page import AboutRent as AR
from locators.locators_order_page import OrderPageOneElements as OPO, OrderPageTwoElements as OPT


class OrderPage(BasePage):

    """Страница «Для кого самокат»"""

    @allure.step('Заполняем поле "* Имя"')
    def fill_first_name_field(self):
        self.wait_visible(OPO.FIRST_NAME_FIELD).send_keys(WF.first_name)

    @allure.step('Заполняем поле "* Фамилия"')
    def fill_last_name_field(self):
        self.wait_visible(OPO.LAST_NAME_FIELD).send_keys(WF.last_name)

    @allure.step('Заполняем поле "* Адрес: куда привезти заказ"')
    def fill_city_field(self):
        self.wait_visible(OPO.CITY_FIELD).send_keys(WF.city)

    @allure.step('Заполняем поле "* Станция метро"')
    def fill_metro_station_field(self):
        self.wait_visible(OPO.METRO_STATION_FIELD).send_keys(WF.metro_station)
        self.click(OPO.SELECT_ANY_STATION)

    @allure.step('Заполняем поле "* Телефон: на него позвонит курьер"')
    def fill_number_phone_field(self):
        self.wait_visible(OPO.NUMBER_PHONE_FIELD).send_keys(WF.number_phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click(OPO.BUTTON_NEXT)

    """Страница «Про аренду»"""

    @allure.step('Заполняем поле "* Когда привезти самокат"')
    def fill_date_for_the_order_field(self):
        self.wait_visible(OPT.DATE_FOR_THE_ORDER).send_keys(AR.next_day_order, Keys.ENTER)

    @allure.step('Заполняем поле "* Срок аренды"')
    def fill_rental_period_field(self):
        self.click(OPT.RENTAL_PERIOD)
        self.click(OPT.RENTAL_PERIOD_DAY)

    @allure.step('Заполняем поле "Цвет самоката"')
    def fill_color_scooter_field(self):
        self.click(OPT.SCOOTER_COLOR)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.click(OPT.BUTTON_ORDER)

    """Модальные окна"""

    @allure.step('Клик по кнопке "Да" в модальном окне подтверждения')
    def click_yes_button(self):
        self.click(OPT.BUTTON_YES)

    @allure.step('Получаем текст из модального окна «Заказ оформлен»')
    def get_success_order_text(self):
        return self.wait_visible(OPT.MODAL_SUCCESS_HEADER).text

    @allure.step('Нажимаем на кнопку "Посмотреть статус"')
    def click_button_check_status(self):
        self.click(OPT.BUTTON_CHECK_STATUS)
