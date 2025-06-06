from django import forms
from .models import Topic, Entry    

class TopicForm(forms.ModelForm):
    """A form for creating or updating a topic."""
    
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # No label for the text field
        widgets = {  'text': forms.TextInput(attrs={'placeholder': 'Enter topic here...'})
        }

class EntryForm(forms.ModelForm):
     class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}