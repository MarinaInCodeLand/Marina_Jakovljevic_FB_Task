from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def click_btn_signup(self):
        """Click on the Sign up button to open sign-up form."""
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="desktop-open-signup-modal"]').click()

    #Fills out the sign-up form with provided user data.
    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, "username").send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_signup_submit(self):
        """Click on the Sign up ...."""
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="auth-submit-button"]').click()

    def register_user(self, first_name, last_name, email, password):
        # Wait until the form is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_signup_submit()

    # Negative scenarios start
    ##########################

    def get_error_messages(self):
        error_messages = []

        # Prvo prikupi sve greške sa klasom 'label label-danger'
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.label.label-danger"))
            )
            errors = self.driver.find_elements(By.CSS_SELECTOR, "div.label.label-danger")
            error_messages.extend([e.text.strip() for e in errors if e.is_displayed()])
        except:
            pass  # ako nema takvih elemenata, nastavi

        # Ovde proveri ima li poruke i u elementu sa klasom 'media-body' za ime/prezime + broj
        try:
            media_error = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.media-body"))
            )
            text = media_error.text.strip()
            if text:
                error_messages.append(text)
        except:
            pass

        return error_messages







