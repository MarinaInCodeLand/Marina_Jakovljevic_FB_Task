import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProfilePage:
    def __init__(self, driver):
        # Konstruktor koji prima WebDriver objekat i čuva ga za dalje korišćenje
        self.driver = driver

    def click_change_photo(self):
        # Klik na dugme "Change Photo" koje otvara modal za promenu slike
        change_photo_button = self.driver.find_element(By.XPATH, "//span[text()='Change Photo']")
        change_photo_button.click()

    def upload_profile_picture(self, relative_image_path):
        # Upload slike profila pomoću apsolutne putanje ka fajlu
        image_path = os.path.abspath(relative_image_path)
        # Pronađi input i ubaci sliku
        self.driver.find_element(By.ID, "profile_picture").send_keys(image_path)

    def click_phone_input(self):
        # Skroluje stranicu na dole i fokusira se na polje za unos telefona
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)

        # Sačeka da se pojavi input
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "phone"))
        )

        # Klikne u input
        phone_input.click()

    def update_phone(self, phone):
        # Poziva metodu za phone input i upisuje broj telefona
        self.click_phone_input()  # koristiš prethodnu metodu
        phone_input = self.driver.find_element(By.ID, "phone")
        phone_input.clear()
        phone_input.send_keys(phone)

    def update_birthdate(self, month_text, day_text, year_text):
        # Ažurira datum rođenja izborom iz tri dropdown menija

        # Mesec i dan imaju istu klasu => dohvata ih zajedno kao listu
        dropdowns = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "select.date-field-margin"))
        )

        # Selektuje mesec (prvi dropdown)
        month_dropdown = dropdowns[0]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", month_dropdown)
        month_dropdown.click()
        Select(month_dropdown).select_by_visible_text(month_text)

        # Selektuje dan (drugi dropdown)
        day_dropdown = dropdowns[1]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", day_dropdown)
        day_dropdown.click()
        Select(day_dropdown).select_by_visible_text(day_text)

        # Godina (nema istu klasu kao prethodna dva, trazi se posebno!)
        year_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[not(contains(@class, 'date-field-margin')) and contains(@class, 'date-field-width')]"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", year_dropdown)
        year_dropdown.click()
        Select(year_dropdown).select_by_visible_text(year_text)

    def click_save_changes(self):
        # Klik na dugme "Save changes" za čuvanje izmena na profilu
        save_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save changes')]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
        save_btn.click()

    def get_success_message(self):
        # Nakon klika na "Save changes", ova metoda ide na vrh strane
        # i pokušava da uhvati poruku "Profile successfully saved!"

        # Scroll na vrh da poruka bude u viewport-u
        self.driver.execute_script("window.scrollTo(0, 0);")

        try:
            # Čeka da se poruka pojavi (brzo nestaje)
            success_msg = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Profile successfully saved')]"))
            )
            return success_msg.text
        except:
            return None # Ako se ne pojavi na vreme, vraća None

    def select_birth_month(self, month_text):
        # Čeka da se učitaju svi dropdown elementi za datume (mesec i dan imaju istu klasu)
        dropdowns = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "select.date-field-margin"))
        )

        # Mesec rodjenja
        month_dropdown = dropdowns[0]

        #self.driver.execute_script("arguments[0].scrollIntoView(true);", month_dropdown)

        # Selektujemo mesec po vidljivom tekstu, npr. "February"
        Select(month_dropdown).select_by_visible_text(month_text)

    def get_day_dropdown(self):
        # Ponovo uzimamo sve dropdown elemente koji imaju istu klasu (mesec i dan)
        dropdowns = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "select.date-field-margin"))
        )

        # Drugi dropdown (indeks 1) => dan rođenja
        return dropdowns[1]
