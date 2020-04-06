import json
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_opts = webdriver.ChromeOptions()
            chrome_opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome()
            self.driver.get('https://work.weixin.qq.com/')
            # cookies = self.driver.get_cookies()
            # with open("cookies.txt", "w") as f:  # 将已登录的页面的cookie存入文件
            #     json.dump(cookies, f)
            with open("E:/HogwartsLagouTesting/pageobject/testcase/cookies.txt","r") as f:  # 读取cookie存入文件
                cookies: List[Dict] = json.load(f)
            for cookie in cookies:
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                self.driver.add_cookie(cookie)  # 将已登录的cookie添加到chrome中
        else:
            self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
