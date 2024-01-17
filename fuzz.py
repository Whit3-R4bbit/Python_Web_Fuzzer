import requests
import asyncio

async def send_request(path):
    
    response = requests.get("https://www.wikipedia.org/" + path)
    print(response.url + " " + str(response.status_code))
    

async def main():

    f = open("common.txt", "r")
    for x in f:
        x = x.strip()
        asyncio.create_task(send_request(x))      

asyncio.run(main())
