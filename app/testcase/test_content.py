from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from time import sleep


class TestBrowser:
    def setup(self):

        des_caps = {
            "platformName": "android",
            "platformVersion": "6.0.1",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": True,
            "deviceName": "127.0.0.1:7555",
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys("Python1")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[contains(@class, "TextView") and @text="男"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机　"]/..//*[@class="android.widget.EditText"]').send_keys("15000358191")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="地址"]/..//*[@class="android.widget.LinearLayout"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="请输入公司地址，例如“腾讯大厦”"]').send_keys("腾讯大厦")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="腾讯大厦"]/../../..//*[@resource-id="com.tencent.wework:id/h5i"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        locator = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gyt"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()
