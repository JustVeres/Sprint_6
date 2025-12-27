from selenium.webdriver.common.by import By
from data.data_order_scooter import WhoIsTheScooterFor as WF

class OrderPageOneElements:
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']") # Локатор для поля "* Имя"
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")   # Локатор для поля "* Фамилия"
    CITY_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # Локатор для поля "* Адрес: куда привезти заказ"
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']") # Локатор для поля "* Станция метро"
    NUMBER_PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # Локатор для поля "* Телефон: на него позвонит курьер"
    SELECT_ANY_STATION = (By.XPATH, f"//*[text()='{WF.metro_station}']") # Локатор для выбора станции для поля "* Станция метро"
    BUTTON_NEXT =  (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']") # Локатор для кнопки "Далее"