from base.base_01 import Base
from page.page_elements import PageElements
import allure


class HomePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title="点击首页的'我'按钮")
    def click_home_my_btn(self):
        """首页点击'我的'"""
        self.click_element(PageElements.home_my_btn_id)

    def close_update_window(self):
        self.click_element(PageElements.close_updata_id)
