import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.flow_signup_page import SignUpPage

# Test to verify error messages when all fields are left empty (step by step)
def test_signup_form_validation(driver):
    driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
    driver.maximize_window()

    signup_page = SignUpPage(driver)

    # Click on the Sign up button to open the form
    signup_page.click_btn_signup()

    # Wait for the form to appear
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    # Click on "Sign up" without entering any data
    signup_page.click_signup_submit()

    # Get all error messages
    errors = signup_page.get_error_messages()
    #print("Prikazane greške:", errors)

    # Verify that all required error messages are displayed
    assert "First Name is required." in errors
    assert "Last Name is required." in errors
    assert "Enter a valid email." in errors
    assert "Password is required." in errors

# Parametrized test to cover individual negative scenarios:
# - empty fields
# - missing First Name / Last Name / email or password
# - names containing digits (not allowed)

@pytest.mark.parametrize("first_name, last_name, email, password, expected_error", [
    ("", "", "", "", "First Name is required."), # all empty as previos example
    ("", "Jakovljević", "email@example.com", "Password123!", "First Name is required."),
    ("Marina", "", "email@example.com", "Password123!", "Last Name is required."),
    ("Marina", "Jakovljević", "", "Password123!", "Enter a valid email."),
    ("Marina", "Jakovljević", "email@example.com", "", "Password is required."),
    ("Marina123", "Jakovljević", "email@example.com", "Password123!", "Unprocessable entity! Your first and last name can't contain digits"),
    ("Marina", "123Jakovljević", "email@example.com", "Password123!", "Unprocessable entity! Your first and last name can't contain digits")
])

def test_signup_validation(driver, first_name, last_name, email, password, expected_error):
    driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
    signup_page = SignUpPage(driver)
    signup_page.click_btn_signup()

    # Wait for form to appear
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    # Fill in only the provided data (leave fields blank if needed)
    if first_name:
        signup_page.enter_first_name(first_name)
    if last_name:
        signup_page.enter_last_name(last_name)
    if email:
        signup_page.enter_email(email)
    if password:
        signup_page.enter_password(password)

    signup_page.click_signup_submit()
    errors = signup_page.get_error_messages()

    # Assert the specific expected error is shown
    assert expected_error in errors
