from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession, CreateNewSession
import asyncio


async def main():
    tdataFolder = r"C:\Users\root\progs\Portable\Telegram\tdata"
    tdesk = TDesktop(tdataFolder)

    assert tdesk.isLoaded(), "Ошибка загрузки tdata. Убедитесь, что путь указан верно."

    client = await tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession)

    await client.connect()

    if not await client.is_user_authorized():
        print("Не удалось авторизоваться. Проверьте данные tdata.")
        return

    bot_username = "woodyvpn_bot"
    start_parameter = "prettyboyclique"

    await client.send_message(bot_username, f"/start {start_parameter}")
    print("Сообщение отправлено боту!")

    await client.disconnect()


asyncio.run(main())
