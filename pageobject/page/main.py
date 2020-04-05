from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage
from pageobject.page.login import Login
from pageobject.page.register import Register


class Main(BasePage):
    """
    1、立即注册
        1、点击立即注册
        2、return立即注册PageObject
    2、企业登录
        1、点击企业登录
        2、return企业登录PageObject
    """
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self.driver)
