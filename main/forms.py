from .models import TableReservation
from django.forms import ModelForm, TextInput, TimeInput, EmailInput, NumberInput


class TableReservationForm(ModelForm):
    class Meta:
        model = TableReservation
        fields = ["name", "tableNumber", "reservationTime", "email"]
        widgets = {
            "name": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Введите ваше имя'
            }),
            "tableNumber": NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Введите номер желаемого столика'
            }),
            "reservationTime": TimeInput(attrs={
                'class': "form-control",
                'placeholder': 'Выберите желаемое время брони'
            }),
            "email": EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Введите ваш email'
            })
        }
