import pytest
import allure
from allure import attachment_type

@allure.epic("Allure TestOps")
@allure.feature("Google search")
@allure.story("The cutest animal")
@allure.label("priority", "High")

def test_passed():
    pass

@allure.label("priority", "Low")
def test_failed():
    assert False, "Some fail reason"

@allure.label("priority", "Low")
def test_broken():
    var = 1 / 0
    assert var

@allure.label("priority", "Medium")
@pytest.mark.skip(reason="Some skip reason")
def test_skipped():
    pass

@allure.label("priority", "Low")
@pytest.mark.xfail(reason="Some xfail reason")
def test_xfail():
    assert False, "Assertion failed"

@allure.label("priority", "Medium")
@pytest.mark.xfail(reason="Test doesn't fail")
def test_xpass():
    pass
