from authentication.login import login_instagram
from data_scraping.scrape_data import scrape_likes
from output.export_data import export_to_json, export_to_csv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def main():
    try:
        username = input('Enter your Instagram username: ')
        password = input('Enter your Instagram password: ')
        
        print("Attempting to log in to Instagram...")
        driver = login_instagram(username, password)
        
        if driver is None:
            print("Failed to initialize WebDriver.")
            return
        
        print("Login successful.")
        
        # to handle 2FA if necessary
        try:
            two_fa_input = driver.find_element(By.NAME, 'verificationCode')
            two_fa_code = input("Enter the 2FA code: ")
            two_fa_input.send_keys(two_fa_code)
            two_fa_input.send_keys(Keys.RETURN)
            time.sleep(5)  
        except NoSuchElementException:
            print("2FA not required or already completed.")
        
        post_url = input('Enter the Instagram post URL: ')
        
        print("Scraping likes from the post...")
        usernames = scrape_likes(driver, post_url)
        
        export_format = input('Enter the export format (json/csv): ').lower()
        filename = input('Enter the output filename: ')

        if export_format == 'json':
            export_to_json(usernames, filename)
        elif export_format == 'csv':
            export_to_csv(usernames, filename)
        else:
            print('Unsupported format.')

        print("Script completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
