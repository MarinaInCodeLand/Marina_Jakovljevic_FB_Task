import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.flow_signup_page import SignUpPage

@pytest.mark.parametrize("password, expected_error", [
    ("Short1!", "Password must be at least 12 characters long"),
    ("passwordonlylower!", "Must contain at least one uppercase letter"),
    ("PASSWORDONLYUPPER!", "Must contain at least one lowercase letter"),
    ("NoNumbersHere!", "Must contain at least one number"),
    ("NoSpecial123", "Must contain at least one special character")
])

def test_password_validation(driver, password, expected_error):
    # Open the main sitemap page
    driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")

    signup_page = SignUpPage(driver)

    # Click on the Sign up button to open the registration form
    signup_page.click_btn_signup()

    # Wait until the first name field is visible, indicating form is ready
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    # Fill in valid data for all fields except password (which is parametrized)
    signup_page.enter_first_name("Marina")
    signup_page.enter_last_name("Jakovljević")
    signup_page.enter_email("email@example.com")
    signup_page.enter_password(password)

    # Submit the sign-up form
    signup_page.click_signup_submit()

    # Collect error messages displayed on the form
    errors = signup_page.get_error_messages()

    # Assert that the expected password validation error message is shown
    assert expected_error in errors
