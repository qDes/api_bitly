# Скрипт для сокращения ссылок и получения количества переходов по коротким ссылкам.

## Требования
Python 3. <br>
Установка зависимостей
```bash
pip3 install -r requirements.txt
```
Для работы скрипта необходимо добавить токен сервиса bit.ly (Generic Access Token) в переменную окружения TOKEN.
## Использование
При запуске скрипта необходимо указать ссылку для сокращения или для подсчёта переходов короткой ссылку.<br>
### Примеры использования
Запрос с валидной короткой ссылкой в качестве аргумента вернёт общее количество переходов по данной ссылке.
```bash
python3 bitly.py --link bit.ly/2PmLzpz
```
Запрос с валидной ссылкой в качестве аргумента вернёт укороченную ссылку.
```bash
python3 bitly.py --link dvmn.org/modules/
```