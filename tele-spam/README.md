
# Telegram Spammer Chat Bot
This application is used to send spam messages and images to bank fraud perpetrators who use the Telegram API as a data storage server.


## Features

- Send text messages automatically
- Set the amount of spam
- Attach image link
- Attach a text description of the image


## Usage
#### To use this you have to know how to get the Bot Token and ChatId from the target

Clone the project

```bash
  git clone https://github.com/emRival/TelegramBot-Spammer
```

Go to the project directory

```bash
  cd tele-spam
```

Setup target ```config.txt```

```bash
BotToken= YourTargetTelegramBotToken
ChatID= ChatID
ImageURL= https://example.com/path/to/image.jpg
CaptionText= This is an automatic message with an image.
MessageCount= 5
```

Run the script using the following command:

```bash
  python tele-spam.py
```


## Authors

- [@emRival](https://www.github.com/emRival)

