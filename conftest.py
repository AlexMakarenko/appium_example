import logging as log
import logging.config
import pytest
import allure
import time

from appium import webdriver
from appium.options.ios import SafariOptions

from api.user_api import UserApi, UserException
from ios_pages.base_page import BasePage

logging.config.dictConfig(
    {
        "version": 1,
        "loggers": {
            "": {  # root logger
                "level": "INFO",
                "handlers": [
                    "debug_console_handler",
                    "info_rotating_file_handler",
                ],
            },
            "my.package": {
                "level": "WARNING",
                "propagate": False,
                "handlers": ["info_rotating_file_handler"],
            },
        },
        "handlers": {
            "debug_console_handler": {
                "level": "DEBUG",
                "formatter": "info",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "info_rotating_file_handler": {
                "level": "INFO",
                "formatter": "info",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "info.log",
                "mode": "a",
                "maxBytes": 1048576,
                "backupCount": 10,
            },
        },
        "formatters": {
            "info": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            },
            "error": {
                "format": "%(asctime)s-%(levelname)s-%(name)s-%(process)d::%(module)s|\
                    %(lineno)s:: %(message)s"
            },
        },
    }
)


@pytest.fixture
def new_user():
    user_api = UserApi()
    payload = {
        "name": "John Smith",
        "gender": "male",
        "email": "jsmith@test.com",
        "status": "active",
    }
    user = user_api.create_user(payload)
    yield user
    try:
        user_api.delete_user(user.id)
    except UserException as e:
        log.error(f"Error during user deletion. Status code: {e.status_code}")


def make_screenshot(driver, test_name):
    name = f"{test_name}{int(time.time())}.png"
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


@pytest.fixture
def ios(request):
    common_caps = {
        "browserName": "Safari",
    }
    options = SafariOptions().load_capabilities(common_caps)
    options.platform_version = "17.0"
    options.device_name = "iPhone SE (3rd generation)"
    options.use_simulator = True
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    failed_before = request.session.testsfailed
    yield driver
    if request.session.testsfailed != failed_before:
        make_screenshot(driver, request.node.name)
    if driver:
        driver.quit()


@pytest.fixture
def gorest_safari(ios):
    base_page = BasePage(ios)
    base_page.open_home_page()
    base_page.accept_policy()
    yield ios
