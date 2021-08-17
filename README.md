# Foodgram "Продуктовый помощник"

Проект Foodgram "Продуктовый помощник" включает в себя онлайн-сервис и API для него. На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное».

## Отличительной особенностью данного сервиса является возможность добавлять рецепты в "Список покупок" и скачать суммированный список продуктов перед походом в магазин.

### Технологии:
- PostgreSQL
- nginx
- Python 3.8.5
- Git (GitHub repository)
- Docker (Docker hub repository)
--- 

### Установка и запуск:
1. Клонируйте репозиторий с проектом 
```bash
git clone https://github.com/n18qpc/foodgram-project-react.git
```
2. На сервере проекта установите `doker` и `docker-compose`
```bash 
sudo apt install docker.io 
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
3. Подготовка к запуску:
Скопируйте подготовленные файлы `docker-compose.yaml` и `nginx/default.conf` из вашего проекта на сервер в `home/<ваш_username>/docker-compose.yaml` и `home/<ваш_username>/nginx/default.conf` соответственно.
Создайте файл `.env` со своими переменными окружения
Пример:
```
DB_NAME=postgres
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=<your_password>
DB_HOST=db
DB_PORT=5432
```
4. Запуск `docker-compose`:
```bash
docker-compose up -d --build
docker-compose exec backend python manage.py makemigrations --noinput
docker-compose exec backend python manage.py migrate --noinput
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input 
```
---
![example workflow](https://github.com/n18qpc/foodgram-project-react/actions/workflows/Foodgram_workflow.yml/badge.svg)

Доступно по адресу 217.28.231.148

админка:
admin admin
admin@ad.com

Авторство github.com/n18qpc
---
