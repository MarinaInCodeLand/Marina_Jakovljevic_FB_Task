import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.login_page import LoginPage
from base_pages.update_profile_page import ProfilePage

def test_manage_profile(driver):
    # 1. Otvaranje stranice sitemap uz osnovnu autentifikaciju
    driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")

    # 2. Navigacija direktno na stranicu profila
    driver.get("https://qahiring.dev.fishingbooker.com/manage/profile")

    # 3. Login
    lp = LoginPage(driver)
    lp.enter_email("bookerfishing@gmail.com")
    lp.click_email_login()
    lp.enter_password("fishingBooker.9")
    lp.click_password_login()

    # 4. Sačekaj da se učita profil (pojavljuje se dugme "Change Photo")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Change Photo']"))
    )

    # 5. Inicijalizujemo stranicu profila
    profile = ProfilePage(driver)

    # 6. Upload slike
    profile.upload_profile_picture("images/profile_picture.jpg")

    # 7. Ažuriranje broja telefona
    profile.update_phone("0621991")

    # 8. Ažuriranje datuma rođenja
    profile.update_birthdate("January", "23", "1994")

    # 9. Klik na "Save changes" dugme
    profile.click_save_changes()

    # 10. Validacija – proveravamo da li se pojavila poruka o uspešnom čuvanju
    msg = profile.get_success_message()
    assert msg is not None and "successfully" in msg.lower(), "Success message not shown!"











