from appium_watch.app.page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ManuallyAdd(BasePage):
    def input_name(self, name):
        self.find(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys(name)
        return self

    def set_gender(self):
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[contains(@class, "TextView") and @text="男"]').click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_phonenumber(self, phonenumber):
        self.find(MobileBy.XPATH, '//*[@text="手机　"]/..//*[@class="android.widget.EditText"]').send_keys(phonenumber)
        return self

    def goto_address(self):
        from app.page.address_page import AddressPage
        self.find(MobileBy.XPATH, '//*[@text="地址"]/..//*[@class="android.widget.LinearLayout"]').click()
        return AddressPage(self._driver)

    def click_save(self):
        from app.page.addmember_page import AddMember
        locator = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gyt"]')
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.find(*locator).click()
        return AddMember(self._driver)
