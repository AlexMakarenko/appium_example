import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import By


class BasePage:
    _default_wait = 10  # seconds
    CONCENT_POLICY_BTN = (By.XPATH, '//button[contains(@class, "fc-cta-consent")]')
    MENU_BTN = (By.XPATH, '//button[contains(@class, "navbar-toggler")]')
    MENU_SHOWED = (By.XPATH, '//*[@id="AppNavBar"][contains(@class, "show")]')
    LOGIN_MENU_ITEM = (By.XPATH, '//li[@class="nav-item"]/a[@href="/consumer/login"]')
    OAUTH_LOGIN_BUTTON = (By.XPATH, '//a[contains(@class, "btn")]')
    TOOLS_DROPDOWN = (By.XPATH, '//*[@id="ToolsDropDown"]')
    BASE64_MENU_ITEM = (By.XPATH, '//a[@href="/tools/base64-encode-decode"]')
    URL_ENCODE_MENU_ITEM = (By.XPATH, '//a[@href="/tools/url-encode-decode"]')
    CLOSE_AD_BUTTON = (By.XPATH, '//img[@aria-label="Close"]')
    DISMISS_AD_BUTTON = (By.XPATH, '//*[@id="dismiss-button"]')

    def __init__(self, driver):
        self.driver = driver

    def wait_presence(self, driver, locator: tuple, time_to_wait: int = _default_wait):
        return WebDriverWait(driver, time_to_wait).until(
            EC.presence_of_element_located(locator)
        )

    def wait_all_presences(
        self, driver, locator: tuple, time_to_wait: int = _default_wait
    ):
        return WebDriverWait(driver, time_to_wait).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_clickable(self, driver, locator: tuple, time_to_wait: int = _default_wait):
        return WebDriverWait(driver, time_to_wait).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_text_of_element(self, driver, locator: tuple, text: str, time_to_wait: int = _default_wait):
        return WebDriverWait(driver, time_to_wait).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def open_home_page(self):
        with allure.step('Opening https://gorest.co.in/'):
            return self.driver.get("https://gorest.co.in/")

    def accept_policy(self):
        with allure.step('Click on Concent policy button'):
            self.wait_presence(self.driver, self.CONCENT_POLICY_BTN).click()

    def open_burger_menu(self):
        with allure.step('Click on manu button'):
            self.wait_presence(self.driver, self.MENU_BTN).click()
            self.wait_presence(self.driver, self.MENU_SHOWED)

    def click_on_tools_menu_item(self):
        with allure.step('Click on tools dropdown list'):
            self.wait_presence(self.driver, self.TOOLS_DROPDOWN).click()

    def click_on_login_menu_item(self):
        with allure.step('Click on login menu button'):
            self.wait_presence(self.driver, self.LOGIN_MENU_ITEM).click()

    def click_on_base64_menu_item(self):
        with allure.step('Click on base64 tool menu item'):
            self.wait_presence(self.driver, self.BASE64_MENU_ITEM).click()

    def click_on_url_encode_menu_item(self):
        with allure.step('Click on url encode menu item'):
            self.wait_presence(self.driver, self.URL_ENCODE_MENU_ITEM).click()

    # def close_ad_if_present(self):
    #     dismiss_ad = self.driver.find_elements(*self.DISMISS_AD_BUTTON)
    #     close_ad = self.driver.find_elements(*self.CLOSE_AD_BUTTON)
    #     close_buttons = dismiss_ad + close_ad
    #     if close_buttons:
    #         for btn in close_buttons:
    #             btn.close()
