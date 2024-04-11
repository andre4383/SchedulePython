import helper
import schedule
import time


def job():
    print("Estudar!")


#schedule.every().day.at("14:30").do(job)
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)