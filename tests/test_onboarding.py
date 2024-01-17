import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from intertop_tests.utils.country_selection import choice_of_country


def test_onboarding():
    with allure.step('Выбор страны '):
        choice_of_country()

    with allure.step('Выбор пола'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/forHimButton')).click()

    with allure.step('Выбор всех чек-боксов'):
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[1]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[2]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[3]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[4]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[5]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[6]')).click()

    with allure.step('Нажать кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее')).click()

    with allure.step('Выбор всех чек-боксов'):
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[1]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[2]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.CheckBox[3]')).click()

    with allure.step('Нажать кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее')).click()

    with allure.step('Выбрать опцию "не включать уведомления"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/notNowNotificationButton')).should(
            have.text('Не сейчас')).click()

    with allure.step('Заголовок главной страницы'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/myIntertopTitleText')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/myIntertopTitleText')).should(
            have.text('Для тебя'))
