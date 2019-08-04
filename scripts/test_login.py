import sys, os, time

sys.path.append(os.getcwd())

from selenium.common.exceptions import TimeoutException
import pytest
from base.get_driver import get_android_driver
from page.page_obj import Page
from base.get_file_data import get_file_data
from page.page_elements import PageElements


def get_login_data():
    data = get_file_data("login_data.yml")
    suc_data = []
    fail_data = []
    for i in data.keys():
        if data.get(i).get("toast"):  # toast的值不为空, 则是登录失败的数据
            fail_data.append(
                (
                    i, data.get(i).get("username"), data.get(i).get("passwd"),
                    data.get(i).get("toast"), data.get(i).get("expect_data"),
                )
            )

        else:
            suc_data.append(
                (
                    i, data.get(i).get("username"), data.get(i).get("passwd"), data.get(i).get("expect_data"),
                )
            )
    return {"success": suc_data, "fail": fail_data}


class TestLogin:
    def setup_class(self):
        self.driver = get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page_obj = Page(self.driver)
        self.page_obj.get_home_page().close_update_window()

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def go_to_login_page(self):
        time.sleep(2)
        self.page_obj.get_home_page().click_home_my_btn()
        self.page_obj.get_login_choice_page().click_exits_account_login()

    @pytest.mark.parametrize("case_num, username, passwd, expect_data", get_login_data().get("success"))
    def test_login_suc(self, case_num, username, passwd, expect_data):
        self.page_obj.get_login_page().login(username, passwd)
        try:
            collection_txt = self.page_obj.get_person_page().get_my_collection_text()
            try:
                assert expect_data in collection_txt
            except AssertionError:
                self.page_obj.get_person_page().get_screenshot()
                assert False
            finally:
                self.page_obj.get_person_page().click_setting_btn()
                self.page_obj.get_setting_page().login_out()
        except TimeoutException:
            self.page_obj.get_person_page().get_screenshot()
            self.page_obj.get_login_page().close_login_page_btn()
            assert False

    @pytest.mark.parametrize("case_num, username, passwd, toast, expect_data", get_login_data().get("fail"))
    def test_login_fail(self, case_num, username, passwd, toast, expect_data):
        self.page_obj.get_login_page().login(username, passwd)  # 登录
        try:
            # 判断toast消息是否存在
            toast_msg = self.page_obj.get_login_page().get_toast_msg(toast)
            try:
                # 断言toast消息
                assert toast_msg == expect_data
            except AssertionError:
                self.page_obj.get_login_page().get_screenshot()
                assert False

        except TimeoutException:
            """toast消息不存在"""
            # 截图
            self.page_obj.get_login_page().get_screenshot()
            assert False

        finally:
            try:
                # 判断登录按钮是否存在, 若存在, 关闭登录页面
                self.page_obj.get_login_page().get_element(PageElements.login_btn_id)
                self.page_obj.get_login_page().close_login_page_btn()
            except TimeoutException:
                """登录按钮不存在,进入设置, 退出登录"""
                self.page_obj.get_person_page().click_setting_btn()
                self.page_obj.get_setting_page().login_out()
                assert False






