![workflow status](https://github.com/solodnikov/scrapy_parser_pep/actions/workflows/main.yml/badge.svg?event=push&branch=master)

# scrapy_parser_pep
 Парсер PEP документации с сайта peps.python.org  

## Описание
Асинхронный парсер, написанный с использованием фреймворка Scrapy, осуществляет сбор информации с официального сайта с PEP стандартами Python:
<https://peps.python.org/>

Данные собираются в формате "Номер PEP, Название, Актуальный статус" и записываются в CSV файл.
Также выполняется анализ собранных данных и подсчет количества стандартов в каждом статусе и общего кол-ва стандартов. Результат анализа записывается в отдельный CSV файл.

## Технологии
* Python 3.9
* Scrapy 2.5.1


## Подготовка парсера к работе

1. Cклонируйте репозиторий на свой локальный компьютер
```
git clone https://github.com/Solodnikov/scrapy_parser_pep.git
```

2. Создайте виртульное окружение и активируйте его, установите зависимости
```
python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
```

3. Запустите парсер - после завершения работы результат будет сохранен в виде csv файлов в директории results
```
scrapy crawl pep
```
