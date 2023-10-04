from lol import LOL
import asyncio

API_KEY = 'K23AVG0UU8B96WR276UA'
API_SECRET = 'PG76UNTD4AOOX3RCFNWWUXNP75NJD3HLK'

async def message_handler(message):
    print(f'Received message: {message}')

async def main():
    lol_client = LOL(API_KEY, API_SECRET, TLS=False)
    await lol_client.connect()
    await lol_client.subscribe('msg')
    await lol_client.bind('msg', 'msg', message_handler)

    try:
        while True:
            await asyncio.sleep(1)  # Keep the event loop running
    except KeyboardInterrupt:
        print('WebSocket connection closed.')

if __name__ == "__main__":
    asyncio.run(main())
