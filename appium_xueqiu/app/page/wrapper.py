from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args, **kwargs):
        from appium_xueqiu.app.page.base_page import BasePage
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        _max_num = 3
        _error_num = 0
        self: BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            _error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = self.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper
