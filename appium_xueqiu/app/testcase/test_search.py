from appium_xueqiu.app.page.app import App
import pytest
import yaml


class TestCase:
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    @pytest.mark.parametrize("name", yaml.safe_load(open("appium_xueqiu/app/testcase/test_search.yaml", encoding="utf-8")))
    def test_case(self, name):
        self.search.search(name)
        if self.search.is_choose(name):
            self.search.reset(name)
        self.search.add(name)
        assert self.search.is_choose(name)
