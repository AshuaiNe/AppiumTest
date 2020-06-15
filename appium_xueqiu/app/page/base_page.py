from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium_xueqiu.app.page.wrapper import handle_black
from appium.webdriver import WebElement


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            elements = self._driver.find_element(*locator)
        else:
            elements = self._driver.find_element(locator, value)
        return elements

    def finds(self, locator, value: str = None):
        element: list
        if isinstance(locator, tuple):
            element = self._driver.find_elements(*locator)
        else:
            element = self._driver.find_elements(locator, value)
        return element
