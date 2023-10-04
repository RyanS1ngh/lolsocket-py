import asyncio
import json
import websockets
from lib.Auth import verify_token

class LOL:
    def __init__(self, API_KEY, API_SECRET, TLS=True):
        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.token = None
        self.user_id = None
        self.channels = {}

        if TLS:
            self.url = f"wss://ws.kolabi.pro:4000/{API_KEY}"
        else:
            self.url = f"ws://ws.kolabi.pro:3000/{API_KEY}"
        self.socket = None

    async def connect(self):
        self.socket = await websockets.connect(self.url)
        print("connected")

    async def subscribe(self, channel):
        channel_key = f"{self.api_key}-{channel}"
        data = {
            "type": "subscribe",
            "channel": channel,
            "secret": self.api_secret,
            "token": self.token
        }
        await self.socket.send(json.dumps(data))
        if channel_key not in self.channels:
            self.channels[channel_key] = []

    async def bind(self, channel, type, callback):
        await self.subscribe(channel)
        channel_key = f"{self.api_key}-{channel}"

        async def listen():
            async for message in self.socket:
                parsed_message = json.loads(message)
                message_type = parsed_message.get("emit_type")
                message_data = parsed_message.get("content")
                for subscription in self.channels[channel_key]:
                    if subscription.get("type") == message_type:
                        await callback(message_data)  # Await the callback function

        self.channels[channel_key].append({
            "type": type,
            "callback": callback
        })

        asyncio.ensure_future(listen())

    def trigger(self, channel, type, message):
        is_client = channel.startswith('client-')
        if is_client:
            data = {
                "type": "client-publish",
                "emit_type": type,
                "channel": channel,
                "content": message,
                "secret": self.api_secret,
                "userId": self.user_id,
                "token": self.token
            }
        else:
            data = {
                "type": "publish",
                "emit_type": type,
                "channel": channel,
                "content": message,
                "secret": self.api_secret,
                "userId": self.user_id,
                "token": self.token
            }
        asyncio.get_event_loop().run_until_complete(self.socket.send(json.dumps(data)))

    def set_token(self, token):
        self.token = token
        user_id = verify_token(token, self.api_secret)
        if user_id:
            self.user_id = user_id
        else:
            print("Invalid token, connection closed.")
            asyncio.get_event_loop().run_until_complete(self.socket.close())
