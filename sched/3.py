import sched, time
from datetime import datetime, timedelta

scheduler = sched.scheduler(time.time, delayfunc=time.sleep)

def soma(n1, n2):
    print(f'Soma: {n1+n2} Tempo: {time.ctime()}')

    scheduler.enterabs((datetime.now() + timedelta(seconds=30)).timestamp(), 1, soma, (2, 2))

def sche():
    scheduler.enterabs(datetime(year=2022, month=6, day=20, hour=17, minute=35).timestamp(), 1, soma, (2, 3))

sche()

scheduler.run()