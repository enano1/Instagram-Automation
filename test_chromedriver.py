from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_chromedriver():
    try:
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.get('https://www.google.com')
        print(driver.title)
        driver.quit()
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")

if __name__ == '__main__':
    test_chromedriver()
