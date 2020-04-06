from time import sleep

from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage

class AddressBook(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()

