import time

from selenium import webdriver

from page.page_home import PageHome
from page.page_res import PageRes


class TestSearch:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.page = PageHome(self.driver)
        self.res = PageRes(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_search(self):

        self.page.input_search("10000")
        time.sleep(2)
        self.page.click_search()
        # time.sleep(2)
        # self.res.click_res()









