from rubpy import Client
from datetime import datetime
import asyncio

client = Client("session")

async def update_bio():
    while True:
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%Y-%m-%d")
        newbio = f"📅 {date_str} | ⏰ {time_str}"

        try:
            await client.update_profile(bio=newbio)
            print(f"بیوگرافی آپدیت شد: {newbio}")
        except Exception as e:
            print(f"خطا در آپدیت بیو: {e}")

        await asyncio.sleep(60)

async def main():
    await client.start()
    try:
        await update_bio()
    finally:
        await client.stop()

asyncio.run(main())