# Описание проекта и его целей.

Разработка и внедрение сервиса прогнозирования дефолта по кредитным картам с контейнеризацией и A/B-тестированием. Проект выполняется в рамках сессионного задания по дисциплине "Внедрение моделей МЛ".

Цель проекта: разработать и внедрить в production-like-среду сервис машинного обучения для прогнозирования дефолта по кредитным картам, который охватывает полный цикл от сохранения модели до организации A/B-тестирования.


# Структура репозитория.
```text
.
├── ab_test_plan.md          # План A/B тестирования модели
│
├── app                      # Основной API
│   ├── api.py               # Flask API: endpoints /predict, /health
│   ├── __init__.py          # Делает app Python-пакетом
│   └── model_handler.py     # Логика загрузки модели и инференса
│
├── data                     # Данные проекта
│   ├── artifacts            # Артефакты после обучения
│   │   ├── features.json    # Список признаков модели
│   │   ├── X_test.csv       # Тестовые признаки
│   │   └── y_test.csv       # Тестовые target-значения
│   │
│   └── UCI_Credit_Card.csv  # Исходный датасет
│
├── docker
│   └── Dockerfile           # Инструкция сборки Docker-образа
│
├── docker-compose.yml       # Запуск контейнеров через docker compose
│
├── models
│   ├── model_v1.pkl         # Обученная модель
│   └── train_model.py       # Скрипт обучения модели
│
├── README.md                # Документация проекта
│
├── requirements.txt         # Python-зависимости
│
└── tests
    └── test_api.py          # Тесты API
```
    
# Инструкция по запуску (локально и в Docker).
## 1. Запуск проекта локально
### 1.1. Скачать репозиторий

git clone https://github.com/troydenys-git/mephi_inception_ML_models_TroyanDI.git

### 1.2. Установить зависимости 

pip install -r requirements.txt

### 1.3. Запустить приложение

python -m app.api

### 1.4. Запустить тест в соседнем терминале

python tests/test_api.py

## 2. Запуск проекта через Docker.
### 2.1. Предварительно выполнить шаги 1.1-1.2

### 2.2. Создать Docker-образ

docker build -t mephi_credit_card_app_troyandi -f docker/Dockerfile .

### 2.3. Запустить тест в соседнем терминале

python tests/test_api.py

# Примеры запросов к API (curl-команды).

Команда для проверки эндпоинта /health. Эндпоинт /predict проверяется через тестовый файл.

 curl http://localhost:5000/health

# Описание формата запросов и ответов.

Запрос:

GET /health

нет тела запроса

Ответ:

{
  "status": "healthy"
}


POST /predict

Запрос

Сервис принимает случайно выбранный сэмпл в формате JSON с признаками клиента из тестовой части датасета UCI Credit Card Default.

Формат входа соответствует обучающему набору X (все признаки, кроме таргета default.payment.next.month).

{
  "LIMIT_BAL": 20000,

  "SEX": 2,

  "EDUCATION": 2,

  "MARRIAGE": 1,

  "AGE": 24,

  "PAY_0": -1,

  "PAY_2": -1,

  "PAY_3": 0,

  ...
}

Особенности:

все поля обязательны,

порядок не важен (он фиксируется через features.json),

типы: int / float

Ответ 

{
  "prediction": 0,

  "probability": 0.12,

  "model_version": "v1",

  "true_label": 0
}

В ответе выводятся: предсказание модели, вероятность класса, версия модели, истинное значение класса.

# Ссылка на Docker-образ в Docker Hub.

https://hub.docker.com/repository/docker/troydenys/mephi_credit_card_app_troyandi/general

docker pull troydenys/my-mephi_credit_card_app_troyandi:latest

# Скриншоты запуска сервиса и тестовых команд
![My Graph](data/artifacts/1.png)

![My Graph](data/artifacts/0.png)