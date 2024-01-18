import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from intertop_tests.utils.country_selection import choice_of_country

@allure.tag("mobile")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
@allure.feature("Поиск")
@allure.story("Поиск из каталога")
@allure.title("Поиск из каталога товара для девочек")
def test_search_catalog():
    with allure.step('Выбираем страну '):
        choice_of_country()

    with allure.step('Выбираем пол пользователя'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/forHerButton')).click()

    with allure.step('Нажаимаем кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).click()
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее'))

    with allure.step('Нажимаем кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).click()

    with allure.step('Выбраем опцию "не включать уведомления"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/notNowNotificationButton')).should(
            have.text('Не сейчас')).click()

    with allure.step('Переходим на страницу шоппинга'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Shopping")).click()

    with allure.step('Открываем каталог'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Каталог"]')).click()

    with allure.step("Выбираем пункт Одежда "):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Одежда"]')).click()

    with allure.step('Проверяем что товары есть в выдаче'):
        results = browser.all((AppiumBy.XPATH, '//android.widget.FrameLayout'))
        results.should(have.size_greater_than(0))
        product_1 = browser.element((AppiumBy.XPATH,
                                  '//android.widget.FrameLayout[@resource-id="ua.mad.intertop:id/productCardViewListing"])[1]'))
    with allure.step("Выбраем вкладку товаров для девочек "):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/genderGirls')).click()

    with allure.step("Проверяем что выборка товаров сменилась "):
        with allure.step('Проверяем товары в выдаче'):
            results = browser.all((AppiumBy.XPATH, '//android.widget.FrameLayout'))
            results.should(have.size_greater_than(0))
            product_2 = browser.element((AppiumBy.XPATH,
                                      '//android.widget.FrameLayout[@resource-id="ua.mad.intertop:id/productCardViewListing"])[1]'))


            assert product_1 != product_2, ("Товары не могут быть одинаковыми")
