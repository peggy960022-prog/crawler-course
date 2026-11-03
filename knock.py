import requests  # 把 requests 工具拿到桌上

# ===== 設定區（換網站時改這裡）=====
URL = "https://books.toscrape.com/no-such-page.html"  # 要敲的門牌號碼（網址）

# 自我介紹（名片）：這是一個 dict，名稱對內容
# 注意：值只能用英文、數字和符號，不要放中文，否則程式會出錯
HEADERS = {
    "User-Agent": "CrawlerCourseStudent/1.0 (personal learning practice)"
}
# ====================================

# headers=HEADERS 的意思：敲門時，把我們寫的名片遞出去
# 不寫這個參數的話，requests 會自己報預設的名號
response = requests.get(URL, headers=HEADERS, timeout=10)

# 看屋主的回應：狀態碼
print("狀態碼：", response.status_code)

# 看我們實際送出去的自我介紹
print("我們送出的 headers：", response.request.headers)

print(type(response))
print(type(response.status_code))