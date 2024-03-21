from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Filter the products by want to buy.')
def verify_secondary_url_opens(context):
    context.app.secondary_page.filter_by_want_buy()


@then('Verify the secondary page opens.')
def verify_secondary_url_opens(context):
    context.app.secondary_page.verify_secondary_url()


@then('Verify all cards have “want to buy” tag.')
def verify_want_to_buy_tag(context):
    context.app.secondary_page.verify_wtb_tag2()
