from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage


class Register(BasePage):
    """
    1、填表
        1、输入文本
        2、下拉框
        3、点击确定
    """
    def register(self):
        self.find(By.ID, 'corp_name').send_keys("hello")
        self.find(By.ID, 'manager_name').send_keys("hello2")
        return True
