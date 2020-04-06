from pageobject.page.address_book import AddressBook


class TestAddressBook:
    def setup(self):
        self.address_book = AddressBook()

    def teardown(self):
        self.address_book.driver.quit()

    def test_click_add_member(self):
        self.address_book.goto_add_member()
