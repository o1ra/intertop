import allure
from appium.webdriver.common.appiumby import AppiumBy
# from selene import browser, have, be
#
#
# def test_seacth():
#     with allure.step(''):
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/shopping'))
#
#
#     with allure.step(''):
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/categoriesSearchIcon')).click()
#
#     with allure.step('Verify content page 2'):
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/searchSearchField')).click().set_value("dress")
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
#             have.text('Далее'))
#
#     with allure.step(''):
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).click()
#
#
#
#     with allure.step(''):
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/notNowNotificationButton')).click()
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/nextButton')).should(
#             have.text('Не сейчас'))
#
#
#     with allure.step(''):
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/myIntertopTitleText')).wait_until(be.visible)
#         browser.element((AppiumBy.ID, 'ua.mad.intertop:id/myIntertopTitleText')).should(
#             have.text('Для тебя'))
#
#
#
