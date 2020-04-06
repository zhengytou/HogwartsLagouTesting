import pytest

from pageobject.page.add_member import AddMember
from pageobject.page.index import IndexPage

data = [('test1', 2, 13012341230), ('test2', 3, 13012341231), ('test3', 4, 13012341232)]


class TestAddMember:
    @classmethod
    def setup_class(cls):
        cls.index = IndexPage()

    @classmethod
    def teardown_class(cls):
        cls.index.driver.quit()

    @pytest.mark.parametrize('name,account,phone', data)
    def test_add_member(self, name, account, phone):
        self.index.goto_add_member().add_member(name, account, phone)
