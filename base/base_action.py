from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 根据特征找元素，属于base
    def find_element(self, feature):
        return WebDriverWait(self.driver, 20, 1).until(lambda x: x.find_element(*feature))

    # 根据特征找元素，属于base
    def find_elements(self, feature):
        return WebDriverWait(self.driver, 20, 1).until(lambda x: x.find_element(*feature))

    # 根据特征和内容输入，属于base
    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def click(self, feature):
        self.find_element(feature).click()
