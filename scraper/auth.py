from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def instagram_login(username, password):
    # Specify the exact ChromeDriver version here
    chrome_driver_version = "126.0.6478.183"  # Replace with your version
    try:
        driver = webdriver.Chrome(ChromeDriverManager(driver_version=chrome_driver_version).install())
        driver.get("https://www.instagram.com/accounts/login/")
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return None

    time.sleep(3)  # Wait for the page to load

    try:
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Error during login process: {e}")
        driver.quit()
        return None

    time.sleep(5)  # Wait for login to complete

    return driver
