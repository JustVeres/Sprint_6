import allure
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from data.data_order_scooter import WhoIsTheScooterFor as WF
from locators.locators_order_registration_page_one import OrderPageOneElements as OPO

class FirstPageOrdering:
    def __init__(self, driver):
        self.driver = driver

    """Заполняем обязательные поля на странице «Для кого самокат»"""
    @allure.step('Заполняем поле "* Имя"')
    def fill_first_name_field(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPO.FIRST_NAME_FIELD))
        self.driver.find_element(*OPO.FIRST_NAME_FIELD).send_keys(WF.first_name)

    @allure.step('Заполняем поле "* Фамилия"')
    def fill_last_name_field(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPO.LAST_NAME_FIELD))
        self.driver.find_element(*OPO.LAST_NAME_FIELD).send_keys(WF.last_name)

    @allure.step('Заполняем поле "* Адрес: куда привезти заказ"')
    def fill_city_field(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPO.CITY_FIELD))
        self.driver.find_element(*OPO.CITY_FIELD).send_keys(WF.city)

    @allure.step('Заполняем поле "* Станция метро"')
    def fill_metro_station_field(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPO.METRO_STATION_FIELD))
        self.driver.find_element(*OPO.METRO_STATION_FIELD).send_keys(WF.metro_station)
        self.driver.find_element(*OPO.SELECT_ANY_STATION).click()

    @allure.step('Заполняем поле "* Телефон: на него позвонит курьер"')
    def fill_number_phone_field(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPO.NUMBER_PHONE_FIELD))
        self.driver.find_element(*OPO.NUMBER_PHONE_FIELD).send_keys(WF.number_phone)

    """Клик на кнопки на странице заказа"""
    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        wait(self.driver, 5).until(EC.element_to_be_clickable(OPO.BUTTON_NEXT)).click()