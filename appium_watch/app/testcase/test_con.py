from appium_watch.app.page.app import App
import yaml
import pytest


class TestContact:
    def setup(self):
        self.app = App()
        self.mian = self.app.start().main()

    @pytest.mark.parametrize('name, phonenumber, address', yaml.safe_load(open("appium_watch/app/data/data.yml", encoding='utf-8')))
    def test_addcontact(self, name, phonenumber, address):
        invitpage = self.mian.goto_addresslist().add_member().manually_add().input_name(name).set_gender().input_phonenumber(phonenumber).goto_address().input_address(address).click_save()
        assert '添加成功' in invitpage.get_toast()
