import requests
from io import BytesIO
from telegram import Bot
from telegram import InputFile

def send_photo_from_url(bot_token, chat_id, photo_url, caption=""):
    bot = Bot(token=bot_token)
    
    response = requests.get(photo_url)
    if response.status_code == 200:
        photo = BytesIO(response.content)
        bot.send_photo(chat_id=chat_id, photo=photo, caption=caption)
    else:
        print(f"Failed to download image from {photo_url}")

def read_config(file_path="config.txt"):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split("=")
            config[key] = value
    return config

if __name__ == '__main__':
    config = read_config()

    bot_token = config.get("BotToken")
    chat_id = config.get("ChatID")
    image_url = config.get("ImageURL")
    caption_text = config.get("CaptionText")
    message_count = int(config.get("MessageCount", 1))

    # Loop untuk mengirim gambar sebanyak yang diinginkan
    for _ in range(message_count):
        send_photo_from_url(bot_token, chat_id, image_url, caption=caption_text)

    print(f"Messages sent successfully to chat ID {chat_id}.")
