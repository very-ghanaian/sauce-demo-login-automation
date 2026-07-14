import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

def test_failed_login_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to("https://www.saucedemo.com")
    login_page.login("standard_user", "wrong_password")

    assert "inventory.html" not in driver.current_url

def test_locked_out_user_cannot_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to("https://www.saucedemo.com")
    login_page.login("locked_out_user", "secret_sauce")

    assert "inventory.html" not in driver.current_url