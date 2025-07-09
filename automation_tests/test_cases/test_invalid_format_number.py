import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.login_page import LoginPage
from base_pages.update_profile_page import ProfilePage

@pytest.mark.parametrize("invalid_phone", [
    "abc123!!!",
    "123",
    "+999999999999999999999",  # predugačak broj
    "phone1234",
])

def test_invalid_phone_number(driver, invalid_phone):
    # Navigacija i login
    driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
    driver.get("https://qahiring.dev.fishingbooker.com/manage/profile")

    lp = LoginPage(driver)
    lp.enter_email("bookerfishing@gmail.com")
    lp.click_email_login()
    lp.enter_password("fishingBooker.9")
    lp.click_password_login()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Change Photo']"))
    )

    profile = ProfilePage(driver)

    # Unos nevalidnog telefona
    profile.update_phone(invalid_phone)

    profile.click_save_changes()

    # Očekuje grešku!
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "phone-error"))
    )
    assert error is not None

