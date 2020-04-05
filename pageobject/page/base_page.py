from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
