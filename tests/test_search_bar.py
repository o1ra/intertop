import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from intertop_tests.utils.country_selection import choice_of_country


def test_search():
    with allure.step('Выбор страны'):
        choice_of_country()

    with allure.step('Выбор пола'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/forHerButton')).click()

    with allure.step('Нажать кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее')).click()

    with allure.step('Нажать кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее')).click()


    with allure.step('Выбрать опцию "не включать уведомления"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/notNowNotificationButton')).should(
            have.text('Не сейчас')).click()

    with allure.step('Перейти на страницу шоппинга'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Shopping')).click()


    with allure.step('Выполнить поиск товара по вкладке "Мужчинам"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/categoriesSearchIcon')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Мужчинам"]')).click()
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/searchSearchField')).click().set_value(
            "Кроссовки").click()
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Кроссовки"]')).click()

    with allure.step('Проверить товары в выдаче'):
        results = browser.all((AppiumBy.XPATH, '//android.widget.FrameLayout'))
        results.should(have.size_greater_than(0))




