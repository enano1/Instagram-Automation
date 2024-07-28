import time
from selenium.webdriver.common.by import By

def scrape_post_data(driver, post_url):
    driver.get(post_url)
    time.sleep(3)  # Wait for the page to load

    # Scrape likes
    likes_button = driver.find_element(By.CSS_SELECTOR, 'a[href*="/liked_by/"]')
    likes_button.click()
    time.sleep(3)
    likes_list = [like.text for like in driver.find_elements(By.CSS_SELECTOR, 'a[role="link"]')]

    # Scrape comments
    comments = []
    comments_elements = driver.find_elements(By.CSS_SELECTOR, 'ul.XQXOT p')
    for comment in comments_elements:
        username = comment.find_element(By.CSS_SELECTOR, 'a[role="link"]').text
        text = comment.find_element(By.CSS_SELECTOR, 'span').text
        comments.append({'username': username, 'comment': text})

    return {'likes': likes_list, 'comments': comments}
