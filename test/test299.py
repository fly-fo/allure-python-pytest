import allure
import pytest


@allure.id("299")
@allure.tag("Dynamic tag")
@allure.title("Тест для показа автоматизации")
@allure.label("owner", "Ольга Ч")
@allure.feature("sending attachments", "test-automation")
def test_method():
    with allure.step("Сначала мы создаём ручной тест"):
        pass
    with allure.step("Затем с помощью магии создаём для него код"):
        pass
    with allure.step("Исполняем тест в среде исполнения"):
        pass
    with allure.step("Закрываем лонч"):
        pass
    with allure.step("Сравниваем сценарии"):
        pass
    with allure.step("Утверждаем сценарий автотеста"):
        pass

