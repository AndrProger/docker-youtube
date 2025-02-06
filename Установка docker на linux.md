### README: Установка Docker на Linux (Ubuntu/Debian)

# 🐳 Установка Docker на Linux – Полное руководство
Ссылка на видео [YouTube](https://youtu.be/ozEXL4JnedE)

## 📌 Описание
В этом руководстве подробно разбирается процесс установки Docker на Linux (Ubuntu/Debian), начиная с обновления системы и удаления старых версий, до проверки работоспособности Docker и устранения возможных ошибок.

## 🛠️ Системные требования
Перед установкой Docker убедитесь, что ваш компьютер соответствует следующим требованиям:
- Ubuntu 20.04 / 22.04 или Debian 10 / 11
- Поддержка WSL 2 (если используется Windows)
- Включенная виртуализация (BIOS/UEFI)
- Минимум 4 ГБ оперативной памяти

## 🚀 Установка Docker

1. **Обновите систему перед установкой:**  
   *sudo apt update*  
   *sudo apt upgrade*

2. **Удалите старые версии Docker (если они установлены):**  
   *sudo apt remove docker docker-engine docker.io containerd runc*

3. **Добавьте официальные репозитории Docker:**  
   *sudo apt install -y apt-transport-https ca-certificates curl software-properties-common*

   *curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg*

   *echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null*

4. **Установите Docker:**  
   *sudo apt update*  
   *sudo apt install -y docker-ce docker-ce-cli containerd.io*

5. **Проверьте версию установленного Docker:**  
   *sudo docker --version*

6. **Добавьте пользователя в группу Docker, чтобы запускать Docker без `sudo` (необязательно, но удобно):**  
   *sudo usermod -aG docker $USER*  
   *newgrp docker*

7. **Запустите тестовый контейнер для проверки установки:**  
   *docker run hello-world*

8. **Проверьте список контейнеров:**  
   *docker ps -a*

## 🎯 Заключение
Теперь Docker установлен и готов к работе! 🚀  
Если у вас возникли вопросы, пишите в **Issues** или оставляйте комментарии.

✅ **Полезные ссылки:**
- [Официальная документация Docker](https://docs.docker.com/)
- [Скачать Docker](https://www.docker.com/products/docker-desktop/)

⭐ Если это руководство было полезным, поставьте **звезду на GitHub**!