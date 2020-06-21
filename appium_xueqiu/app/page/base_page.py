from appium.webdriver.webdriver import WebDriver
from appium_xueqiu.app.page.wrapper import handle_black
from appium.webdriver import WebElement
import yaml
import inspect
import json
import time
import os


class BasePage:
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def screenshot(self, file_path: str = None):
        if file_path is None:
            project_path = os.getcwd()
            file_path = project_path + "/image/"
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            image_name = int(time.time())
            file_path = file_path + str(image_name) + '.png'
        self._driver.save_screenshot(file_path)
        return file_path

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def finds(self, locator, value: str = None):
        element: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace(f'${{{key}}}', value)
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    self.find(step["by"], step["locator"]).click()
                elif action == "send_keys":
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                elif action == "len > 0":
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0
