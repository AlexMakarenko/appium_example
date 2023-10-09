import allure

from appium.webdriver.common.appiumby import By
from selenium.common.exceptions import TimeoutException

from ios_pages.base_page import BasePage


class GorestBase64Page(BasePage):
    BASE64_INPUT = (By.XPATH, '//*[@id="base64-input"]')
    BASE64_ENCODE_BUTTON = (By.XPATH, '//button[contains(@class, "base-64-encode")]')
    BASE64_OUTPUT_FIELD = (By.XPATH, '//*[@id="base64-output"]')

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Enter text into imput")
    def enter_text_into_base64_input(self, text: str):
        self.wait_presence(self.driver, self.BASE64_INPUT).send_keys(text)

    @allure.step("Click on encode button")
    def click_on_encode_button(self):
        self.wait_presence(self.driver, self.BASE64_ENCODE_BUTTON).click()

    @allure.step("Verify the result")
    def check_base64_result(self, text: str):
        try:
            self.wait_text_of_element(self.driver, self.BASE64_OUTPUT_FIELD, text)
            return True
        except TimeoutException:
            return False
