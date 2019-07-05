from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print("tick!!!")

# sched = BlockingScheduler()
sched = BackgroundScheduler()
sched.add_job(tick, 'interval', seconds=3)
sched.start()

while True:
    pass
