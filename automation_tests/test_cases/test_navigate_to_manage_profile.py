import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.login_page import LoginPage

def test_login_and_go_to_manage_profile(driver):
    driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
    # Now navigate to the Manage Profile page
    driver.get("https://qahiring.dev.fishingbooker.com/manage/profile")

    lp = LoginPage(driver)

    # Enter login credentials
    lp.enter_email("bookerfishing@gmail.com")
    lp.click_email_login()
    lp.enter_password("fishingBooker.9")
    lp.click_password_login()

    # # Wait until the URL contains '/manage/profile' indicating successful login and redirection
    # WebDriverWait(driver, 10).until(
    #     EC.url_contains("/manage/profile")
    # )

    # Wait for the profile header to appear
    profile_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h3[text()='You on FishingBooker']")
        )
    )

    # Assert that the profile header is correctly displayed
    assert profile_header.text == "You on FishingBooker"

