# Urban Routes UI Automation Project

This project contains an automated UI testing suite for the "Urban Routes" web application. It is built with Python and utilizes the Selenium WebDriver framework to simulate a user's journey of ordering a taxi.

The tests follow the Page Object Model (POM) design pattern for better maintainability, readability, and separation of concerns.

## ⚠️ Important Note

The target web application for this testing suite, "Urban Routes," was a proprietary, temporary environment used for educational purposes. As a result, the URL is no longer active, and these tests **cannot be run** by cloning the repository.

This project serves as a portfolio piece to demonstrate skills in:

- UI test automation using Python and Selenium.
- Implementation of the Page Object Model (POM) design pattern.
- Test suite organization with Pytest.
- Handling dynamic web elements and asynchronous operations.

## Features Tested

The test suite covers the end-to-end user flow for ordering a ride, including:

- Setting 'From' and 'To' addresses for the route.
- Selecting a specific service plan ('Supportive').
- Entering a phone number and verifying it with a confirmation code retrieved from browser logs.
- Adding a credit card as a payment method.
- Leaving a custom message for the driver.
- Requesting extra services (Blanket and handkerchiefs).
- Ordering a specific quantity of an item (Ice cream).
- Initiating the final order and verifying that the car search modal appears.

## Technologies Used

- **Python**: The core programming language.
- **Selenium WebDriver**: For browser automation and UI interaction.
- **Pytest**: As the testing framework for test discovery, execution, and assertions.

## Project Structure

The project is organized to promote modularity and separation of concerns:

- `tests/test_urban_routes.py`: Contains the test class and methods that define the test steps and assertions. It orchestrates the calls to the page object methods.
- `urban_routes.py`: Implements the Page Object for the application. It encapsulates all the web element locators and the methods that interact with them.
- `data.py`: Stores all test data and constants, such as URLs, addresses, and credentials, keeping them separate from the test logic.
- `helpers.py`: Provides utility functions, such as the function to retrieve the phone confirmation code from browser performance logs.
- `requirements.txt`: Lists the necessary Python packages for the project.