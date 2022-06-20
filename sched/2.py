"""Marcar um evento em um tempo específico"""
import sched, time
from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)

def rescheduler():
    """Zere os segundos da hora atual e some mais 1 minuto"""
    new_target = datetime.now().replace(second=0, microsecond=0)
    new_target += timedelta(minutes=1)
    print(new_target)

    scheduler.enterabs(new_target.timestamp(), priority=1, action=saytime)


def saytime():
    print(time.ctime())
    rescheduler()

"""def google_request():
    from requests import get
    print(get('http://google.com').text)
    rescheduler()"""

rescheduler()

scheduler.run(blocking=True)