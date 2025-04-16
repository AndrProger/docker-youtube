# Docker Volumes и Bind Mounts – Практическое руководство

В этом уроке мы разберём, что такое Docker Volumes и Bind Mounts, зачем они нужны и как с ними работать на практике.
Ссылка на видео: [YouTube](https://youtu.be/vIey0mLCVK8)

## 📌 Что такое Volume и Bind Mount?

В Docker есть два основных способа сохранять данные контейнеров:

- **Volume** – это удобный, абстрактный способ хранения данных. Docker управляет местоположением данных сам (обычно они хранятся в `/var/lib/docker/volumes`).
- **Bind Mount** – вы вручную указываете конкретный путь на вашем компьютере, например, папку на рабочем столе.

## ⚙️ Основные отличия:

- **Volume** – проще и универсальнее, подходит для большинства случаев.
- **Bind Mount** – точнее и удобнее, если вам нужно напрямую работать с файлами на хосте.

---

## 🚀 Практические шаги:

### 1. Создание Docker Volume
```powershell
docker volume create pg-data
docker volume ls
```

### 2. Запуск контейнера PostgreSQL с Volume
```powershell
docker run -d --name pg-container -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=testdb -v pg-data:/var/lib/postgresql/data -p 5432:5432 postgres:latest
```

### 3. Тестирование данных в PostgreSQL
Создаём таблицу и добавляем данные для проверки:

```sql
-- Создаем таблицу employees
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    hire_date DATE
);

-- Добавляем данные
INSERT INTO employees (first_name, last_name, hire_date) VALUES
('John', 'Doe', '2023-01-15'),
('Jane', 'Smith', '2022-06-30'),
('Alice', 'Johnson', '2024-02-01');
```

### 4. Создание контейнера с Bind Mount
```powershell
docker run -d `
  --name nginx-container `
  -v "C:/Users/User/Documents/site:/usr/share/nginx/html" `
  -p 8080:80 `
  nginx:latest
```

Теперь папка на вашем компьютере напрямую связана с контейнером Nginx!

---

## 🗃️ Проверка сохранения данных

Если вы удалите контейнер PostgreSQL и пересоздадите его с тем же Volume, данные останутся целыми.

### Удаление контейнера:
```powershell
docker stop pg-container; docker rm pg-container
```

### Повторный запуск контейнера (данные сохраняются!):
```powershell
docker run -d --name pg-container -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=testdb -v pg-data:/var/lib/postgresql/data -p 5432:5432 postgres:latest
```

---

## 🛠️ Удаление Docker Volume

Если Volume больше не нужен:
```powershell
docker volume rm pg-data
```

_Важно:_ Volume нельзя удалить, если он используется контейнером!

---

## 🎯 Итоги урока:

- Узнали разницу между Volume и Bind Mount.
- Научились создавать и подключать Docker Volume.
- Проверили, что данные сохраняются после пересоздания контейнера.
- Поняли, когда удобнее использовать Bind Mount.

Теперь вы можете уверенно управлять данными своих Docker-контейнеров!

