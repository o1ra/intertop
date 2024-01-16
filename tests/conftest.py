import os
import allure
import allure_commons
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser, support
from config import config
from intertop_tests.utils import attach
from intertop_tests.utils import path

def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        choices=['local', 'bstack'],
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = path.to_resource(f".env.{context}")
    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f"Warning: Configuration file '{env_file_path}' not found.")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    options = config.driver_options(context=context)
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            options.get_capability('remote_url'),
            options=options
        )

    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    attach.screenshot()

    attach.page_source_xml()

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id' + session_id):
        browser.quit()

    if context == 'bstack':
        attach.bstack_video(session_id)
