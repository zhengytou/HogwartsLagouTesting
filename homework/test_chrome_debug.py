import json
from typing import List, Dict
from selenium import webdriver


class TestTest:
    def setup_method(self, method):
        # 声明一个变量，设置为chrometoptions
        chrome_opts = webdriver.ChromeOptions()
        # set address same as chrome debugging port
        chrome_opts.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_opts)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookie(self):
        cookies = self.driver.get_cookies()
        # with open("cookies.txt", "w") as f:  # 将已登录的页面的cookie存入文件
        #     json.dump(cookies, f)
        with open("cookies.txt" "r") as f:  # 读取cookie存入文件
            cookies: List[Dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)  # 将已登录的cookie添加到chrome中
        self.driver.get("https://home.testing-studio.com/t/topic/1362")  # 直接访问目标网页，不用一步步点击
