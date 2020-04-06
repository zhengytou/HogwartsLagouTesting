import pytest
from pageobject.page.add_member import AddMember
from pageobject.page.index import IndexPage

data = [("测试1", "hogwarts002", '13112341231'), ("测试2", "hogwarts001", '13112341232'),
        ("测试3", "hogwarts003", '13112341233')]


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
        assert name in AddMember(self.index.driver).get_name()
        assert phone in AddMember(self.index.driver).get_mobile()
