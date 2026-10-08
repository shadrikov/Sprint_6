# Sprint_6 Автотесты для учебного сервиса Яндекс.Самокат

Проект представляет собой набор автоматизированных тестов для учебного сервиса, реализованных на стеке **Python + Selenium + pytest + Allure**. Архитектура проекта построена по паттерну **Page Object Model (POM)** с вынесением локаторов в отдельные файлы для удобства поддержки.

## Структура проекта

```text
Sprint_6/
├── allure_results/       # Папка для хранения результатов отчётов Allure
├── locators/             # Локаторы элементов
│   ├── base_page_locators.py
│   ├── home_page_locators.py
│   └── order_page_locators.py
├── pages/                # Page Objects (классы страниц)
│   ├── base_page.py      # Базовый класс со вспомогательными методами
│   ├── home_page.py      # Логика главной страницы
│   └── order_page.py     # Логика страницы заказа
├── tests/                # Тестовые сценарии
│   ├── test_faq.py       # Тесты блока «Вопросы о важном»
│   ├── test_order.py     # Тесты формы заказа
│   └── test_redirects.py # Тесты редиректов
├── .gitignore            # Игнорируемые файлы для git
├── conftest.py           # Фикстуры
├── data.py               # Тестовые данные и константы
├── urls.py               # Базовые URL приложения
├── requirements.txt      # Зависимости проекта
└── README.md             # Документация

## Требования к окружению

Для запуска проекта требуется:
- Python
- Установленный браузер Mozilla Firefox

## Установка и настройка

Установите зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt

## Запуск тестов с генерацией отчёта Allure

Для получения подробного отчёта необходимо добавить флаг --alluredir:
```bash
pytest --alluredir=allure_results

## Просмотр отчёта Allure

После успешного прогона тестов сгенерируйте и откройте отчёт:
```bash
allure serve allure_results