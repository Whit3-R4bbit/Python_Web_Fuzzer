import requests
import asyncio
import aiohttp
import time

async def send_request(session, path):
    
    async with session.get("http://localhost:8080/" + path) as resp:
        return resp
    

async def main():

    f = open("common.txt", "r")
    
    async with aiohttp.ClientSession() as session:
        value = [send_request(session, path) for path in f]
        results = await asyncio.gather(*value)
        


if __name__ == "__main__":
    starttime = time.time()
    asyncio.run(main())
    print(time.time() - starttime)
