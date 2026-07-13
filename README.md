# Sauce Demo Login Automation

A small test automation project built with Python, Selenium, and Pytest. It automates logging into the Sauce Demo web app and verifies successful and failed login scenarios using the Page Object Model (POM) pattern.

## What this project demonstrates

- Python OOP (classes, inheritance) applied to test automation
- Page Object Model structure, separating page logic from test logic
- Selenium WebDriver for real browser automation
- Pytest fixtures for reusable browser setup and teardown
- Positive and negative test assertions

## Project structure

pages/
    base_driver.py   - Base class with shared browser actions
    login_page.py    - Login page object and login logic
tests/
    test_login.py    - Test cases for login functionality
requirements.txt

## How to run

1. Install dependencies:

   pip3 install -r requirements.txt

2. Run the tests:

   python3 -m pytest tests/test_login.py -v

## Tests included

- Successful login with valid credentials
- Failed login with an incorrect password

## Author

Obed — QA Engineer building toward AI-augmented test automation.