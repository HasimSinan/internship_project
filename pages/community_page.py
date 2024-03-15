from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class CommunityPage(Page):
    JOIN_PRO = (By.CSS_SELECTOR, ".pro-button[wized='proButton']")
    CONTACT_SUPPORT_BTN = (By.CSS_SELECTOR, ".chat-button[href*='reelly_dubai_bot?start']")

    def verify_community_url(self):
        self.wait_element_presence(*self.JOIN_PRO)
        self.verify_url('https://soft.reelly.io/community')

    def verify_support_clickable(self):
        self.wait_element_clickable(*self.CONTACT_SUPPORT_BTN)
