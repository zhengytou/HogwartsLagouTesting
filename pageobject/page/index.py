from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageobject.page.add_member import AddMember
from pageobject.page.base_page import BasePage
from pageobject.page.import_address_book import ImportAddressBook
from pageobject.page.join_member import JoinMember
from pageobject.page.mass_message import MassMessage
from pageobject.page.punch_the_clock import PunchTheClock
from pageobject.page.sale_service import SaleService


class IndexPage(BasePage):
    index_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.driver.get(self.index_url)
        element = self.find(By.CSS_SELECTOR, ".index_service_cnt.js_service_list a:nth-child(1)")
        ActionChains(self.driver).click(element).perform()
        return AddMember(self.driver)

    def assert_goto_add_member(self):
        text = self.driver.find_element_by_link_text('添加成员').text
        assert text == '添加成员'

    def goto_import_address_book(self):
        self.driver.get(self.index_url)
        element = self.find(By.CSS_SELECTOR, ".index_service_cnt.js_service_list a:nth-child(2)")
        ActionChains(self.driver).click(element).perform()
        return ImportAddressBook(self.driver)

    def assert_goto_import_address_book(self):
        sleep(1)
        text = self.find(By.CSS_SELECTOR, '.util_fz_large.import_auto_title').text
        assert text == '上传通讯录，将智能识别成员和架构导入'

    def goto_join_member(self):
        self.driver.get(self.index_url)
        element = self.find(By.CSS_SELECTOR, ".index_service_cnt.js_service_list a:nth-child(3)")
        ActionChains(self.driver).click(element).perform()
        return JoinMember(self.driver)

    def assert_goto_join_member(self):
        sleep(1)
        text = self.find(By.CSS_SELECTOR, '.ww_normalCntHead_title_content').text
        assert text == '成员加入'

    def goto_mass_message(self):
        self.driver.get(self.index_url)

        element = self.find(By.CSS_SELECTOR, ".index_service_cnt.js_service_list a:nth-child(4)")
        ActionChains(self.driver).click(element).perform()
        sleep(3)
        return MassMessage(self.driver)

    def assert_goto_mass_message(self):
        sleep(1)
        text = self.find(By.CSS_SELECTOR, '.msg_create_infoItem_selectApps.js_select_apps_btn').text
        assert text == '选择需要发消息的应用'

    def goto_sale_service(self):
        self.driver.get(self.index_url)
        element = self.find(By.CSS_SELECTOR, ".index_service_cnt.js_service_list a:nth-child(5)")
        ActionChains(self.driver).click(element).perform()
        return SaleService(self.driver)

    def assert_goto_sale_service(self):
        sleep(1)
        text = self.find(By.CSS_SELECTOR, '.util_ml_small.util_fz_large').text
        print(text)
        assert text == '查看'

    def goto_punch_the_clock(self):
        self.driver.get(self.index_url)
        element = self.find(By.CSS_SELECTOR, ".index_service_cnt.js_service_list a:nth-child(6)")
        ActionChains(self.driver).click(element).perform()
        return PunchTheClock(self.driver)

    def assert_goto_punch_the_clock(self):
        sleep(1)
        text = self.find(By.CSS_SELECTOR, '.app_stage_header_info_title').text
        assert text == '打卡'
