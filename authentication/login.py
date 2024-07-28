from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_instagram(username, password):
    try:
        print("Starting WebDriver setup...")
        driver_path = ChromeDriverManager().install()
        print(f"ChromeDriver path: {driver_path}")
        chrome_service = Service(driver_path)
        chrome_options = Options()
        print("Service and Options initialized.")
        
        # Initialize the Chrome WebDriver with the service and options
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        print("WebDriver initialized.")
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        
        time.sleep(5)  # Wait for the login process to complete
        
        # Check if 2FA is required
        try:
            two_fa_input = driver.find_element(By.NAME, 'verificationCode')
            two_fa_code = input("Enter the 2FA code: ")
            two_fa_input.send_keys(two_fa_code)
            two_fa_input.send_keys(Keys.RETURN)
            time.sleep(5)  # Wait for the 2FA process to complete
        except NoSuchElementException:
            print("2FA not required or already completed.")
        
        # Wait for the main page to load after login
        time.sleep(5)
        if "accounts/login" in driver.current_url:
            print("Login failed, please check your credentials.")
            return None

        return driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return None

if __name__ == '__main__':
    username = input('Enter your Instagram username: ')
    password = input('Enter your Instagram password: ')
    driver = login_instagram(username, password)
    if driver:
        print("Login successful. You can proceed with further actions.")
    else:
        print("Login failed.")
