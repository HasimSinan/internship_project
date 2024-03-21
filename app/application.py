from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_in_page import SignIn
from pages.main_menu import MainMenu
from pages.settings_page import SettingsPage
from pages.community_page import CommunityPage
from pages.secondary_page import SecondaryPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignIn(driver)
        self.main_menu = MainMenu(driver)
        self.settings_page = SettingsPage(driver)
        self.community_page = CommunityPage(driver)
        self.secondary_page = SecondaryPage(driver)
