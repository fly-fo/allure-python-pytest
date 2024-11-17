import json
import os

import allure
from allure import attachment_type
from allure_commons.types import Severity

@allure.epic("Allure TestOps")
@allure.feature("Attachments")
@allure.story("Add atachment")


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and configured
    driver.maximize_window()
    yield driver
    driver.quit()


def test_order_checkout(browser):
    # Constants and test data
    base_url = "https://example.com"  # Replace with your application URL
    username = "test_user"
    password = "Test1234!"
    search_query = "Test Product"
    customer_name = "Иван Иванов"
    phone = "+7 900 123-45-67"
    address = "Москва, ул. Тестовая, д.1, кв.1"
    email = "test@example.com"

    # Step 1: Log in to the application
    browser.get(f"{base_url}/login")
    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    # Verify login was successful
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "user-profile"))
    )

    # Step 2: Search for the product
    search_box = browser.find_element(By.ID, "search")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Verify product is displayed in search results
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-item"))
    )
    browser.find_element(By.CLASS_NAME, "product-item").click()

    # Step 3: Add the product to the cart
    browser.find_element(By.ID, "add-to-cart-button").click()

    # Verify product is added to the cart
    browser.get(f"{base_url}/cart")
    cart_items = browser.find_elements(By.CLASS_NAME, "cart-item")
    assert len(cart_items) > 0, "Cart is empty, but it should contain the added product."

    # Step 4: Proceed to checkout
    browser.find_element(By.ID, "checkout-button").click()

    # Verify checkout page is displayed
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "checkout-form"))
    )

    # Step 5: Fill out the checkout form
    browser.find_element(By.ID, "customer-name").send_keys(customer_name)
    browser.find_element(By.ID, "customer-phone").send_keys(phone)
    browser.find_element(By.ID, "customer-address").send_keys(address)
    browser.find_element(By.ID, "customer-email").send_keys(email)
    browser.find_element(By.ID, "payment-method-card").click()
    browser.find_element(By.ID, "confirm-order-button").click()

    # Verify order confirmation
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "order-confirmation"))
    )
    confirmation_message = browser.find_element(By.CLASS_NAME, "order-confirmation").text
    assert "Спасибо за ваш заказ" in confirmation_message, "Order confirmation not displayed."

