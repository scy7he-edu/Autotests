# Gmail Auto Tests

Проект автоматизированного UI-тестирования (на примере авторизации Google/Gmail) с использованием Python, Pytest и Playwright.
В проекте реализован обход базовых антифрод-систем для успешного прохождения автоматизированного логина.

## Требования (Prerequisites)
* Python 3.10+
* Установленный в системе браузер Google Chrome (тесты настроены на использование локального канала `chrome`, а не стандартного Chromium от Playwright).

## Установка (Installation)

1. Клонируйте репозиторий:
   ```bash
   git clone <url_вашего_репозитория>
   cd gmail_auto_tests
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   # venv\Scripts\activate   # Для Windows
   ```

3. Установите зависимости проекта:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` в корне проекта и заполните его своими тестовыми данными. Пример содержимого `.env` в файле `.env.example`

5. Установите необходимые браузеры Playwright (на всякий случай, если понадобятся системные зависимости):
   ```bash
   playwright install
   ```

## Запуск тестов (Running Tests)

Запуск всех тестов в проекте:
```bash
pytest
```

Для отображения print-логов и подробного вывода можно использовать флаг `-s -v`:
```bash
pytest -s -v
```
