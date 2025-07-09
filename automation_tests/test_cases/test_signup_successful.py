import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.click_signup_link_sitemap_page import SitemapPageClickSignUp
from base_pages.flow_signup_page import SignUpPage

class TestSignUpPositive:
    def test_successful_signup(self, driver):
        sitemap = SitemapPageClickSignUp(driver)
        signup = SignUpPage(driver)

        driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
        sitemap.click_sign_up_link() # from click_signup_link_page!

        # Other user data
        first_name = "Petar"
        last_name = "Petrovic"
        # Generate unique email
        unique_email = f"testuser_{int(time.time())}@example.com" #import time!
        email = unique_email
        password = "ValidPass123!"

        signup.register_user(first_name, last_name, email, password)

        # Check successful registration
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.list-title"))
        ).text

        assert "Top Fishing Destinations" in success_message