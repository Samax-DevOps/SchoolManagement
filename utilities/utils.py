from datetime import datetime, timedelta
from pathlib import Path


def get_current_time():
    return str(datetime.now())


def get_one_day_ahead_date():
    d = datetime.now() + timedelta(days=1)
    return d.strftime('%Y-%m-%dT%H:%M')


def get_root_of_project():
    return Path(__file__).parent.parent
