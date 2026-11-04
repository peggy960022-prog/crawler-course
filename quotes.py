import requests
from bs4 import BeautifulSoup

# ===== 設定區（換網站時改這裡）=====
URL = "https://quotes.toscrape.com/"   # 要敲的門牌號碼
HEADERS = {
    "User-Agent": "CrawlerCourseStudent/1.0 (personal learning practice)"
}                                       # 自我介紹（名片），沿用 unpack.py
ENCODING = "utf-8"                      # 依 <head> 裡的 meta charset="UTF-8" 設定
BOX_TAG = "div"                         # 每一則名言「外盒」的標籤
BOX_CLASS = "quote"                     # 外盒的 class（沒有點）
TEXT_TAG = "span"                       # 名言文字所在的標籤（在外盒裡面）
TEXT_CLASS = "text"                     # 名言文字的 class
AUTHOR_TAG = "small"                    # 作者所在的標籤（在外盒裡面）
AUTHOR_CLASS = "author"                 # 作者的 class
# =====================================

# 敲門：送出請求，timeout=10 代表最多等 10 秒
response = requests.get(URL, headers=HEADERS, timeout=10)
# 指定編碼，要在讀 response.text 之前
response.encoding = ENCODING
print("狀態碼：", response.status_code)

# 拆信：把網頁原始碼交給 BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# quotes 是一個 list，裡面裝著所有外盒
quotes = soup.find_all(BOX_TAG, class_=BOX_CLASS)
print("找到幾個盒子：", len(quotes))

# 迴圈：每一圈的 quote 是 list 裡的「一個外盒」
for quote in quotes:
    # 盒子裡找盒子：只在這一則外盒裡找「標籤 + class」都符合的
    text = quote.find(TEXT_TAG, class_=TEXT_CLASS).text.strip()
    author = quote.find(AUTHOR_TAG, class_=AUTHOR_CLASS).text.strip()
    # 每一圈印出一行：作者 | 名言
    print(author, "|", text)