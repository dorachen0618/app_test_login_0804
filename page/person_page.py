from base.base_01 import Base
from page.page_elements import PageElements
import allure


class PersonPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title="获取'我的收藏'文本内容")
    def get_my_collection_text(self):
        """获取'我的收藏'文本 """
        text = self.get_element(PageElements.my_collection_id).text
        # print(text)
        allure.attach("获取的文本:", text)
        return text

    @allure.step(title="点击个人中心的设置按钮")
    def click_setting_btn(self):
        """点击设置按钮"""
        self.click_element(PageElements.person_setting_btn_id)

