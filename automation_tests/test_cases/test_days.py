import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.login_page import LoginPage
from base_pages.update_profile_page import ProfilePage

# Test da izbor dana koji je veci od
# maksimalnog br dana za taj mesec NE postoji u dropdownu
months_days = {
    "January": 31,
    "February": 28,  # po zadatku ne mora prestupna godina
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

@pytest.mark.parametrize("month, invalid_day", [
    ("April", 31),
    ("June", 31),
    ("September", 31),
    ("November", 31),
    ("February", 30),
    ("February", 31),
])

def test_invalid_date_selection(driver, month, invalid_day):
    driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
    driver.get("https://qahiring.dev.fishingbooker.com/manage/profile")

    lp = LoginPage(driver)
    lp.enter_email("bookerfishing@gmail.com")
    lp.click_email_login()
    lp.enter_password("fishingBooker.9")
    lp.click_password_login()

    profile = ProfilePage(driver)

    # Izaberi mesec
    profile.select_birth_month(month)

    # Pokušaj da izabereš invalidan dan
    day_dropdown = profile.get_day_dropdown()  # Get metoda u ProfilePage ti vrati Select element dana

    # Očekuje da ne postoji u dropdownu
    with pytest.raises(NoSuchElementException):
        Select(day_dropdown).select_by_visible_text(str(invalid_day))


