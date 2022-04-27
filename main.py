import asyncio
import random
import string

from telethon.sync import TelegramClient


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
destination = '@mephiFacesbot'


async def send_greetings(count: int):
    async with TelegramClient("tester", api_id, api_hash) as client:
        for i in range(count):
            await client.send_message(destination, '/start')


async def send_some_text(count: int):
    async with TelegramClient("tester", api_id, api_hash) as client:
        for i in range(count):
            rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            await client.send_message(destination, rand_str)


async def send_some_photo(count: int):
    async with TelegramClient("tester", api_id, api_hash) as client:
        for i in range(count):
            await client.send_file(destination, f"./static/pic{random.randint(1, 8)}.png")


async def main():
    await send_some_text(200)
    await send_greetings(200)
    await send_some_photo(200)


asyncio.run(main())
