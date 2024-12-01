# heart-telegram-bot
бот для отрисовки сердечка в чате.

## Настройка
Перед настройкой необходимо сгенерировать `API HASH` и `API ID`.
Это можно сделать в [my.telegram.org](https://my.telegram.org/) (раздел API development tools).

Далее:
```sh
$ git clone https://github.com/Fazzyt/heart-telegram-bot.git heart-telegram-bot
$ cd heart-telegram-bot
$ # Отредактируйте config.py
$ python3 -m venv .env
$ . .env/bin/activate  # Каждый раз перед запуском
$ pip install -r requirements.txt
$ python3 __main__.py
```

