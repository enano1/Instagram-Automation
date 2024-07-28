import pandas as pd
import json

def get_post_url():
    post_url = input("Enter the Instagram post URL: ")
    if not post_url.startswith("https://www.instagram.com/p/"):
        raise ValueError("Invalid Instagram post URL")
    return post_url

def export_data(data, file_format='json'):
    if file_format == 'json':
        with open('output/instagram_data.json', 'w') as f:
            json.dump(data, f, indent=4)
    elif file_format == 'csv':
        likes_df = pd.DataFrame(data['likes'], columns=['Username'])
        comments_df = pd.DataFrame(data['comments'])
        likes_df.to_csv('output/instagram_likes.csv', index=False)
        comments_df.to_csv('output/instagram_comments.csv', index=False)
