import requests
from config import URL

value = requests.get(URL)
json_format = value.json()

print("\n---Assalomu aleykum 🙂---\n")
print("Currency Converter dasturiga xush kelibsiz!\n")

print("Mavjud kurslar: ", end = " ")
for a in json_format:
    print(a['code'], end = " ")

count = float(input("\n\nqancha pulni konver qilmoqchisiz -> "))
value_to = str(input("qaysi pul birligiga o'tkazish kerak -> "))
value_from = str(input("qaysi pul birligidan o'tkazmoqchisiz -> "))

m = value_from.upper()
n = value_to.upper()

for i in json_format:
    if i['code'] == n:
        for j in json_format:
            if m == j['code']:
                s = f"natija = {float(j['cb_price'])/float(i['cb_price']) * count}"
                print(s)
        break

