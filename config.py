import os
from typing import Literal
import pydantic
from appium.options.android import UiAutomator2Options
from intertop_tests.utils import path

EnvContext = Literal['local', 'bstack']


class Config(pydantic.BaseSettings):
    # --- Context ---
    context: EnvContext = 'bstack'

    # --- Appium Capabilities ---

    platformName: str = os.getenv('platformName')
    platformVersion: str = os.getenv('platformVersion')
    device_name: str = os.getenv('deviceName')
    app_local: str = path.to_resource('intertop-2-78-0.apk')
    udid: str = os.getenv('udid')
    # appWaitActivity: str = os.getenv('appWaitActivity', 'org.wikipedia.*')

    # --- > BrowserStack Capabilities ---

    remote_url: str = os.getenv('remote_url')
    app_bstack: str = os.getenv('app')
    userName: str = os.getenv('userName')
    accessKey: str = os.getenv('accessKey')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('app', self.app_local)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('app', self.app_bstack)
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
