Парсер документов PEP на базе фреймворка Scrapy.

Парсер выводит собранную информацию в два csv файла:
- Список всех PEP: номер, название и статус.
- Сводка по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).

В качестве стартовой ссылки установлена https://peps.python.org/

# Как запустить проект:
## Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/nu-shtosh/ScrapyPepParse
```
```
cd api_yambd
```
## Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
## Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
## Запустите парсер:
```
scrapy crawl pep
```
![Python]
(https://camo.githubusercontent.com/9e4f14dd191ddc455ee50765b7045333002f3856f195668d4a1aba421f124c18/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2532302d2532333165343135652e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)
