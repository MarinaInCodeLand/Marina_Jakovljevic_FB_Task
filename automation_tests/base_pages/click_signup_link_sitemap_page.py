from selenium.webdriver.common.by import By

class SitemapPageClickSignUp:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_up_link(self):
        """
        Finds and clicks the Sign up button/link on the sitemap page.
        """
        sign_up_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="desktop-open-signup-modal"]')
        sign_up_button.click()
