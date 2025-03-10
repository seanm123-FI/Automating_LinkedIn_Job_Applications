from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

EMAIL = "Seanmurphy852@gmail.com"   # Your LinkedIn Email
PASSWORD = "Killara12!"   # Your LinkedIn Password
PHONE = '083 472 3254'

def abort_application(driver):
    try:
        discard_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-control-name=discard_application_confirm_btn]")))
        discard_button.click()
        # Don't show job again
        dont_show_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label^='Dismiss'][aria-label*='job']")))
        dont_show_button.click()
        print("Aborted application")
    except Exception as e:
        print("Could not abort application:", e)

def login(driver):
    try:
        # Open LinkedIn
        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4158619509&distance=25&f_AL=true&f_E=2%2C3%2C4&f_PP=105178154&f_WT=3%2C2&geoId=104738515&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
        print("Opened LinkedIn")

        # Click on the Sign in button
        sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button")))
        sign_in_button.click()
        print("Clicked on the Sign in button")

        # Enter the email and password
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#base-sign-in-modal_session_key")))
        email_field.send_keys(EMAIL)
        password_field = driver.find_element(By.CSS_SELECTOR, "#base-sign-in-modal_session_password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        print("Entered email and password")
    except Exception as e:
        print("Error logging in:", e)

def load_all_jobs(driver):
    # Scroll to load all job listings
    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def apply_for_jobs(driver):
    # Get Listings
    try:
        all_jobs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable")))
        print("Found", len(all_jobs), "jobs")
    except Exception as e:
        print("Error finding job listings:", e)
        return

    number_of_submissions = 0
    for job in all_jobs:
        job.click()
        time.sleep(1)

        try:
            # Click on the Easy Apply button
            easy_apply_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button")))
            easy_apply_button.click()
            print("Clicked on the Easy Apply button")
        except Exception as e:
            print("Easy Apply button not found:", e)
            continue

        try:
            phone_field = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id*=phoneNumber]")))
            if not phone_field.get_attribute('value'):
                phone_field.send_keys(PHONE)
                print("Entered phone number")
        except Exception as e:
            print("Phone number field not found:", e)

        try:
            next_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Continue to next step']")))
            next_button.click()
        except Exception as e:
            print("Next button not found:", e)

        try:
            review_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Review your application']")))
            review_button.click()
        except Exception as e:
            print("Review button not found:", e)

        try:
            submit_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "footer button")))
            if "Submit application" in submit_button.text:
                submit_button.click()
                time.sleep(1)
                print("Submitted application")
                number_of_submissions += 1
            else:
                print("Submit button not found")
                abort_application(driver)
        except Exception as e:
            print("Submit button not found or an error occurred:", e)
            abort_application(driver)
            continue

        try:
            done_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label^='Dismiss']")))
            done_button.click()
            dont_show_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label^='Dismiss'][aria-label*='job']")))
            dont_show_button.click()
        except Exception as e:
            print("Could not find done button:", e)
            abort_application(driver)

    print("Number of applications submitted:", number_of_submissions)

# Main execution
if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-webrtc")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    login(driver)
    load_all_jobs(driver)
    apply_for_jobs(driver)

    driver.quit()
    print("Done")