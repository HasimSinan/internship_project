from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainMenu(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, ".menu-button-block[href='/settings']")
    SECONDARY_BTN = (By.CSS_SELECTOR, ".menu-button-block[href='/secondary-listings']")

    def click_settings(self):
        # sleep(3)
        self.wait_element_clickable_click(*self.SETTINGS_BTN)

    def click_secondary(self):
        self.wait_element_clickable_click(*self.SECONDARY_BTN)
