from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage
from pageobject.page.register import Register


class Login(BasePage):
    """
    1、扫码
        用手机扫码二维码
    2、立即注册
        1、点击立即注册
        2、return立即注册PageObject
    """
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self.driver)
