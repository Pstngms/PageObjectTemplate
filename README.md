# Page Object template
Шаблон для написания UI тестов с использованием паттерна Page Object 

## Инструменты
python3

pytest-selenium

## Запуск

Для работы с данным шаблоном необходимо:

1. Скачать требуемую версию веб-драйвера и поместить в корневую директорию

2. Создать и активировать виртуальное окружение c помощью команд:
    ```
    python -m venv venv

   Windows: venv\Scripts\activate
   
   Linux и MacOS: source venv/bin/activate
    ```
    
3. Установить пакеты с помощью команды:
    ```
    pip install -r requirements
    ```
    
Для запуска тестов используйте команду:
    ```
    python -m pytest -v --driver Chrome --driver-path *chromedriver path* tests/*test_name.py*
    ```
    
    *chromedriver path* - путь до веб-драйвера.

    *test_name.py* - название файла с тестами(в папке tests).

