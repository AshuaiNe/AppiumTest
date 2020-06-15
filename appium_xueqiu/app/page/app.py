from appium_xueqiu.app.page.main import Main
from appium_xueqiu.app.page.base_page import BasePage
from appium import webdriver


class App(BasePage):

    def start(self):
        if self._driver is None:
            des_caps = {
                "platformName": "android",
                "platformVersion": "6.0.1",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": True,
                "deviceName": "127.0.0.1:7555",
            }
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
