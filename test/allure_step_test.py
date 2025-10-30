import allure

@allure.label("priority", "Low")
@allure.step
def step_function_with_args(arg1, arg2):
    pass

@allure.label("priority", "Medium")
@allure.step("Step with param '{param}'")
def step_with_placeholder(param):
    pass

@allure.label("priority", "Medium")
@allure.step("Custom step title")
def step_function_with_title():
    pass

@allure.label("priority", "Medium")
def test_step():
    with allure.step("First step"):
        step_with_placeholder("Param value")
        with allure.step("Nested step"):
            step_function_with_args("value1", "value2")
    step_function_with_title()
