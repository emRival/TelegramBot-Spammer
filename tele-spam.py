import asyncio
import requests
from io import BytesIO
from telegram import Bot
from telegram.error import TelegramError

def read_config(file_path="config.txt"):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split("=")
            config[key] = value
    return config

async def send_photo_from_url(bot_token, chat_id, photo_url, caption=""):
    bot = Bot(token=bot_token)

    try:
        response = requests.get(photo_url)
        if response.status_code == 200:
            photo = BytesIO(response.content)
            message = await bot.send_photo(chat_id=chat_id, photo=photo, caption=caption)
            print(f"✅ Foto berhasil dikirim ke {chat_id} dengan ID pesan: {message.message_id}")
        else:
            print(f"❌ Gagal mengunduh gambar dari {photo_url}, status code: {response.status_code}")
    except TelegramError as e:
        print(f"❌ Terjadi kesalahan saat mengirim foto: {e}")
    except Exception as e:
        print(f"❌ Kesalahan umum: {e}")

async def main():
    config = read_config()

    bot_token = config.get("BotToken")
    chat_id = config.get("ChatID")
    image_url = config.get("ImageURL")
    caption_text = config.get("CaptionText")
    message_count = int(config.get("MessageCount", 1))

    tasks = [send_photo_from_url(bot_token, chat_id, image_url, caption=caption_text) for _ in range(message_count)]
    await asyncio.gather(*tasks)

    print(f"🎉 Semua pesan ({message_count}) berhasil dikirim ke {chat_id}!")

if __name__ == '__main__':
    asyncio.run(main())
