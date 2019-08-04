from base.base_01 import Base
from page.page_elements import PageElements
import allure


class SettingPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title="退出登录操作")
    def login_out(self):
        """退出登录"""
        self.swipe_screen(1)  # 屏幕上划
        allure.attach("点击退出登录按钮", "")
        self.click_element(PageElements.setting_logout_btn_id)  # 点击退出登录
        allure.attach("点击退出登录弹窗的确定按钮", "")
        self.click_element(PageElements.setting_confirm_logout_btn_id)  # 点击确定退出
