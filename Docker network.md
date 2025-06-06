
# Урок: Docker Network

Привет, ребята! 👋  
В этом уроке из нашего Docker‑курса погружаемся в **Docker Network**: что это такое, какие бывают драйверы и как с ними работать с помощью команд.
Ссылка на видео: [YouTube](https://youtu.be/ylK1GfBvx0I)
---

## Что такое Docker Network  
Docker Network — это встроенный механизм Docker, который отвечает за организацию сетевого взаимодействия контейнеров между собой и с внешним миром. По умолчанию каждый контейнер подключается к сети `bridge`, но вы можете создавать свои сети с разными драйверами для решения специфичных задач.

---

## Типы сетевых драйверов

- **bridge**  
  Виртуальная локальная сеть, изолированная от хоста. Контейнеры внутри одной сети `bridge` общаются по DNS-именам. Идеально для простых сценариев и разработки на локальной машине.

- **host**  
  Контейнер разделяет сетевой стек с хостом — нет сетевой изоляции. Повышает производительность, но снижает безопасность, так как контейнер «видит» все интерфейсы хоста.

- **none**  
  Полная сетевая изоляция: контейнер запускается без сетевых интерфейсов. Используется для тестов или задач, где не нужен ни входящий, ни исходящий трафик.

- **overlay**  
  Виртуальная сеть, которая может объединять контейнеры на разных Docker‑демонах (например, в Docker Swarm или Kubernetes). Позволяет строить распределённые приложения.

- **macvlan**  
  Контейнер получает собственный MAC‑адрес и выглядит в локальной сети как отдельное физическое устройство. Нужен, когда требуется прямое подключение к сети без NAT.

- **ipvlan**  
  Похож на `macvlan`, но управляет только IP‑адресами на более низком уровне. Поддерживает режимы L2 и L3, меньше накладных расходов по сравнению с `macvlan`.

---

## Описание команд

- `docker network ls`  
  **Что делает:** выводит список всех сетей Docker на текущем хосте: имя, ID, драйвер и статус.  
  **Пример:**  
  ```bash
  docker network ls
  ```

- `docker network create --driver <driver> <name>`  
  **Что делает:** создаёт новую сеть с указанным драйвером.  
  **Пример:**
  ```bash
  docker network create --driver bridge my-bridge-net
  ```  
  Создаст мостовую сеть `my-bridge-net`.

- `docker run -d --name web nginx`  
  **Что делает:** запускает контейнер `nginx` в фоновом режиме (`-d`), присваивает ему имя `web` и подключает к сети `bridge` по умолчанию.  
  **Пример:**
  ```bash
  docker run -d --name web nginx
  ```

- `docker run -it --name client --network my-bridge-net alpine sh`  
  **Что делает:** запускает контейнер `alpine` в интерактивном режиме (`-it`), даёт имя `client` и подключает его к сети `my-bridge-net`.  
  **Пример:**
  ```bash
  docker run -it --name client --network my-bridge-net alpine sh
  ```

- `ping <container-name>`  
  **Что делает:** проверяет сетевое соединение между контейнерами в одной сети, используя встроенный DNS Docker.  
  **Пример:**
  ```bash
  ping web
  ```

- `docker inspect -f '{{ .NetworkSettings.Networks.<network>.IPAddress }}' <container>`  
  **Что делает:** выводит IP‑адрес контейнера в указанной сети.  
  **Пример:**
  ```bash
  docker inspect -f '{{ .NetworkSettings.Networks.bridge.IPAddress }}' web
  ```

- `docker network inspect <network>`  
  **Что делает:** показывает подробную информацию о сети: конфигурация подсетей, параметры драйвера, список подключённых контейнеров.  
  **Пример:**
  ```bash
  docker network inspect bridge
  ```

- `docker run --network none alpine ifconfig`  
  **Что делает:** запускает контейнер без сетевых интерфейсов (драйвер `none`) и выполняет `ifconfig` для проверки отсутствия сети.  
  **Пример:**
  ```bash
  docker run --network none alpine ifconfig
  ```

---

Если урок был полезен, ставьте 👍 и подписывайтесь на канал!  
Пишите ваши вопросы в комментариях — разберём вместе!
