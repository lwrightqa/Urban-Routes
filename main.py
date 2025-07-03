from datetime import time
import data
import helpers
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage
from selenium import webdriver

class TestUrbanRoutes:
    # Setup Class
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Helpers from S7
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

        # My additions
        cls.driver.maximize_window()
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    # Setting addresses for route
    def test_set_route(self):
        self.routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

    # Selecting 'Supportive' plan
    def test_select_plan(self):
        # Perform the action.
        self.routes_page.select_plan()
        self.routes_page.check_for_plan()

    # Click and fill in the phone number model
    def test_fill_phone_number(self):
        # Fill in phone number and click next
        self.routes_page.fill_phone_number(data.PHONE_NUMBER)
        # Get confirmation code
        confirmation_code = retrieve_phone_code(self.driver)
        # Print confirmation code
        print(f"\nRetrieved code: {confirmation_code}")
        # Delegate the action to the page object
        self.routes_page.enter_confirmation_code(confirmation_code)

    # Click and fill in payment details
    def test_fill_card(self):
        self.routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)

    # Leave a comment for the driver
    def test_comment_for_driver(self):
        self.routes_page.comment_for_driver()
        sent_comment = self.driver.find_element(*self.routes_page.COMMENT_INPUT).get_attribute("value")
        assert sent_comment == "I need a quiet ride, please."

    # Request blanket and handkerchiefs option
    def test_order_blanket_and_handkerchiefs(self):
        self.routes_page.order_blanket_and_handkerchiefs()
        assert self.driver.find_element(*self.routes_page.BLANKET_AND_HANDKERCHIEFS_SWITCH).is_selected()

    # Order 2 Ice creams
    def test_order_2_ice_creams(self):
        self.routes_page.order_ice_creams(2)
        assert self.routes_page.get_ice_cream_value() == 2

    # Click button to search car models
    def test_car_search_model_appears(self):
        pass # Add later

    # Teardown Class
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()