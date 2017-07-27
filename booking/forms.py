from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "where_from",
            "where_to",
            "date_travelling",
            "type_of_ticket",
            "class_of_choice",
            "travelling_persons",
            "kids",
        ]
