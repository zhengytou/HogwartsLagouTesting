from pageobject.page.main import Main


class TestRegister:
    # def setup(self, driver):
    #     self.main = Main(driver)

    def test_register(self,driver):
        main=Main(driver)
        assert main.goto_register().register()
