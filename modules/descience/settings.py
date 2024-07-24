# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'calculate-contributions': {
        'task': 'your_app.tasks.calculate_contributions',
        'schedule': crontab(hour=0, minute=0),  # Run daily at midnight
    },
    'distribute-sg-tokens': {
        'task': 'your_app.tasks.distribute_sg_tokens',
        'schedule': crontab(day_of_month=1, hour=0, minute=0),  # Run monthly
    },
}
