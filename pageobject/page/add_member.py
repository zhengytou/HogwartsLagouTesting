from typing import List
from selenium.webdriver.common.by import By
from pageobject.page.address_book import AddressBook
from pageobject.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self, name, account, phone):
        self.find(By.ID, 'username').send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.driver.find_elements_by_css_selector('.qui_btn.ww_btn.js_btn_save')[0].click()
        return AddressBook(self.driver)

    def get_name(self) -> List:
        name = []
        elements: List = self.driver.find_elements_by_css_selector('td:nth-child(2)')
        for e in elements:
            name.append(e.text)
        return name

    def get_mobile(self) -> List:
        mobile = []
        elements: List = self.driver.find_elements_by_css_selector('td:nth-child(5)')
        for e in elements:
            mobile.append(e.text)
        return mobile
