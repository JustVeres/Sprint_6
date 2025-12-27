import allure
from pages.base_page import BasePage
from locators.locators_main_page import ElementsMainPage as EMP
from data.data_url import Urls

"""qa-scooter.praktikum-services.ru/"""
class MainPage(BasePage):

    @allure.step('Открываем сайт qa-scooter')
    def open_main_page(self):
        self.open(Urls.qa_scooter_main_url)

    @allure.step('Нажимаем верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.click(EMP.TOP_ORDER_BUTTON)

    @allure.step('Скроллим и нажимаем кнопку "Заказать" в середине страницы')
    def click_middle_order_button(self):
        self.scroll_and_click(EMP.MIDDLE_ORDER_BUTTON)

    @allure.step('Скроллим страницу до низа')
    def scroll_bottom_page(self):
        self.scroll_to_bottom()

    @allure.step('Кликаем по вопросу в разделе «Вопросы о важном»')
    def click_questions(self, index: int):
        self.click(EMP.DROP_DOWN_TEXT[index])

    @allure.step('Ожидаем отображение ответа')
    def wait_answer(self, answer_locator):
        self.wait_visible(answer_locator)

    @allure.step('Кликаем на кнопку "Яндекс" в хедере')
    def click_yandex_button_on_header(self):
        self.wait_visible(EMP.BUTTON_YANDEX_ON_HEADER)
        tabs_before = self.get_window_handles()
        self.click(EMP.BUTTON_YANDEX_ON_HEADER)
        tabs_after = self.get_window_handles()
        new_tab = list(set(tabs_after) - set(tabs_before))[0]
        self.driver.switch_to.window(new_tab)
        self.get_url_contains(Urls.dzen_url)

    @allure.step('Кликаем на кнопку "Самокат" в хедере')
    def click_scooter_button_on_header(self):
        self.click(EMP.BUTTON_SCOOTER_ON_HEADER)
        self.get_url_contains(Urls.qa_scooter_main_url)
