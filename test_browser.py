from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestBrowser:
    def setup(self):

        des_caps = {
            "platformName": "android",
            "platformVersion": "6.0.1",
            "browserName": "Browser",
            "noReset": True,
            "deviceName": "127.0.0.1:7555",
            "chromedriverExecutable": "D:/driver/chromedriver52/chromedriver.exe"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        search_locator = (By.ID, "index-bn")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()
