from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            self.driver.get(self._base_url)
        else:
            self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
