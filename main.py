from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession, CreateNewSession
import asyncio


async def main():
    tdataFolder = r"path\to\Portable\Telegram\tdata"
    tdesk = TDesktop(tdataFolder)

    assert tdesk.isLoaded(), "Failed loading tdata. Check tdataFolder path."

    client = await tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession)

    await client.connect()

    if not await client.is_user_authorized():
        print("Authorization failed. Check your tdata.")
        return

    bot_username = "referal_bot_username"
    start_parameter = "todo_telegram_account_username"

    await client.send_message(bot_username, f"/start {start_parameter}")
    print("Message successfully sent!")

    await client.disconnect()


asyncio.run(main())
