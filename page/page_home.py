from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PageHome(BaseAction):

    search_file_text = By.ID, "kw"
    search_button = By.ID, "su"

    def input_search(self, text):
        self.input(self.search_file_text, text)

    def click_search(self):
        self.click(self.search_button)