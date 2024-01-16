import os
from typing import Literal
import pydantic
from appium.options.android import UiAutomator2Options
from intertop_tests.utils import path

EnvContext = Literal['local', 'bstack']


class Config(pydantic.BaseSettings):
    # --- Context ---
    context = os.getenv('context', 'bstack')

    # --- Appium Capabilities ---

    platformName: str = os.getenv('platformName', 'android')
    platformVersion: str = os.getenv('platformVersion', '13.0')
    deviceName: str = os.getenv('deviceName', 'Samsung Galaxy S23 Ultra')
    app: str = os.getenv('app')
    udid: str = os.getenv('udid')

    # --- > BrowserStack Capabilities ---
    projectName: str = os.getenv('projectName', 'First Python project')
    buildName: str = os.getenv('buildName', 'browserstack-build-1')
    sessionName: str = os.getenv('sessionName', 'BStack first_test')
    remote_url: str = os.getenv('remote_url', 'http://127.0.0.1:4723/wd/hub')  # it's a default appium server url
    userName: str = os.getenv('userName')
    accessKey: str = os.getenv('accessKey')

    # --- Selene ---
    timeout: float = 30.0

    def driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local_emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('app', self.app)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.deviceName)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'First Python project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack first_test',
                    'userName': self.userName,
                    'accessKey': self.accessKey,
                },
            )

        return options


context = Config().context
config = Config(_env_file=path.to_resource(f'.env.{context}'))
