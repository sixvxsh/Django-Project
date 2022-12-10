from django import forms
from django.forms import ModelForm
from .models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()

class TodoUpateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title' , 'body', 'created')
        #if we use all of the fields of model we can use this method:
        #fields = '__all__'