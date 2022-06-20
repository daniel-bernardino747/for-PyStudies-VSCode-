import sched
import time

scheduler = sched.scheduler()

def saytime():
    print(time.ctime())
    scheduler.enter(delay=10, priority=2, action=saytime)


def hello():
    print('Hello!')
    scheduler.enter(delay=5, priority=1, action=hello)

def start():
    scheduler.enter(delay=5, priority=1, action=hello)
    scheduler.enter(delay=10, priority=2, action=saytime)

start()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('parei com sched')