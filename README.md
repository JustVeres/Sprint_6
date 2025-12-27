# Sprint_6
Проект 6 спринта, 28_qa-python

```text
Sprint_6/
├── allure-results/                         # Отчёты Allure

├── data/
│   ├── data_important_questions.py         # Тестовые данные для блока "Вопросы о важном"
│   └── data_order_scooter.py               # Тестовые данные для оформления заказа самоката
│   └── data_url.py                         # Тестовые данные с url

├── locators/
│   ├── locators_main_page.py                    # Локаторы главной страницы
│   ├── locators_order_registration_page_one.py  # Локаторы первой страницы заказа
│   ├── locators_order_registration_page_two.py  # Локаторы второй страницы заказа
│   └── locators_order_status_page.py            # Локаторы страницы статуса заказа

├── pages/
│   ├── main_page.py                       # Page Object главной страницы
│   ├── order_registration_page_one.py     # Page Object первой страницы заказа
│   ├── order_registration_page_two.py     # Page Object второй страницы заказа
│   └── order_status_page.py               # Page Object страницы статуса заказа

├── tests/
│   ├── test_check_redirect_after_ordering.py  # Проверка редиректа после оформления заказа
│   ├── test_important_questions.py            # Тесты блока "Вопросы о важном"
│   └── test_ordering_scooter.py               # Тесты оформления заказа самоката
│
├── requirements.txt                       # Подключённые библиотеки
├── conftest.py                            # Фикстуры pytest
└── README.md                              # Описание проекта
