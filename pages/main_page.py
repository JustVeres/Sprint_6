import allure
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_main_page import ElementsMainPage as EMP

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    """Верхняя часть главной страницы"""
    # ожидание и клик по кнопке заказа в верхней части страницы
    @allure.step('Ожидание и клик по кнопке заказа в верхней части страницы')
    def wait_and_click_top_order_button(self):
        wait(self.driver, 5).until(EC.element_to_be_clickable(EMP.TOP_ORDER_BUTTON)).click()

    """Средняя часть главной страницы"""
    # скролл и клик до кнопки заказа в средней области страницы
    @allure.step('Скролл и клик до кнопки заказа в средней области страницы')
    def scroll_and_click_middle_order_button(self):
        element = self.driver.find_element(*EMP.MIDDLE_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    """Нижняя часть главной страницы"""
    # скролл до низа страницы
    @allure.step('Скролл до низа страницы')
    def scroll_bottom_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # клик по раскрывающемуся списку в разделе «Вопросы о важном»
    @allure.step('Клик по раскрывающемуся списку в разделе «Вопросы о важном»')
    def click_questions(self, index: int):
        self.driver.find_element(*EMP.DROP_DOWN_TEXT[index]).click()

    # ожидаем видимость ответа под вопросами
    @allure.step('Ожидаем видимость ответа под вопросами')
    def wait_answer(self, answer_locator):
        wait(self.driver, 5).until(EC.visibility_of_element_located(answer_locator))
