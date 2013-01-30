from django.forms.models import ModelForm
from models import Book


# use a special form where author is excluded from form and get from url
class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('author',)
