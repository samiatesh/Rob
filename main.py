import requests
import random
import time

# لیست یوزر ایجنت‌ها
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edge/91.0.864.48",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Android 10; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.172",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; AS; AS; InfoPath.3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 Edge/12.246",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
]

# لیست لینک‌ها
urls = [

     "https://nfashion2022.blogspot.com"
   
]

# تابع برای باز کردن لینک‌ها
def open_link(url, user_agent):
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers)
        print(f"Successfully opened {url} with User-Agent: {user_agent}")
        return response.text  # برگشت محتوای صفحه برای هر URL
    except requests.exceptions.RequestException as e:
        print(f"Error opening {url}: {e}")

# حلقه برای باز کردن لینک‌ها به صورت تصادفی و زمان‌بندی تصادفی
while True:
    for url in urls:
        user_agent = random.choice(user_agents)  # انتخاب تصادفی یوزر ایجنت
        print(f"Opening {url}...")
        open_link(url, user_agent)
        wait_time = random.randint(2, 10)  # زمان تصادفی بین 5 تا 15 ثانیه
        print(f"Waiting for {wait_time} seconds...")
        time.sleep(wait_time)  # صبر کردن به مدت زمان تصادفی
