import allure

from appium.webdriver.common.appiumby import By

from ios_pages.base_page import BasePage


class GorestLoginPage(BasePage):
    OAUTH_LOGIN_BUTTON = (By.XPATH, '//a[contains(@class, "btn")]')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Get links from login buttons')
    def get_links_from_login_buttons(self):
        all_login_buttons = self.wait_all_presences(
            self.driver, self.OAUTH_LOGIN_BUTTON
        )
        return [btn.get_attribute("href") for btn in all_login_buttons]
