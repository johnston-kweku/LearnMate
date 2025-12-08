from django.core.mail import send_mail
from django.contrib.auth.models import User
from datetime import date

def send_streak_reminders():
    today = date.today()
    user = User.objects.all()
    for u in user:
        profile = u.userprofile
        last_entry_date = profile.last_entry_date
        if last_entry_date != today:
           send_mail(
               subject='Keep Your Learning Streak Alive!',
                message=(
                    f"Hi {u.username},\n\n"
                    "You haven't added a new topic today. Keep your streak going!\n"
                    "Log in to your account and add a new topic to stay on fire.\n\n"
                    "Best,\n"
                    "The LearnMate Team"
                ),
                from_email='johnstonkweku@gmail.com',
                recipient_list=[u.email],
                fail_silently=False,
           )

           