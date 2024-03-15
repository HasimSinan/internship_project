from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SettingsPage(Page):
    COMMUNITY_BTN = (By.CSS_SELECTOR, ".page-setting-block[href='/community']")

    def click_community(self):
        self.wait_element_clickable_click(*self.COMMUNITY_BTN)