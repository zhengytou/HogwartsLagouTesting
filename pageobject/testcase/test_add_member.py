import pytest

from pageobject.page.address_book import AddressBook
from pageobject.page.index import IndexPage

data = [()]


class TestAddressBook:
    @classmethod
    def setup_class(cls):
        cls.index = IndexPage()

    @classmethod
    def teardown_class(cls):
        cls.index.driver.quit()

    @pytest.mark.parametrize('name,account,phone', data)
    def test_click_add_member(self, name, account, phone):
        self.index.goto_add_member().add_member(name, account, phone)
