import os
from typing import Literal
from appium.options.android import UiAutomator2Options
from pydantic import BaseModel
from intertop_tests.utils import path


EnvContext = Literal['local', 'bstack']


class Settings(BaseModel):
    context: str
    userName: str = os.getenv('USER_NAME')
    password: str = os.getenv('ACCESS_KEY')
    remote_url: str = os.getenv('REMOTE_URL')
    udid: str = os.getenv('UDID')
    app: str = os.getenv('APP')
    platformVersion: str = os.getenv('PLATFORM_VERSION')
    platformName: str = os.getenv('PLATFORM_NAME')
    deviceName: str = os.getenv('DEVICE_NAME')
    projectName: str = os.getenv('PROJECT_NAME')
    buildName: str = os.getenv('BUILD_NAME')
    sessionName: str = os.getenv('SESSION_NAME')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('app', path.to_resource(self.app))
            options.set_capability('udid', self.udid)

        if context == 'bstack':
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('platformName', self.platformName)
            options.set_capability('deviceName', self.deviceName)
            options.set_capability('projectName', self.projectName)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options', {
                    'buildName': self.buildName,
                    'sessionName': self.sessionName,
                    'userName': self.userName,
                    'accessKey': self.password,
                },
            )

        return options


config = Settings(context='local')






