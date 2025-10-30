import allure
import pytest
from allure import attachment_type
from allure_commons.types import Severity

@allure.epic("Allure TestOps")
@allure.feature("Attachments")
@allure.story("Add atachment")
@allure.label("priority", "Medium")

@allure.title("Some title for test")
def test_with_title():
    pass


@allure.title("Test title with param {param}")
@pytest.mark.parametrize("param", ["first", "second"])
def test_with_dynamic_title(param):
    pass


@allure.title("Fixture title")
@pytest.fixture()
def titled_fixture():
    pass


def test_with_titled_fixture(titled_fixture):
    pass
