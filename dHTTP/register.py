import aiohttp
import typing
import asyncio


class Register:
    def __init__(self, app_id: int, headers: dict):
        self.headers = headers
        self.app_id = app_id
        self.session = aiohttp.ClientSession(headers=headers)

    async def global_commands(self, json: dict):

        try:
            await self.session.post(
                f"https://discord.com/api/v8/applications/{self.app_id}/commands",
                json=json,
            )

        except Exception as e:
            print(f"An exception occured: {e}")
