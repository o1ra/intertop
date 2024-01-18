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
@allure.story("Поиск с использованием строки поиска")
@allure.title("Поиск товара для мужчин с использованием строки поиска")
def test_search():
    with allure.step('Выбираем страну'):
        choice_of_country()

    with allure.step('Выбираем пол пользователя'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/forHerButton')).click()

    with allure.step('Нажимаем кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее')).click()

    with allure.step('Нажимаем кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее')).click()

    with allure.step('Выбираем опцию "не включать уведомления"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/notNowNotificationButton')).should(
            have.text('Не сейчас')).click()

    with allure.step('Переходим на страницу шоппинга'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Shopping')).click()

    with allure.step('Выполняем поиск товара по вкладке "Мужчинам"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/categoriesSearchIcon')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мужчинам"]')).click()
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/searchSearchField')).click().set_value(
            "Кроссовки").click()
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Кроссовки"]')).click()

    with allure.step('Проверяем товары в выдаче'):
        results = browser.all((AppiumBy.XPATH, '//android.widget.TextView['
                                               '@resource-id="ua.mad.intertop:id/productCartName"]'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Кроссовки'))
