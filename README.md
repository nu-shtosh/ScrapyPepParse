Парсер документов PEP на базе фреймворка Scrapy.

Парсер выводит собранную информацию в два csv файла:
- Список всех PEP: номер, название и статус.
- Сводка по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).

В качестве стартовой ссылки установлена https://peps.python.org/.

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/nu-shtosh/ScrapyPepParse
```
```
cd api_yambd
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
