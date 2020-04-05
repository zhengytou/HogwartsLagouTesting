import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestFile:
    @pytest.mark.skip
    def test_file_upload(self, driver):
        """
        打开百度图片，点击上传一张本地图片
        """
        driver.get('http://image.baidu.com/')
        driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        driver.find_element_by_id('stfile').send_keys('E:\hi.jpg')
        sleep(3)

    def test_alert(self, driver):
        """
        打开网页 https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作右侧页面，将元素1拖拽到元素2
        这时候会有一个alert弹框，点击弹框中的‘确定’
        然后点击‘点击运行’
        关闭网页
        :param driver: fixture返回的一个webdriver
        :return:
        """
        driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        driver.switch_to.frame('iframeResult')  # 切换到需要的frame
        drag_element = driver.find_element_by_id('draggable')
        drop_element = driver.find_element_by_id('droppable')
        action = ActionChains(driver)  # 生成一个动作
        action.drag_and_drop(drag_element, drop_element).perform()  # 拖拽并释放
        sleep(2)
        alert = driver.switch_to.alert  # 切换到alert弹框
        alert.accept()  # alert弹出上的确认按钮
        driver.switch_to.default_content()  # 切换回默认的frame
        driver.find_element_by_id('submitBTN').click()
