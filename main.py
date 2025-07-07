import data
import helpers
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestUrbanRoutes:
    # Setup Class
    @classmethod
    def setup_class(cls):
        # Additional logging enabled to retrieve phone confirmation code
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
        cls.routes = UrbanRoutesPage(cls.driver) # Shortened class to reduce typing

    # Setting addresses for route
    def test_set_route(self):
        self.routes.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        # Checking input text against expected results
        sent_from_input = self.driver.find_element(*self.routes.FROM_INPUT).get_attribute("value")
        sent_to_input = self.driver.find_element(*self.routes.TO_INPUT).get_attribute("value")
        assert sent_from_input == "East 2nd Street, 601"
        assert sent_to_input == "1300 1st St"

    # Selecting 'Supportive' plan
    def test_select_plan(self):
        # Select the plan
        self.routes.select_plan()
        # Ensure 'Supportive' plan is selected/highlighted.
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.routes.SELECTED_SUPPORTIVE_PLAN))
        print("\nSupportive plan selected")

    # Click and fill in the phone number model
    def test_fill_phone_number(self):
        # Click the button, fill in phone number and click next
        self.routes.fill_phone_number(data.PHONE_NUMBER)
        # Check that entered phone number matches expected entry
        sent_phone_number = self.driver.find_element(*self.routes.PHONE_NUMBER_INPUT).get_attribute("value")
        assert sent_phone_number == "+1 555 555 55 55"
        # Wait for confirmation code to generate
        time.sleep(3)
        # Get confirmation code
        confirmation_code = retrieve_phone_code(self.driver)
        # Print confirmation code
        print(f"\nRetrieved code: {confirmation_code}")
        # Delegate the action to the page object
        self.routes.enter_confirmation_code(confirmation_code)
        # Ensure confirmation code matches actual input
        sent_confirmation_code = self.driver.find_element(*self.routes.PHONE_CODE_INPUT).get_attribute("value")
        assert sent_confirmation_code == confirmation_code

    # Click and fill in payment details
    def test_fill_card(self):
        self.routes.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        # Ensure sent card number and card code match expected data
        sent_card_number = self.driver.find_element(*self.routes.CARD_NUMBER_INPUT).get_attribute("value")
        sent_card_code = self.driver.find_element(*self.routes.CARD_CODE_INPUT).get_attribute("value")
        assert sent_card_number == "1234 0000 4321"
        assert sent_card_code == "12"

    # Leave a comment for the driver
    def test_comment_for_driver(self):
        self.routes.comment_for_driver()
        # Assert sent comment matches input
        sent_comment = self.driver.find_element(*self.routes.COMMENT_INPUT).get_attribute("value")
        assert sent_comment == "I need a quiet ride, please."

    # Request blanket and handkerchiefs option
    def test_order_blanket_and_handkerchiefs(self):
        self.routes.order_blanket_and_handkerchiefs()
        # Ensure blanket and handkerchiefs option was selected
        assert self.driver.find_element(*self.routes.BLANKET_AND_HANDKERCHIEFS_SWITCH).is_selected()
        print("\nBlanket and handkerchiefs selected")

    # Order 2 Ice creams
    def test_order_2_ice_creams(self):
        self.routes.order_ice_creams(2)
        # Check that number of ice creams ordered matches input
        actual_ice_creams = self.routes.get_ice_cream_value()
        assert actual_ice_creams == 2

    # Click the button to search car models
    def test_car_search_model_appears(self):
        self.routes.click_final_order()
        # Ensuring modal appears (Note: sometimes it appears and disappears quickly so I'm not sure if I'm supposed to validate the contents of the modal.
        self.routes.car_search_model_appears()

    # Teardown Class
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()