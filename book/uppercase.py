from django.core.exceptions import ValidationError


def uppercase(value):
    if not value[0].isupper():
        raise ValidationError('Введите название с заглавной буквы!')
