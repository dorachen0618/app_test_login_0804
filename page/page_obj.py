from page.home_page import HomePage
from page.person_page import PersonPage
from page.login_choice_page import LoginChoicePage
from page.login_page import LoginPage
from page.setting_page import SettingPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        """返回首页的页面对象"""
        return HomePage(self.driver)

    def get_person_page(self):
        """返回个人中心的页面对象"""
        return PersonPage(self.driver)

    def get_login_choice_page(self):
        """返回登录选择的页面对象"""
        return LoginChoicePage(self.driver)

    def get_login_page(self):
        """返回登录的页面对象"""
        return LoginPage(self.driver)

    def get_setting_page(self):
        """返回设置的页面对象"""
        return SettingPage(self.driver)
