from selenium.webdriver.common.by import By
from pageobject.page.address_book import AddressBook
from pageobject.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self, name, account, phone):
        self.find(By.CSS_SELECTOR, '.ww_compatibleTxt.ww_compatibleTxt_Small.ww_inputWithTips_WithErr').send_keys(name)
        self.find(By.ID, '#memberAdd_acctid').send_keys(account)
        self.find(By.ID, '#memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.qui_btn ww_btn.js_btn_save').click()
        return AddressBook(self.driver)

