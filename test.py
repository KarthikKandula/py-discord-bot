import requests
import json
import random
import string
# from bot import ping

def get_quote():
    response = requests.get("https://type.fit/api/quotes")
    json_data = json.loads(response.text)
    print(json_data)
    print(len(json_data))

    print(random.randint(0,1642)) 
    print(json_data[random.randint(0,1642)])

    quote = json_data[random.randint(0,1642)]['text'] + " by " + json_data[random.randint(0,1642)]['author']
    print(quote)
    # return(quote)

    ping()

# get_quote()

async def sendVolMsg(msgtosend):
    await ping(msgtosend)

async def testasyncfunc(printtest):
    print(printtest)


def main():
    print("Entered Main!")

    testasyncfunc("Printing from call from main")
    # sendVolMsg("Ping from test!")
