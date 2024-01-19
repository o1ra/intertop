import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from intertop_tests.utils.country_selection import choice_of_country

@allure.tag("mobile")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
@allure.feature("Онбординг")
@allure.story("Онбординг для неавторизованного пользователя")
@allure.title("Прохождение онбординга с выбором чек-боксов")
def test_onboarding():
    with allure.step('Выбираем страну '):
        choice_of_country()

    with allure.step('Выбираем пол пользователя'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/forHimButton')).should(
            have.text('Для него')).click()

    with allure.step('Выбираем все чек-боксы'):
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[1]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[2]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[3]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[4]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[5]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[6]')).click()

    with allure.step('Нажимаем кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее')).click()

    with allure.step('Выбираем все чек-боксы'):
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[1]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[2]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[3]')).click()

    with allure.step('Нажимаем кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее')).click()

    with allure.step('Выбраем опцию "не включать уведомления"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/notNowNotificationButton')).should(
            have.text('Не сейчас')).click()

    with allure.step('Проверяем заголовок главной страницы'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/myIntertopTitleText')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/myIntertopTitleText')).should(
            have.text('Для тебя'))
