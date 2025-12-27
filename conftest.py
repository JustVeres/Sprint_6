import pytest
from selenium import webdriver

@pytest.fixture # Фикстура для запуска и закрытия браузера Firefox
def driver():
    driver_instance = webdriver.Firefox()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()
