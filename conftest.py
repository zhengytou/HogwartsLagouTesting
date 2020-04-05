import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def pytest_configure(config):
    marks_list = ["Web", "Interface"]
    for mark in marks_list:
        config.addinivalue_line("markers", mark)


@pytest.fixture(scope='session')
def driver() -> webdriver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    WebDriverWait.until()
    yield driver
    driver.quit()
