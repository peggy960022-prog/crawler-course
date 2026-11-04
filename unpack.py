import requests
from bs4 import BeautifulSoup

# ===== 設定區（換網站時改這裡）=====
URL = "https://books.toscrape.com/"  # 要敲的門牌號碼（網址）
HEADERS = {
    "User-Agent": "CrawlerCourseStudent/1.0 (personal learning practice)"
}  # 自我介紹（名片）
ENCODING = "utf-8"           # 網頁的文字編碼（換網站時要確認）
BOX_TAG = "article"          # 每一筆資料「外盒」的標籤
BOX_CLASS = "product_pod"    # 外盒的 class 名稱
TITLE_TAG = "h3"             # 書名所在盒子的標籤（在外盒裡面）
LINK_TAG = "a"               # 書名連結的標籤（在 h3 裡面）
TITLE_ATTR = "href"         # 完整書名放在哪個名牌（HTML 屬性）
PRICE_TAG = "p"              # 價格所在盒子的標籤
PRICE_CLASS = "price_color"  # 價格盒子的 class
# ====================================

# 敲門
response = requests.get(URL, headers=HEADERS, timeout=10)
# 指定編碼，要在使用 response.text 之前
response.encoding = ENCODING
print("狀態碼：", response.status_code)

# 拆信，找出所有外盒
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all(BOX_TAG, class_=BOX_CLASS)
print("找到幾個盒子：", len(books))

# 迴圈：一個一個拿起外盒，每一圈 book 就是其中一個盒子
for book in books:
    # 盒子裡找盒子：先找 h3，再在 h3 裡找 a
    title_box = book.find(TITLE_TAG)
    link = title_box.find(LINK_TAG)
    # 完整書名：讀名牌（HTML 屬性），用 ["名稱"] 讀
    title = link[TITLE_ATTR]
    # 價格：在這本書的外盒裡找價格盒子，取文字並去掉空白
    price = book.find(PRICE_TAG, class_=PRICE_CLASS).text.strip()
    # 每一圈印出一行
    print(title, "|", price)