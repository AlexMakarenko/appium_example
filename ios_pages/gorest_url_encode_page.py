import allure

from appium.webdriver.common.appiumby import By
from selenium.common.exceptions import TimeoutException

from ios_pages.base_page import BasePage


class GorestUrlEncodePage(BasePage):
    URL_INPUT = (By.XPATH, '//*[@id="url-input"]')
    URL_OUTPUT = (By.XPATH, '//*[@id="url-output"]')
    URL_DECODE_BUTTON = (By.XPATH, '//button[contains(@class, "url-decode")]')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Enter text into imput')
    def enter_text_into_input(self, text: str):
        self.wait_presence(self.driver, self.URL_INPUT).send_keys(text)

    @allure.step('Click on encode button')
    def click_on_decode_button(self):
        self.wait_presence(self.driver, self.URL_DECODE_BUTTON).click()

    @allure.step('Verify the result')
    def check_url_result(self, text: str):
        try:
            self.wait_text_of_element(self.driver, self.URL_OUTPUT, text)
            return True
        except TimeoutException:
            return False
