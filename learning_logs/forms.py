from django import forms 
from .models import Topic, Entry
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']
        labels = {'topic_name': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entry']
        labels = {'entry': ''}
        widgets = {'entry': forms.Textarea(attrs={'cols':80})}

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        