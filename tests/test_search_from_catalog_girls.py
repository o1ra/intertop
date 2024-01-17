import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from intertop_tests.utils.country_selection import choice_of_country


def test_my_interests():
    with allure.step('Выбор страны '):
        choice_of_country()

    with allure.step('Выбор пола'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/forHerButton')).click()

    with allure.step('Нажать кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).click()
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее'))

    with allure.step('Нажать кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).click()

    with allure.step('Выбрать опцию "не включать уведомления"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/notNowNotificationButton')).should(
            have.text('Не сейчас')).click()

    with allure.step('Перейти на страницу шоппинга'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Shopping")).click()

    with allure.step('Открыть каталог'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Каталог"]')).click()

    with allure.step("Выбрать вкладку товаров для девочек "):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Девочкам"]')).click()

    with allure.step("Выбрать пункт Одежда "):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Одежда"]')).click()

    with allure.step('Проверить что товары есть в выдаче'):
        results = browser.all((AppiumBy.XPATH, '//android.widget.FrameLayout'))
        results.should(have.size_greater_than(0))
