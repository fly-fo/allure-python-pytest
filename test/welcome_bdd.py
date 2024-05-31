from pathlib import Path
from pytest_bdd import scenario, when, then

import examples_allure_pytest_bdd


FEATURE_PATH = Path("features") / "welcome.feature"


@scenario(FEATURE_PATH, "Example of Allure Pytest-BDD")
def test_example_of_allure_pytest_bdd():
    pass


@when("calling examples_allure_pytest_bdd.get_message", target_fixture="message")
def call_get_message():
    return examples_allure_pytest_bdd.get_message()


@then("the greeting message with the project's name is created")
def assert_message(message):
    assert message == "Hello from examples.allure-pytest-bdd!"
