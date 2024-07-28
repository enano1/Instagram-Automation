import requests
import json
import csv
import os
import time

def scrape_likes(driver, post_url):
    # Getting the shortcode from the post URL
    shortcode = post_url.split("/")[-2]

    cookies = driver.get_cookies()
    session_id = None
    for cookie in cookies:
        print(f"Cookie: {cookie}")  
        if cookie['name'] == 'sessionid':
            session_id = cookie['value']
            break

    if session_id is None:
        print("Failed to retrieve session ID from the WebDriver.")
        return []

    url = "https://www.instagram.com/graphql/query/"
    query_hash = "d5d763b1e2acf209d62d22d184488e57"  # update this later
    end_cursor = ''
    count = 0
    start_file = 1
    per_file = 250
    output_dir = 'scraped_data'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    headers = {
        'Cookie': f'sessionid={session_id}'
    }

    usernames = []

    while True:
        variables = {
            "shortcode": shortcode,
            "include_reel": True,
            "first": 50,
            "after": end_cursor
        }
        params = {
            'query_hash': query_hash,
            'variables': json.dumps(variables)
        }
        response = requests.get(url, headers=headers, params=params)
        try:
            data = response.json()
            print(f"Response JSON: {data}")  # debug this

            if 'data' not in data:
                print("Error: 'data' key not found in the response.")
                break

            edges = data['data']['shortcode_media']['edge_liked_by']['edges']
            page_info = data['data']['shortcode_media']['edge_liked_by']['page_info']
            end_cursor = page_info['end_cursor']
            has_next_page = page_info['has_next_page']

            with open(os.path.join(output_dir, f'likes_{start_file}.csv'), 'a', newline='') as csvfile:
                fieldnames = ['username', 'full_name', 'profile_pic_url', 'is_private']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if count == 0:
                    writer.writeheader()

                for edge in edges:
                    node = edge['node']
                    writer.writerow({
                        'username': node['username'],
                        'full_name': node['full_name'],
                        'profile_pic_url': node['profile_pic_url'],
                        'is_private': node['is_private']
                    })
                    usernames.append(node['username'])
                    count += 1

                    if count % per_file == 0:
                        start_file += 1

            if not has_next_page:
                break

            time.sleep(2)  

        except json.JSONDecodeError:
            print("Error decoding JSON response.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    print(f"Scraping completed. Total likes scraped: {count}")
    return usernames
