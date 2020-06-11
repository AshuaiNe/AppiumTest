from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class TestBrowser:
    def setup(self):

        des_caps = {
            "platformName": "android",
            "platformVersion": "6.0.1",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            # "browserName": "browser",
            "noReset": True,
            "deviceName": "192.168.15.102:5555",
            "chromedriverExecutable": "D:/driver/chromedriver44/chromedriver.exe"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.XPATH, '//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phonenumber_locator = (By.ID, "phone-number")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(phonenumber_locator))
        self.driver.find_element(*phonenumber_locator).send_keys("15000358178")
        self.driver.find_element(MobileBy.ID, "code").send_keys("1234")
        self.driver.find_element(MobileBy.CSS_SELECTOR, "body > div > div > div.form-wrap > div > div.btn-submit").click()
