import requests
from bs4 import BeautifulSoup
from discord import Webhook, RequestsWebhookAdapter
import schedule
import time


def checkPrice():
    prevDayPrice = 66567.72
    count = 0
    webhook = Webhook.from_url(
        "https://discord.com/api/webhooks/825460904938307645/LEpZCep1GtYTtEpNTlWTDcbHKS1IoyVPI7V0Hrd9K3a6QQ7JWnV4BHsuJQ1dYxVJTKaB", adapter=RequestsWebhookAdapter())
    webhook.send("Bot is Alive")

    while True:
        # Set 24 hour timer to push the daily changes in TVL

        try:
            URL = 'https://bscscan.com/address/0xcc4f2ba99ef851978103675fe9b582001437e68d'
            source = requests.get(URL).text
            soup = BeautifulSoup(source, 'lxml')
            results = soup.find(id='ContentPlaceHolder1_divSummary')
            price = results.find_all('div', class_='col-md-8')
            split = str(price[1].text).split(' ')
            dollarAmountComma = split[0].split('$')[1]
            beforeConcat = dollarAmountComma.split(',')

            dollarAmount = float(beforeConcat[0] + beforeConcat[1])
            bnbAmount = split[2]

            if dollarAmount <= 60000:
                webhook.send(
                    'AHHHHH ITS GETTING LOW: ${}'.format(dollarAmount))
            elif dollarAmount <= 30000:
                webhook.send(
                    'AHHHHH ITS GETTING LOWER: ${}'.format(dollarAmount))
            elif dollarAmount <= 40000:
                webhook.send(
                    'AHHHHH ITS GETTING EVEN LOWER: ${}'.format(dollarAmount))

            if count == 1440:
                percent = float(
                    ((dollarAmount - prevDayPrice)/abs(prevDayPrice))*100)
                percent = round(percent, 2)
                webhook.send("Daily Percent Gain is {} from {} to {}".format(
                    percent, prevDayPrice, dollarAmount))
                prevDayPrice = dollarAmount
                count = 0
            if count % 50 == 0:
                webhook.send("Current TVL in $: {}".format(dollarAmount))

            time.sleep(60)
            count += 1
        except AttributeError:
            pass
    webhook.send("Killed")


def main():
    checkPrice()


if __name__ == "__main__":
    main()
