from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import data

# ----- Main Page Class -----
class UrbanRoutesPage:
	URBAN_ROUTES_URL = data.URBAN_ROUTES_URL
	FROM_INPUT = (By.ID, "from") # 'From' input only takes 'East 2nd Street, 601'
	TO_INPUT = (By.ID, "to") # 'To' input only takes '1300 1st St'
	CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and text()='Call a taxi']")

	MODAL_CLOSE = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
	MODAL = (By.XPATH, "//div[contains(@class, 'modal')]")

	# Finds the div with the class 'tcard-title' that contains the text "Supportive"
	SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(@class, 'tcard-title') and .='Supportive']")
	SELECTED_SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(@class, 'tcard') and contains(@class, 'active')][.//div[text()='Supportive']]")

	PHONE_NUMBER_LINK = (By.XPATH, "//div[contains(@class, 'np-text') and contains(text(), 'Phone number')]")
	PHONE_NUMBER_INPUT = (By.ID, "phone")
	PHONE_NUMBER_NEXT_BUTTON = (By.CSS_SELECTOR, "button.button.full")

	PHONE_CODE_INPUT = (By.ID, "code")
	PHONE_CODE_SUBMIT = (By.XPATH, "//button[contains(text(), 'Confirm')]")

	ADD_PAYMENT_BUTTON = (By.XPATH, "//div[contains(@class, 'pp-text') and contains(text(),'Payment method')]")
	ADD_CARD_BUTTON = (By.XPATH, "//div[contains(@class, 'pp-title') and contains(text(), 'Add card')]")

	CARD_NUMBER_INPUT = (By.ID, "number")
	CARD_CODE_INPUT = (By.XPATH, "//input[@id='code' and contains(@class, 'card-input')]")
	CARD_LINK_BUTTON = (By.XPATH, "//button[contains(text(), 'Link')]")

	COMMENT_INPUT = (By.ID, "comment")

	BLANKET_AND_HANDKERCHIEFS_DOM = (By.XPATH, "//div[@class='r-sw-label' and contains(text(), 'Blanket and handkerchiefs')]/following-sibling::div[@class='r-sw']//span")
	BLANKET_AND_HANDKERCHIEFS_SWITCH = (By.XPATH, "//div[@class='r-sw-label' and contains(text(), 'Blanket and handkerchiefs')]/following-sibling::div[@class='r-sw']//input")

	ICE_CREAM_PLUS = (By.XPATH, "//div[text()='Ice cream']/following-sibling::div[@class='r-counter']//div[@class='counter-plus']")
	ICE_CREAM_VALUE = (By.XPATH, "//div[text()='Ice cream']/following-sibling::div[@class='r-counter']//div[@class='counter-value']")

	ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
	CAR_SEARCH_MODEL = (By.CLASS_NAME, "order-body")

	# ----- FUNCTIONS -----
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 5)

	# Open Page
	def open_page(self):
		self.driver.get(self.URBAN_ROUTES_URL)

	# Enter 'from' address into from_address field
	def enter_from_address(self, from_address):
		self.driver.find_element(*self.FROM_INPUT).send_keys(from_address)

	# Enter 'to' address into to_address field
	def enter_to_address(self, to_address):
		self.driver.find_element(*self.TO_INPUT).send_keys(to_address)

	# Click the taxi button to proceed to order ride
	def click_taxi_button(self):
		self.wait.until(EC.visibility_of_element_located(self.CALL_TAXI_BUTTON)).click()

	# Enter from and to addresses, click taxi button
	def set_route(self, from_address, to_address):
		self.enter_from_address(from_address)
		self.enter_to_address(to_address)
		self.click_taxi_button()

	# Select tariff/plan
	def select_plan(self):
		self.wait.until(EC.element_to_be_clickable(self.SUPPORTIVE_PLAN)).click()

	# Fill phone number
	def fill_phone_number(self, phone_number):
		self.wait.until(EC.visibility_of_element_located(self.PHONE_NUMBER_LINK)).click()
		self.wait.until(EC.visibility_of_element_located(self.PHONE_NUMBER_INPUT)).send_keys(phone_number)
		self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()

	# Enter confirmation code
	def enter_confirmation_code(self, code):
		# Wait for phone code field visibility to enter the code
		self.wait.until(EC.visibility_of_element_located(self.PHONE_CODE_INPUT)).send_keys(code)
		# Find and click submit button
		self.driver.find_element(*self.PHONE_CODE_SUBMIT).click()

	# Fill payment card
	def fill_card(self, card_number, card_code):
		# Click the button to open the payment method section
		self.driver.find_element(*self.ADD_PAYMENT_BUTTON).click()
		# Wait for the "Add card" button to appear and click it
		self.wait.until(EC.element_to_be_clickable(self.ADD_CARD_BUTTON)).click()
		# Wait for card input to appear and send number
		self.wait.until(EC.visibility_of_element_located(self.CARD_NUMBER_INPUT)).send_keys(card_number)
		self.wait.until(EC.visibility_of_element_located(self.CARD_CODE_INPUT)).send_keys(card_code)
		# Click the 'Link' button to submit the card
		self.driver.find_element(*self.CARD_LINK_BUTTON).click()
		# Click X to close the modal
		self.wait.until(EC.element_to_be_clickable(self.MODAL_CLOSE)).click()

	# Leave driver comment
	def comment_for_driver(self):
		self.wait.until(EC.presence_of_element_located(self.COMMENT_INPUT)).send_keys(data.MESSAGE_FOR_DRIVER)

	# Order the blanket and handkerchiefs option
	def order_blanket_and_handkerchiefs(self):
		self.wait.until(EC.element_to_be_clickable(self.BLANKET_AND_HANDKERCHIEFS_DOM)).click()

	# Order 2 ice creams
	def order_ice_creams(self, quantity: int):
		plus_button = self.wait.until(EC.element_to_be_clickable(self.ICE_CREAM_PLUS))
		for _ in range(quantity):
			plus_button.click()

	# Retrieve the number of ice creams selected and convert to integer
	def get_ice_cream_value(self):
		value_element = self.wait.until(EC.visibility_of_element_located(self.ICE_CREAM_VALUE))
		return int(value_element.text)

	# Click the final order button
	def click_final_order(self):
		self.driver.find_element(*self.ORDER_BUTTON).click()

	# Car search modal appears
	def car_search_model_appears(self):
		self.wait.until(EC.visibility_of_element_located(self.CAR_SEARCH_MODEL))