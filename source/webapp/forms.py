from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Issue, Project
from django.core.validators import MaxLengthValidator, MinLengthValidator


def min_len_validator(string):
    if len(string) < 2:
        raise ValidationError('Заголовок должен быть длинее 2-ух символов')
    return string


def letters_capital_validator(string):
    if string != string.capitalize():
        raise ValidationError('Строка должна начинаться с большой буквы')


class IssueForm(forms.ModelForm):
    summary = forms.CharField(validators=(MaxLengthValidator(
        limit_value=50,
    ), min_len_validator, letters_capital_validator))
    description = forms.CharField(widget=forms.Textarea, validators=(MinLengthValidator(
        limit_value=2,
    ), letters_capital_validator))

    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Заголовок задачи',
            'description': 'Описание задачи',
            'status': 'Статус',
            'type': 'Тип'
        }


class ProjectForm(forms.ModelForm):
    started_at = forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}))
    finished_at = forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Project
        fields = ('name', 'description', 'started_at', 'finished_at')
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'started_at': 'Дата начала',
            'finished_at': 'Дата окончания'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')
