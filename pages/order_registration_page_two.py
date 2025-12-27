import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from data.data_order_scooter import AboutRent as AR
from locators.locators_order_registration_page_two import OrderPageTwoElements as OPT

class SecondPageOrdering:
    def __init__(self, driver):
        self.driver = driver

    """Заполняем обязательные поля на странице «Про аренду»"""
    @allure.step('Заполняем поле "* Когда привезти самокат"')
    def fill_date_for_the_order_field(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPT.DATE_FOR_THE_ORDER))
        self.driver.find_element(*OPT.DATE_FOR_THE_ORDER).send_keys(AR.next_day_order, Keys.ENTER)

    @allure.step('Заполняем поле "* Срок аренды"')
    def fill_rental_period_field(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPT.RENTAL_PERIOD))
        self.driver.find_element(*OPT.RENTAL_PERIOD).click()
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPT.RENTAL_PERIOD_DAY))
        self.driver.find_element(*OPT.RENTAL_PERIOD_DAY).click()

    @allure.step('Заполняем "Цвет самоката"')
    def fill_color_scooter_field(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(OPT.SCOOTER_COLOR))
        self.driver.find_element(*OPT.SCOOTER_COLOR).click()

    """Клик на кнопки на странице заказа"""
    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        wait(self.driver, 5).until(EC.element_to_be_clickable(OPT.BUTTON_ORDER)).click()

    """Взаимодействие с модальным окном «Хотите оформить заказ?»"""
    @allure.step('Клик по кнопке "Да"')
    def click_yes_button(self):
        wait(self.driver, 5).until(EC.element_to_be_clickable(OPT.BUTTON_YES)).click()

    """Взаимодействие с модальным окном «Заказ оформлен»"""
    @allure.step('Смотрим модальное окно «Заказ оформлен»')
    def get_success_order_text(self):
        element = wait(self.driver, 5).until(EC.visibility_of_element_located(OPT.MODAL_SUCCESS_HEADER))
        return element.text

    @allure.step('Нажимаем на кнопку "Посмотреть статус"')
    def click_button_check_status(self):
        wait(self.driver, 5).until(EC.element_to_be_clickable(OPT.BUTTON_CHECK_STATUS)).click()