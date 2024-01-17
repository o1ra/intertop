import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_onboarding():
    with allure.step('Выбор страны '):
        results = browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button[1]'))
        results.should(have.exact_text("Казахстан"))

    with allure.step('Выбор пола'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/forHerButton')).click()

    with allure.step('Нажать кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).click()
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Далее'))

    with allure.step('Нажать кнопку "Далее"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).click()


    with allure.step('Выбрать опцию "не включать уведомления"'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/notNowNotificationButton')).click()
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
            have.text('Не сейчас'))


    with allure.step('Заголовок главной страницы'):
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/myIntertopTitleText')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'ua.mad.intertop:id/myIntertopTitleText')).should(
            have.text('Для тебя'))

