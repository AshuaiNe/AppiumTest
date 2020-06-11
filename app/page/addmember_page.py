from app.page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class AddMember(BasePage):

    def manually_add(self):
        from app.page.manuallyadd_page import ManuallyAdd
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ManuallyAdd(self._driver)
