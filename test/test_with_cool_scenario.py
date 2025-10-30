import pytest
import allure
from allure_commons.reporter import AllureReporter
from allure_pytest.listener import AllureListener

# Mock functions simulating application logic
def login(username, password):
    if username == "test_user" and password == "Test1234!":
        return {"status": "success", "token": "mock_token"}
    return {"status": "failure", "message": "Invalid credentials"}


def search_product(query):
    if query == "Test Product":
        return [{"id": 1, "name": "Test Product", "price": 100}]
    return []


def add_to_cart(product_id, quantity):
    if product_id == 1 and quantity > 0:
        return {"status": "success", "cart": [{"id": 1, "name": "Test Product", "quantity": quantity, "price": 100}]}
    return {"status": "failure", "message": "Product not available"}


def checkout(cart, customer_data):
    if cart and customer_data.get("name") and customer_data.get("payment_method"):
        return {"status": "success", "order_id": 12345}
    return {"status": "failure", "message": "Invalid checkout details"}


@allure.feature("Order Checkout")
@allure.label("priority", "Medium")
@allure.story("Successful order placement with valid data")
def test_order_checkout():
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
        login_response = login(username, password)
        assert login_response["status"] == "success", "Login failed"
        allure.attach(str(login_response), name="Login Response", attachment_type=allure.attachment_type.JSON)

    with allure.step("Search for the product"):
        products = search_product(search_query)
        assert len(products) > 0, "No products found"
        product = products[0]
        allure.attach(str(products), name="Search Results", attachment_type=allure.attachment_type.JSON)

    with allure.step("Add the product to the cart"):
        cart_response = add_to_cart(product["id"], 1)
        assert cart_response["status"] == "success", "Adding to cart failed"
        cart = cart_response["cart"]
        assert len(cart) > 0, "Cart is empty"
        allure.attach(str(cart), name="Cart Contents", attachment_type=allure.attachment_type.JSON)

    with allure.step("Proceed to checkout and place the order"):
        checkout_response = checkout(cart, customer_data)
        assert checkout_response["status"] == "success", "Checkout failed"
        assert "order_id" in checkout_response, "Order ID missing in response"
        allure.attach(str(checkout_response), name="Checkout Response", attachment_type=allure.attachment_type.JSON)



@allure.id(295)
@allure.feature("Google search")
@allure.label("priority", "Low")
@allure.label("owner", "Ольга Ч")
@allure.title("Поиск катринки с квоккой")
def test_poisk_katrinki_s_kvokkoj():
    with allure.step("Найти поисковую строку на главной странице ya.ru"):
        with allure.step("Attachment [87]"):
            pass
        pass

    with allure.step("Ввести текст \"Квокка фото\""):
        pass

    with allure.step("На клавиатуре нажать \"Enter\""):
        pass
    pass

