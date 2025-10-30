import unittest
import allure
import pytest
from allure import attachment_type
import pytest

@pytest.fixture(autouse=True)
def apply_priority_label():
    allure.dynamic.label("priority", "Medium")

@pytest.fixture(scope="module")
def setup_module():
    print("\n[Setup Module] Preparing resources for the fake test...")
    yield
    print("\n[Teardown Module] Cleaning up resources after the fake test...")

@pytest.fixture(scope="function")
def setup_function():
    print("\n[Setup Function] Setting up before a test...")
    yield
    print("\n[Teardown Function] Tidying up after a test...")

def test_step1(setup_module, setup_function):
    print("[Test Step 1] Performing test step 1...")
    assert True, "Step 1 passed"

def test_step2(setup_module, setup_function):
    print("[Test Step 2] Performing test step 2...")
    assert 1 + 1 == 2, "Step 2 passed"

def test_step3(setup_module, setup_function):
    print("[Test Step 3] Performing test step 3...")
    assert "a" in "apple", "Step 3 passed"
