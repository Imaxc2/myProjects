from bs4 import BeautifulSoup as BS
import requests
import time
import webbrowser

minim = 0
while True:
    r = requests.get("https://funpay.com/chips/99/")
    html = BS(r.content, "html.parser")
    allcost = []
    for el in html.select(".tc-price"):
        title = el.select("div")
        if title:
            rubles = float(title[0].text.split(' ')[0].strip())
            allcost.append(rubles)
    if minim != min(allcost):
        minim = min(allcost)
        print(f'{minim} - {len(allcost)}')
        if minim <= 0.23:
            webbrowser.open('https://funpay.com/chips/99/')
    time.sleep(240)

