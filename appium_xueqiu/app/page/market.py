from appium_xueqiu.app.page.base_page import BasePage
from appium_xueqiu.app.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        # self.steps("../data/market.yml")
        return Search(self._driver)
