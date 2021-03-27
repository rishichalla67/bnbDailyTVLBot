import requests
from bs4 import BeautifulSoup
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url("https://discord.com/api/webhooks/825460904938307645/LEpZCep1GtYTtEpNTlWTDcbHKS1IoyVPI7V0Hrd9K3a6QQ7JWnV4BHsuJQ1dYxVJTKaB", adapter=RequestsWebhookAdapter())
webhook.send("Bot is Alive")
while True:
    try:
        URL = 'https://bscscan.com/address/0xcc4f2ba99ef851978103675fe9b582001437e68d'
        source = requests.get(URL).text

        soup = BeautifulSoup(source, 'lxml')
        results = soup.find(id='ContentPlaceHolder1_divSummary')
        price = results.find_all('div', class_='col-md-8')
        split = str(price[1].text).split(' ')
        dollarAmountComma = split[0].split('$')[1]
        beforeConcat = dollarAmountComma.split(',')
        dollarAmount = beforeConcat[0] + beforeConcat[1]
        bnbAmount = split[2]
        if float(dollarAmount) <= 40000:
            print('AHHHHH ITS GETTING LOW')

        print(float(dollarAmount), bnbAmount)
    except AttributeError:
        pass