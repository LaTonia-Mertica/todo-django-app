from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '   enter task', 'style': 'width:90%'}), 
    label = '', max_length = 255)

class NoteForm(forms.Form):
    notes = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 99.25%', 'placeholder': '   enter note'}), max_length= 444, label = '')

