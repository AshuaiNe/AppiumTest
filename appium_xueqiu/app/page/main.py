from appium_xueqiu.app.page.base_page import BasePage
from selenium.webdriver.common.by import By
from appium_xueqiu.app.page.market import Market


class Main(BasePage):

    def goto_xueqiu(self):
        pass

    def goto_market(self):
        self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return Market(self._driver)

    def goto_deal(self):
        pass

    def goto_my(self):
        pass
