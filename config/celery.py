import os   # os - это модуль, которая помогает нам работать с ОС (с убунту и этим проектом )
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") # путь до наших настроек

app = Celery('config') # создали экземпляр от celery (celery - это класс), 'config' - название нашей директории, где находится наши настройки

app.config_from_object('django.conf:settings',namespace='CELERY') # загрузили настройки селери

app.autodiscover_tasks()  # метод позволяет селери самому автоматически искать таски и запускать их
