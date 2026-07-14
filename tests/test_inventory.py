from selenium import webdriver
from pages.base_driver import BaseDriver
import pytest
from pages.login_page import LoginPage
from pages.Inventory import InventoryPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_backpack_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.go_to("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()   

    assert inventory_page.go_to_cart() == "1"