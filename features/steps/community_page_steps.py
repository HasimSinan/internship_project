from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Verify the right page opens.')
def verify_community_url_opens(context):
    context.app.community_page.verify_community_url()


@then('Verify “Contact support” button is available and clickable.')
def verify_community_url_opens(context):
    context.app.community_page.verify_support_clickable()