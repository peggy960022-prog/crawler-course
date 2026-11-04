import requests
from bs4 import BeautifulSoup

url = "http://10.167.215.35:8000/html"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
row = soup.select_one("hello")
print(response.text)
print(row)

# responses

# 1. response.text = "<p>hello</p>"
# 2. install bs
# 3. BeautifulSoup
# 4. select one
# 5. get text

