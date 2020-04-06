from time import sleep

from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self, name, account, phone):
        self.driver.find_element_by_id('username').send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone)
        self.driver.find_elements_by_css_selector('.qui_btn.ww_btn.js_btn_save')[0].click()
        return True

