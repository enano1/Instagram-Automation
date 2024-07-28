from scraper.auth import instagram_login
from scraper.scraper import scrape_post_data
from scraper.utils import get_post_url, export_data

def main():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")

    driver = instagram_login(username, password)
    post_url = get_post_url()
    data = scrape_post_data(driver, post_url)
    export_data(data, file_format='json')

    driver.quit()

if __name__ == "__main__":
    main()
