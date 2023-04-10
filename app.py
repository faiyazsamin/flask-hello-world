from flask import Flask, request
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup

@app.route('/')
def extractor():
    # target url
    all_data = ''
#     url = ["https://mzamin.com/news.php?news=50698","https://mzamin.com/news.php?news=50671","https://www.jagonews24.com/international/news/846639","https://www.somoynews.tv/news/2023-04-11/প্রতিদিন-দুই-পরিপূর্ণ-রোজার-সওয়াব-লাভ-করবেন-যেভাবে","https://www.prothomalo.com/world/india/zwke9i8cc6","https://www.somoynews.tv/news/2023-04-11/ইউরোপকে-অবশ্যই-যুক্তরাষ্ট্র-নির্ভরশীলতা-কমাতে-হবে-ম্যাক্রোঁ","https://www.ajkerpatrika.com/267868/ডলারের-আধিপত্য-ঠেকাতে-বিকল্প-আনছে-ব্রিকস-জোট"]
    url = request.args.get('data')
    # making requests instance
    for items in url:
        reqs = requests.get(items)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        title = soup.find("meta", property="og:title")
        all_data = all_data +"\n"+title["content"] if title else "No meta title given"
        # print(title["content"] if title else "No meta title given")
    return all_data
