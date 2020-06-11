from app.page.addmember_page import AddMember
from app.page.base_page import BasePage


class AddressList(BasePage):

    def add_member(self):
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return AddMember(self._driver)
