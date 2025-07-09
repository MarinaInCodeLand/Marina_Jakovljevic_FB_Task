from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object Model for the login page."""
    btn_login_css = '[data-testid="desktop-open-login-modal"]'
    input_email_id = "username"
    input_password_id = "password"
    button_email_login_css = 'button[data-testid="auth-submit-button"]'
    button_password_login_css = 'button[data-testid="auth-password-submit-button"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_btn_login(self):
        """Click on the Log in button to open login modal."""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_login_css))).click()

    def enter_email(self, email):
        """Enter email in the email input field."""
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, self.input_email_id)))
        email_input.clear()
        email_input.send_keys(email)

    def click_email_login(self):
        """Click on the Continue with email button after entering email."""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_email_login_css))).click()

    def enter_password(self, password):
        """Enter password in the password input field."""
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, self.input_password_id)))
        password_input.clear()
        password_input.send_keys(password)

    def click_password_login(self):
        """Click on the login button after entering password."""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_password_login_css))).click()
