from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the main page.')
def open_signin(context):
    context.app.sign_in_page.open_sign_in()


@when('Log in to the page.')
def log_in_page(context):
    context.app.sign_in_page.enter_valid_email()
    context.app.sign_in_page.enter_valid_password()
    context.app.sign_in_page.click_continue()



