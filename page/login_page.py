from base.base_01 import Base
from page.page_elements import PageElements
import allure


class LoginPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title="登录操作")
    def login(self, username, pwd):
        """登录"""
        allure.attach("输入用户名和密码", "用户名:{}, 密码:{}".format(username, pwd))
        self.send_msg(PageElements.login_name_id, username)  # 输入用户名
        self.send_msg(PageElements.login_passwd_id, pwd)  # 输入密码
        allure.attach("点击登录按钮", "")
        self.click_element(PageElements.login_btn_id)  # 点击登录按钮

    @allure.step(title="关闭登录页面")
    def close_login_page_btn(self):
        """关闭登录页面"""
        self.click_element(PageElements.login_close_page_btn_id)
