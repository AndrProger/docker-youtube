# 1. Выбор базового образа
FROM python:3.9-slim

# 2. Добавление метаданных (опционально)
LABEL maintainer="your_email@example.com"
LABEL version="1.0"
LABEL description="Пример Dockerfile для простого Flask-приложения"

# 3. Задание переменных окружения для Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Определение рабочей директории в контейнере
WORKDIR /app

# 5. Копирование файла зависимостей в рабочую директорию
COPY requirements.txt /app/

# 6. Установка зависимостей
RUN pip install --upgrade pip && pip install -r requirements.txt

# 7. Копирование исходного кода приложения в контейнер
COPY . /app

# 8. Открытие порта 5000 для работы приложения
EXPOSE 5000

# 9. Определение команды для запуска приложения
CMD ["python", "app.py"]
