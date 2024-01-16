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

    @property
    def run_on_browserstack(self):
        return 'hub.browserstack.com' in self.remote_url

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        if self.deviceName:
            options.set_capability('deviceName', self.deviceName)

        if self.platformName:
            options.set_capability('platformName', self.platformName)
        options.set_capability('app', path.to_resource(self.app) if self.app and (
                    self.app.startswith('./') or self.app.startswith('../')) else self.app)

        if self.udid:
            options.udid = self.udid

        if self.run_on_browserstack:
            options.load_capabilities(
                {
                    'platformVersion': self.platformVersion,
                    'noReset': False,
                    'bstack:options': {
                        'projectName': self.projectName,
                        'buildName': self.buildName,
                        'sessionName': self.sessionName,
                        'userName': self.userName,
                        'accessKey': self.accessKey
                    },
                }
            )

        return options


context = Config().context
config = Config(_env_file=path.to_resource(f'.env.{context}'))
