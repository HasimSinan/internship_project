from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainMenu(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, ".menu-button-block[href='/settings']")

    def click_settings(self):
        self.wait_element_clickable_click(*self.SETTINGS_BTN)
