import allure


@allure.step
def step_function_with_args(arg1, arg2):
    pass


@allure.step("Перейдите в поисковую систему '{param}'")
def step_with_placeholder(param):
    pass


@allure.step("Custom step title")
def step_function_with_title():
    pass


def test_step():
    with allure.step("Вход в поисковик"):
        step_with_placeholder("ya.ru")
        with allure.step("Введите поисковый запрос"):
            step_function_with_args("Квокка фото", "Кот фото")
    step_function_with_title()
