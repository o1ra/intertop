import os
import allure
import pytest
import allure_commons
from intertop_tests.utils import attach, path
from dotenv import load_dotenv
from selene import browser, support
from appium import webdriver


def pytest_addoption(parser):
    parser.addoption("--context", default="bstack", help="Specify context")


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = path.to_resource(f".env.{context}")
    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=f'.env.{context}')
    else:
        print(f"Warning: Configuration file '{env_file_path}' not found.")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from config import config

    options = config.to_driver_options(context=context)

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=options
        )

    browser.config.timeout = 15.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    attach.screenshot()
    attach.page_source_xml()

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id' + session_id):
        browser.quit()

    if context == 'bstack':
        attach.bstack_video(config, session_id)
