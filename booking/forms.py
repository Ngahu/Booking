from django import forms

from .models import Book
from .models import profile

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "where_from",
            "where_to",
            "date_travelling",
            "class_of_choice",
            "travelling_persons",
            "kids",
        ]

#class BookForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super(BookForm,self).__init__(*args,**kwargs)
   #     for field in iter(self.fields):
  #          self.fields[field].widget.attrs.update({
 #               'class':'form-control'
#            })



class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        exclude = ('user',)

