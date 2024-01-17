from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy


def choice_of_country():
    country = browser.element((AppiumBy.XPATH, '//android.widget.Button[1]'))
    if country.matching(have.exact_text('Казахстан')):
        country.click()
    else:
        browser.element((AppiumBy.XPATH, '//android.widget.Button[2]')).click()