import pytest
import requests
import allure
from allure_commons.reporter import AllureReporter
from allure_pytest.listener import AllureListener

@pytest.fixture
def api_session():
    """Fixture to provide a session for making requests."""
    session = requests.Session()
    yield session
    session.close()


@allure.feature("Order Checkout")
@allure.story("Successful order placement with valid data")
def test_order_checkout(api_session):
    # Constants and test data
    base_url = "https://example.com/api"  # Replace with your API base URL
    login_endpoint = f"{base_url}/login"
    search_endpoint = f"{base_url}/products/search"
    cart_endpoint = f"{base_url}/cart"
    checkout_endpoint = f"{base_url}/checkout"

    username = "test_user"
    password = "Test1234!"
    search_query = "Test Product"
    customer_data = {
        "name": "Иван Иванов",
        "phone": "+7 900 123-45-67",
        "address": "Москва, ул. Тестовая, д.1, кв.1",
        "email": "test@example.com",
        "payment_method": "card",
    }

    with allure.step("Log in to the application"):
        login_payload = {"username": username, "password": password}
        response = api_session.post(login_endpoint, json=login_payload)
        assert response.status_code == 200, "Login failed"
        token = response.json().get("token")
        assert token, "Authentication token not received"
        api_session.headers.update({"Authorization": f"Bearer {token}"})
        allure.attach(str(response.json()), name="Login Response", attachment_type=allure.attachment_type.JSON)

    with allure.step("Search for the product"):
        search_params = {"query": search_query}
        response = api_session.get(search_endpoint, params=search_params)
        assert response.status_code == 200, "Product search failed"
        products = response.json().get("products", [])
        assert products, "No products found"
        product_id = products[0]["id"]
        allure.attach(str(response.json()), name="Search Response", attachment_type=allure.attachment_type.JSON)

    with allure.step("Add the product to the cart"):
        cart_payload = {"product_id": product_id, "quantity": 1}
        response = api_session.post(cart_endpoint, json=cart_payload)
        assert response.status_code == 200, "Adding to cart failed"
        cart = response.json().get("cart", {})
        assert len(cart.get("items", [])) > 0, "Cart is empty"
        allure.attach(str(response.json()), name="Cart Response", attachment_type=allure.attachment_type.JSON)

    with allure.step("Proceed to checkout and place the order"):
        checkout_payload = {"customer": customer_data}
        response = api_session.post(checkout_endpoint, json=checkout_payload)
        assert response.status_code == 200, "Checkout failed"
        order_confirmation = response.json()
        assert "order_id" in order_confirmation, "Order confirmation missing order_id"
        allure.attach(str(response.json()), name="Checkout Response", attachment_type=allure.attachment_type.JSON)

