from selenium.webdriver.common.by import By

"""qa-scooter.praktikum-services.ru/"""
class ElementsMainPage:
    # Кнопка "Заказать" наверху страницы
    TOP_ORDER_BUTTON =  (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    # Кнопка "Заказать" посередине страницы
    MIDDLE_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    # Локаторы вопросов (кликабельные элементы)
    DROP_DOWN_TEXT = [(By.ID, f"accordion__heading-{i}") for i in range(8)]

    # Локаторы ответов на вопросы
    ELEMENT_FIRST = (By.ID, "accordion__panel-0")
    ELEMENT_SECOND = (By.ID, "accordion__panel-1")
    ELEMENT_THIRD = (By.ID, "accordion__panel-2")
    ELEMENT_FOURTH = (By.ID, "accordion__panel-3")
    ELEMENT_FIFTH = (By.ID, "accordion__panel-4")
    ELEMENT_SIXTH = (By.ID, "accordion__panel-5")
    ELEMENT_SEVENTH = (By.ID, "accordion__panel-6")
    ELEMENT_EIGHTH = (By.ID, "accordion__panel-7")

    # Кнопки в хэдере
    BUTTON_YANDEX_ON_HEADER = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")   # Кнопка "Яндекс" на лого в хедере
    BUTTON_SCOOTER_ON_HEADER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR") # # Кнопка "Самокат" на лого в хедере
