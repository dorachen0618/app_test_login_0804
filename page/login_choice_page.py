from base.base_01 import Base
from page.page_elements import PageElements
import allure


class LoginChoicePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title="点击'已有账号去登陆'")
    def click_exits_account_login(self):
        """点击'已有账号,去登陆' """
        self.click_element(PageElements.exits_account_login_id)
