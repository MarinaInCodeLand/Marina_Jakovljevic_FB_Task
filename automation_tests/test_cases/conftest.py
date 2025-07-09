import pytest
from selenium import webdriver
from base_pages.login_page import LoginPage

@pytest.fixture
def driver():
    # Start the browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Close the browser after test
    driver.quit()

# # @pytest.fixture
# # def login(driver):
# #     login_page = LoginPage(driver)
# #     driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
# #     login_page.click_btn_login()
# #     login_page.enter_email("bookerfishing@gmail.com")
# #     login_page.click_email_login()
# #     login_page.enter_password("fishingBooker.9")
# #     login_page.click_password_login()
# #     return driver
#
# @pytest.fixture
# def logged_in_driver(driver):
#     # Autorizacija sa sitemap URL-om
#     driver.get("https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/sitemap")
#     # Posle logina idi na manage profile
#     driver.get("https://qahiring.dev.fishingbooker.com/manage/profile")
#
#     # Navigacija na login i login akcija
#     login = LoginPage(driver)
#     login.enter_email("bookerfishing@gmail.com")
#     login.click_email_login()
#     login.enter_password("fishingBooker.9")
#     login.click_password_login()
#
#     return driver