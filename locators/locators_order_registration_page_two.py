from selenium.webdriver.common.by import By
from data.data_order_scooter import AboutRent as AR

class OrderPageTwoElements:
    DATE_FOR_THE_ORDER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # Локатор для поля "* Когда привезти самокат"
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']") # Локатор для поля "* Срок аренды"
    RENTAL_PERIOD_DAY = (By.XPATH, f"//div[@role='option' and text()='{AR.rent_a_day}']") # Выбор срока аренды
    SCOOTER_COLOR = (By.ID, f"{AR.color_order}") # Выбор цвета самоката
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']") # Кнопка "Заказать" посередине
    BUTTON_YES = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']") # Кнопка "Да"
    MODAL_SUCCESS_HEADER = (By.XPATH, "//div[text()='Заказ оформлен']")  # Модальное окно с заголовком "Заказ оформлен"
    BUTTON_CHECK_STATUS = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']") # Кнопка "Посмотреть статус"
