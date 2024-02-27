import aiohttp
import asyncio

async def fetch_google():
    url = 'https://www.google.com'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            headers = response.headers
            status_code = response.status
            status_message = response.reason
            response_text = await response.text()

            print("Headers:")
            print(headers)
            print("\nResponse Code:", status_code)
            print("Response Message:", status_message)
            print("\nResponse Text:")
            print(response_text)

async def main():
    await fetch_google()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
