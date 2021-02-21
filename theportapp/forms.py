from django.utils import timezone
from .models import Messenger
from django import forms

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messenger
        fields = ('name', 'email', 'message')
