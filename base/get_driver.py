from appium import webdriver


def get_android_driver(package, activity):
    """
    :param package: App包名
    :param activity: App启动名
    :return:
    """
    param = {}
    param["platformName"] = "Android"  # 测试平台
    param["platformVersion"] = "5.1"   # 测试设备的版本
    param["deviceName"] = "Samsung"    # 测试设备的名称-可随便写
    param["appPackage"] = package      # 启动的包
    param["appActivity"] = activity    # 启动的activity
    param["automationName"] = "Uiautomator2"    # 支持获取手机toast消息
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", param)
    return driver
