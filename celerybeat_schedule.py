from celery import Celery # type: ignore
from celery.schedules import crontab # type: ignore

app = Celery(
    'crawler_scheduler',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/1'
)

# Cấu hình lịch chạy
app.conf.beat_schedule = {
    'run-example-spider-every-1-minute': {
        'task': 'tasks.run_spider',   # Tên task
        'schedule': crontab(minute="*/1"),  # Lặp lại sau mỗi phút
    },
}

# Timezone (nếu cần)
app.conf.timezone = 'Asia/Ho_Chi_Minh'
