import allure


@allure.epic("Allure TestOps")
@allure.feature("BDD")
@allure.story("Labels")
@allure.label("priority", "Low")
def test_allure_bdd_labels():
    pass


@allure.parent_suite("Custom parent suite")
@allure.suite("Custom suite")
@allure.label("priority", "Low")
@allure.sub_suite("Custom sub suite")
def test_allure_suites():
    pass


@allure.label("allure-examples", "allure-pytest")
@allure.label("priority", "Low")
def test_allure_custom_labels():
    pass

@allure.label("priority", "Low")
def test_dynamic_labels():
    allure.dynamic.label("test-image", "some-image:latest")


@allure.label("priority", "Low")
def test_allure_severity():
    pass

@allure.label("priority", "High")
@allure.tag("Tagged test")
def test_allure_tags():
    allure.dynamic.tag("Dynamic tag")

@allure.label("priority", "Low")
@allure.label("owner", "admin")
def test_owner():
    pass

@allure.label("priority", "Low")
@allure.id(123)
def test_allure_id():
    pass
