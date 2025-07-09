import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.flow_signup_page import SignUpPage

@pytest.mark.parametrize("email, expected_error", [
    # Invalid email formats
    ("plainaddress", "Enter a valid email."),
    ("missingatsign.com", "Enter a valid email."),
    ("@missingusername.com", "Enter a valid email."),
    ("user@.com", "Enter a valid email."),
    ("user@com", "Enter a valid email."),
    ("user@domain..com", "Enter a valid email."),
    ("user@domain.c", "Enter a valid email."),
    ("user name@domain.com", "Enter a valid email."),
    ("invalidemail.com", "Enter a valid email."),

    # Already registered email
    ("bookerfishing@gmail.com", "bookerfishing@gmail.com is already registered at FishingBooker. Check the email you entered, or log in to your existing account.")
])
def test_email_validation(driver, email, expected_error):
    # Open target page
    driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
    signup_page = SignUpPage(driver)

    # Open the sign-up form
    signup_page.click_btn_signup()

    # Wait for the form to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    # Fill in valid data for all fields except the email
    signup_page.enter_first_name("Marina")
    signup_page.enter_last_name("Jakovljević")
    signup_page.enter_email(email)
    signup_page.enter_password("Password123!")

    # Submit the form
    signup_page.click_signup_submit()

    # Capture displayed error messages
    errors = signup_page.get_error_messages()

    # Assert that expected error is shown
    assert expected_error in errors
