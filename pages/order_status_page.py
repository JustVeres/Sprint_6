import allure
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_order_status_page import StatusPageElements as SP

class OrderStatusPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на кнопку "Яндекс" в хедере')
    def click_yandex_button_on_header(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(SP.BUTTON_YANDEX_ON_HEADER))
        tabs_before = self.driver.window_handles
        self.driver.find_element(*SP.BUTTON_YANDEX_ON_HEADER).click()
        tabs_after = self.driver.window_handles
        new_tab = list(set(tabs_after) - set(tabs_before))[0]
        self.driver.switch_to.window(new_tab)
        wait(self.driver, 10).until(EC.url_contains("dzen.ru"))

    @allure.step('Кликаем на кнопку "Самокат" в хэдере')
    def click_scooter_button_on_header(self):
        wait(self.driver, 5).until(EC.visibility_of_element_located(SP.BUTTON_SCOOTER_ON_HEADER))
        self.driver.find_element(*SP.BUTTON_SCOOTER_ON_HEADER).click()
        wait(self.driver, 10).until(EC.url_contains("https://qa-scooter.praktikum-services.ru/"))
