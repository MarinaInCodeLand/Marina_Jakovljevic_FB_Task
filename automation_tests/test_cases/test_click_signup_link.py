import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.click_signup_link_sitemap_page import SitemapPageClickSignUp

class TestSignUpClick:
    page_url = "https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap"

    def test_click_signup(self):
        # Start the Chrome browser
        self.driver = webdriver.Chrome()
        # try => part of the code that might raise an exception
        try:
            # Open the target page
            self.driver.get(self.page_url)

            # Create an instance of the sitemap page and click the Sign up link
            self.page = SitemapPageClickSignUp(self.driver)
            self.page.click_sign_up_link()

            # Wait for the Sign up form to appear and get its text
            act_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='sc-ehmTmK hzcGeR']"))
            ).text

            # Assert that the Sign up page is opened by checking the text
            assert "Sign up" in act_text

        # finally => part of the code that ALWAYS executes,
        # regardless of whether an exception occurred
        finally:
            # Close the browser
            self.driver.quit()