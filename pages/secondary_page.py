from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SecondaryPage(Page):
    FILTER_BTN = (By.CSS_SELECTOR, ".filter-button")
    WANT_TO_BUY_FLTR = (By.CSS_SELECTOR, ".switcher-button[wized='ListingTypeBuy']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "[wized= 'applyFilterButtonMLS']")
    LISTING_CARDS = (By.CSS_SELECTOR, "[wized= 'listingCardMLS']")
    WANT_TO_BUY_TAG = (By.CSS_SELECTOR, ".for-sale-block")
    NEXT_PAGE_BTN = (By.CSS_SELECTOR, "[wized= 'nextPageMLS']")
    UNIT_DESCRIPTION = (By.CSS_SELECTOR, "[wized= 'unitDescriptionMLS']")
    LISTING_COUNTER = (By.CSS_SELECTOR, "[wized= 'publisherProfileImageMLS']")
    WHATSAPP_BUTTON = (By.CSS_SELECTOR, "[wized= 'whatsAppButtonMLS']")

    def verify_secondary_url(self):
        self.wait_element_presence(*self.FILTER_BTN)
        self.verify_url('https://soft.reelly.io/secondary-listings')

    def filter_by_want_buy(self):
        sleep(2)
        self.wait_element_clickable_click(*self.FILTER_BTN)
        self.wait_element_clickable_click(*self.WANT_TO_BUY_FLTR)
        self.wait_element_clickable_click(*self.APPLY_FILTER_BTN)

    def verify_wtb_tag(self):
        listing_block = self.find_elements(*self.LISTING_CARDS)
        tag = self.find_elements(*self.WANT_TO_BUY_TAG)
        assert len(listing_block) == len(tag), f'Number of listing blocks does not match number of tags'

    def verify_wtb_tag2(self):

        for x in range(0,4):
            # self.wait_element_clickable(*self.NEXT_PAGE_BTN)
            listing_block = self.find_elements(*self.LISTING_CARDS)
            tag = self.find_elements(*self.WANT_TO_BUY_TAG)
            assert len(listing_block) == len(tag), f'Number of listing blocks does not match number of tags for page'
            print(listing_block)
            self.wait_element_clickable_click(*self.NEXT_PAGE_BTN)
            sleep(5)


