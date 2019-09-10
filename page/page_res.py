from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PageRes(BaseAction):

    res_image = By.ID, "xgoflr"

    def click_res(self):
        self.click(self.res_image)






