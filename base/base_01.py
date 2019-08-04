from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time, os, allure


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元组(元素的定位类型, 定位类型的属性值)
        :param timeout: 等待时长
        :param poll_frequency: 检测时间间隔
        :return: 返回定位元素对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元组(元素的定位类型, 定位类型的属性值)
        :param timeout: 等待时长
        :param poll_frequency: 检测时间间隔
        :return: 返回定位元素对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=10, poll_frequency=1.0):
        """
        点击元素
        :param loc: 元组(元素的定位类型, 定位类型的属性值)
        :param timeout: 等待时长
        :param poll_frequency: 检测时间间隔
        :return:
        """
        self.get_element(loc, timeout, poll_frequency).click()

    def send_msg(self, loc, msg, timeout=10, poll_frequency=1.0):
        """
        给输入框输入内容
        :param loc: 元组(元素的定位类型, 定位类型的属性值)
        :param msg: 输入框输入的内容
        :param timeout: 等待时长
        :param poll_frequency: 检测时间间隔
        :return:
        """
        self.get_element(loc, timeout, poll_frequency).clear()
        self.get_element(loc, timeout, poll_frequency).send_keys(msg)

    @allure.step(title="滑动屏幕")
    def swipe_screen(self, tag):
        """
        滑动屏幕
        :param option: 1: 向上滑动 2:向下滑动 3.向左滑动 4.向右滑动
        :return:
        """
        time.sleep(2)
        screen = self.driver.get_window_size()
        width = screen.get("width")
        height = screen.get("height")

        if tag == 1:
            allure.attach("向上滑动", "")
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3)
        if tag == 2:
            allure.attach("向下滑动", "")
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8)
        if tag == 3:
            allure.attach("向左滑动", "")
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5)
        if tag == 4:
            allure.attach("向右滑动", "")
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5)

    @allure.step(title="获取toast消息")
    def get_toast_msg(self, toast):
        """
        获取toast消息
        :param toast:toast消息文本
        :return:
        """
        msg_path = (By.XPATH, "//*[contains(@text, '{}')]".format(toast))
        msg = self.get_element(msg_path, timeout=3, poll_frequency=0.5).text
        allure.attach("获取到的toast消息:", msg)
        return msg

    @allure.step(title="截图操作")
    def get_screenshot(self):
        image_name = "./image" + os.sep + "{}.png".format(time.time())
        self.driver.get_screenshot_as_file(image_name)
        with open(image_name, "rb") as f:
            allure.attach(image_name, f.read(), allure.attach_type.PNG)
