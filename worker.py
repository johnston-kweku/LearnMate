import time
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
django.setup()

from learning_logs.tasks import send_streak_reminders

def run_worker():
    while True:
        print("Running worker task: sending streak reminders...")
        send_streak_reminders()

        # WAIT BEFORE NEXT RUN
        # You can change this interval
        time.sleep(60 * 60 * 24)  # runs every 1 hour

if __name__ == "__main__":
    run_worker()
