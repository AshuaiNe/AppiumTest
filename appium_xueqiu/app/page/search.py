from appium_xueqiu.app.page.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        self._params["name"] = name
        self.steps("appium_xueqiu/app/data/search.yml")
        return self

    def add(self, name):
        self._params["name"] = name
        self.steps("appium_xueqiu/app/data/search.yml")

    def is_choose(self, name):
        self._params["name"] = name
        return self.steps("appium_xueqiu/app/data/search.yml")

    def reset(self, name):
        self._params["name"] = name
        self.steps("appium_xueqiu/app/data/search.yml")
        return self
