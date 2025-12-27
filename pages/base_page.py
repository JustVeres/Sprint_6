from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self, url):
        self.driver.get(url)

    def presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_clickable(locator).click()

    def scroll_to_element(self, locator):
        element = self.presence(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        return element

    def scroll_and_click(self, locator):
        element = self.scroll_to_element(locator)
        self.wait_clickable(locator)
        element.click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_window_handles(self):
        return self.driver.window_handles

    def get_current_url(self):
        return self.driver.current_url

    def get_url_contains(self, url):
        return self.wait.until(EC.url_contains(url))

    def find_element_text(self, locator):
       return self.driver.find_element(*locator).text
