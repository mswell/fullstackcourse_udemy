import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.johnlewis.com/humanscale-diffrient-world-office-chair-white/p2155325")
soup = BeautifulSoup(r.content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_value = element.text.strip()

price = float(string_value[1:])

if price < 400:
    print("Buy the chair!")
elif price == 400:
    print("Buy at your own peril!")
else:
    print("Definitely don't buy.")
