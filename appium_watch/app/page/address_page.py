from page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class AddressPage(BasePage):
    def input_address(self, address):
        from app.page.manuallyadd_page import ManuallyAdd
        self.find(MobileBy.XPATH, '//*[@text="请输入公司地址，例如“腾讯大厦”"]').send_keys(address)
        self.find(MobileBy.XPATH, '//*[@text="腾讯大厦"]/../../..//*[@resource-id="com.tencent.wework:id/h5i"]').click()
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()
        return ManuallyAdd(self._driver)
