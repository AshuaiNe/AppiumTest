from app.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.mian = self.app.start().main()

    def test_addcontact(self):
        self.mian.goto_addresslist().add_member().manually_add().input_name().set_gender().input_phonenumber().goto_address().input_address().click_save()
