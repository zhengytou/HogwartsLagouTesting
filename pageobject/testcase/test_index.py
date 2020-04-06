from time import sleep

import pytest

from pageobject.page.index import IndexPage


class TestIndex:
    @classmethod
    def setup_class(cls):
        cls.index = IndexPage()

    @classmethod
    def teardown_class(cls):
        cls.index.driver.quit()
    # @pytest.mark.skip
    def test_click_add_member(self):
        self.index.goto_add_member()
        self.index.assert_goto_add_member()

    # @pytest.mark.skip
    def test_goto_import_address_book(self):
        self.index.goto_import_address_book()
        self.index.assert_goto_import_address_book()

    # @pytest.mark.skip
    def test_goto_mass_message(self):
        self.index.goto_mass_message()
        self.index.assert_goto_mass_message()

    # @pytest.mark.skip
    def test_goto_punch_the_clock(self):
        self.index.goto_punch_the_clock()
        self.index.assert_goto_punch_the_clock()

    # @pytest.mark.skip
    def test_goto_sale_service(self):
        self.index.goto_sale_service()
        self.index.assert_goto_sale_service()

    # @pytest.mark.skip
    def test_goto_join_member(self):
        self.index.goto_join_member()
        self.index.assert_goto_join_member()
