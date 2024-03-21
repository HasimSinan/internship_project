from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f"Expected text '{expected_text}' does not match to '{actual_text}'"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f"Expected text '{expected_text}' not in '{actual_text}'"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected '{expected_url}' does not match '{actual_url}'"

    def verify_partial_url(self, expected_partial_url):
        # actual_url = self.driver.current_url
        # assert expected_partial_url in actual_url, f"Expected '{expected_partial_url}' is not in '{actual_url}'"
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f"Expected url '{expected_partial_url}' not found.")

    def wait_element_presence(self, *locator):
        self.wait.until(EC.presence_of_element_located(locator),
                        message=f'Element by {locator} not present')

    def wait_element_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f'Element by {locator} not clickable')

    def wait_element_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f'Element by {locator} not clickable').click()

    def wait_element_visible(self, *locator):
        self.wait.until(EC.visibility_of(locator),
                        message=f'Element by {locator} not visible')

    def wait_element_invisible(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator),
                        message=f'Element by {locator} still visible')

    def wait_text_in_element_present(self, *locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text),
                        message=f'Element by {locator} still visible')

    def wait_elements_presence(self, *locator):
        self.wait.until(EC.presence_of_all_elements_located(locator),
                        message=f'Element by {locator} not present')
