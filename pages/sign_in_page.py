from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignIn(Page):
    USER_EMAIL = (By.CSS_SELECTOR, "#email-2")
    USER_PASSWORD = (By.CSS_SELECTOR, "#field")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def open_sign_in(self):
        self.open('https://soft.reelly.io/sign-in')

    def enter_valid_email(self):
        self.wait_element_clickable(*self.USER_EMAIL)
        self.input_text('hsinanm@gmail.com', *self.USER_EMAIL)

    def enter_valid_password(self):
        # self.wait_element_presence(*self.USER_PASSWORD)
        self.input_text('112233Hsm!', *self.USER_PASSWORD)

    def click_continue(self):
        self.wait_element_clickable_click(*self.CONTINUE_BTN)