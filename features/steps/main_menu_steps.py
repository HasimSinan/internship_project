from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("Click on settings option.")
def click_to_settings(context):
    context.app.main_menu.click_settings()


@when("Click on secondary option.")
def click_to_secondary(context):
    context.app.main_menu.click_secondary()