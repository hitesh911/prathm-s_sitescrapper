# from main import scrape_author_info


# print(scrape_author_info("http://onlinelibrary.wiley.com/doi/10.1002/mma.9842"))
import requests
headers = {
    "Sec-Ch-Ua":'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
response = requests.post("http://onlinelibrary.wiley.com/toc/10991476/2024/47/6", headers=headers)
print(response.status_code)
