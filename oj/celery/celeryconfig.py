from __future__ import absolute_import
import os
from celery import Celery

# set to ensure setting is loaded before calling
os.environ['DJANGO_SETTINGS_MODULE'] = 'oj_fun.settings'

app = Celery('oj')

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379',
    CELERY_ACCEPT_CONTENT = ['application/json'],
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_RESULT_SERIALIZER = 'json',
    CELERY_TIMEZONE = 'Africa/Nairobi',
    CELERYD_CONCURRENCY = 2,
    CELERY_IMPORTS = ("oj.views.testViews", )
    )

if __name__ == '__main__':
    app.start()






