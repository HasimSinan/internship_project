from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("Click on Community option.")
def click_to_community(context):
    context.app.settings_page.click_community()