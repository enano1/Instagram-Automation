# import re

# def validate_instagram_url(url):
#     pattern = r'https?://(www\.)?instagram\.com/p/[\w-]+/'
#     return re.match(pattern, url) is not None

import re

def validate_instagram_url(url):
    pattern = r'https?://(www\.)?instagram\.com/p/[\w-]+/?'
    return re.match(pattern, url) is not None
