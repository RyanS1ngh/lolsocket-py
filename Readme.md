# LOLSOCKET-PY  
LOLSOCKET-PY is a Python library for interacting with WebSocket servers using the LOL protocol. It provides an easy-to-use interface to connect to LOL WebSocket servers, subscribe to channels, and handle incoming messages.  

## Installation  

```bash 
pip install lol-websocket-client
```

Usage
-----

```python
from lol import LOL
import asyncio 

API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'

async def message_handler(message): print(f 'Received message: {message}')
async def main():
    lol_client = LOL(API_KEY, API_SECRET, TLS = False) await lol_client.connect() await lol_client.subscribe('msg') await lol_client.bind('msg', 'msg', message_handler) try: while True: await asyncio.sleep(1) # Keep the event loop running     except KeyboardInterrupt:         print('WebSocket connection closed.')  if __name__ == "__main__":     asyncio.run(main())
```

API Reference
-------------

### LOL(API_KEY, API_SECRET, TLS=True)

Initialize a LOL WebSocket client.

*   `API_KEY`: Your LOL API key.
*   `API_SECRET`: Your LOL API secret.
*   `TLS`: Boolean indicating whether to use secure WebSocket (wss) or not. Default is `True`.

#### Methods

*   `async def connect()`: Establish a WebSocket connection to the LOL server.
*   `async def subscribe(channel)`: Subscribe to a specific channel.
*   `async def bind(channel, type, callback)`: Bind a callback function to handle messages of a specific type from a channel.
*   `def trigger(channel, type, message)`: Send a message to a specific channel.

### Example

```python

lol_client = LOL(API_KEY, API_SECRET, TLS=False)
await lol_client.connect() 
await lol_client.subscribe('channel_name') 
await lol_client.bind('channel_name', 'message_type', message_handler) 
lol_client.trigger('channel_name', 'message_type', 'Your message')

```

## TEST KEYS

ApiKey "K23AVG0UU8B96WR27612" ApiSecret "PG76UNTD4AOOX3RCFNWWUXNP75NJD3H22"

License
