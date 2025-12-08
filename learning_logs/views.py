from django.shortcuts import render
from .models import Topic, Entry, UserProfile
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import timedelta, datetime, date
from django.contrib import messages

# Create your views here.


def index(request):
    """The home page for learning_logs."""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    # Show all topics.
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all it's entries."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # No form submitted, create a blank form
        form = TopicForm()

    else:
        # POST data submitted.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            user_profile = request.user.userprofile
            today = date.today()
            last_entry_date = user_profile.last_entry_date
            streak = user_profile.current_streak

            if last_entry_date == today:
                pass
            elif last_entry_date == today - timedelta(days=1):
                streak += 1
            else:
                streak = 1

            user_profile.current_streak = streak
            user_profile.last_entry_date = today
            user_profile.save()

            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add new entryfor a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        """No data submitted; create blank form"""
        form = EntryForm()
    else:
        # Post data sumbitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; prefill form with current entry
        form = EntryForm(instance=entry)

    else:
        # Post data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def about(request):
    return render(request, 'learning_logs/about.html')


def extras(request):
    return render(request, 'learning_logs/extras.html')


def robots_txt(request):
    content = "User-agent: *\nDisallow:\nSitemap: https://learning-log-django.onrender.com/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")


@login_required
def dashboard(request):
    topics = Topic.objects.filter(owner=request.user)
    topic_length = topics.count()

    profile, created = UserProfile.objects.get_or_create(user=request.user)

    today = date.today()
    streak = profile.current_streak
    last_entry_date = profile.last_entry_date

    if not request.user.email:
        messages.info(request, "Please update your email to receive streak reminders!")


    context = {
        'topic_length': topic_length,
        'today': today,
        'streak': streak,
        'last_entry_date': last_entry_date,
    }

    return render(request, 'learning_logs/dashboard.html', context)
