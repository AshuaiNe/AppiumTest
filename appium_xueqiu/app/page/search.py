from appium_xueqiu.app.page.base_page import BasePage
from selenium.webdriver.common.by import By


class Search(BasePage):
    def search(self, name):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("阿里巴巴")
        self.find(By.XPATH, "//*[@text='BABA']").click()
        self.find(By.XPATH, f"//*[contains(@resource-id, 'll_stock_item_container')]//*[@text='{name}']/../..//*[@text='加自选']").click()
        return self

    def add(self):
        pass

    def in_choose(self, name):
        self.find(By.XPATH, f"//*[contains(@resource-id, 'll_stock_item_container')]//*[@text='{name}']/../..//*[@text='已添加']")
        return self

    def reset(self):
        pass
