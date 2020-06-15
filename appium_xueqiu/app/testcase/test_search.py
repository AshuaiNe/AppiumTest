from appium_xueqiu.app.page.app import App


class TestCase:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_case(self):
        ele = self.main.goto_market().goto_search().search("阿里巴巴")
        assert ele.in_choose("阿里巴巴")
