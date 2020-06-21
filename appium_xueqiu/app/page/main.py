from appium_xueqiu.app.page.base_page import BasePage
from appium_xueqiu.app.page.market import Market


class Main(BasePage):

    def goto_xueqiu(self):
        pass

    def goto_market(self):
        self.steps("../data/main.yml")
        return Market(self._driver)

    def goto_deal(self):
        pass

    def goto_my(self):
        pass
