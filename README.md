# Sprint_6
Проект 6 спринта, 28_qa-python

```text
Sprint_6/
├── allure-results/                            # Отчёты Allure

├── data/
│   ├── data_important_questions.py            # Тестовые данные для блока "Вопросы о важном"
│   └── data_order_scooter.py                  # Тестовые данные для оформления заказа самоката
│   └── data_url.py                            # Тестовые данные с url

├── locators/
│   ├── locators_main_page.py                  # Локаторы главной страницы
│   ├── locators_order_page.py                 # Локаторы страниц заказа

├── pages/
    ├── base_page.py                           # Page Object общих элементов страницы
│   ├── main_page.py                           # Page Object главной страницы
│   ├── order_page.py                          # Page Object страниц заказа

├── tests/
│   ├── test_check_redirect_after_ordering.py  # Проверка редиректа после оформления заказа
│   ├── test_important_questions.py            # Тесты блока "Вопросы о важном"
│   └── test_ordering_scooter.py               # Тесты оформления заказа самоката
│
├── requirements.txt                           # Подключённые библиотеки
├── conftest.py                                # Фикстуры pytest
└── README.md                                  # Описание проекта
