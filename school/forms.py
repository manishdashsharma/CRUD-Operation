from .models import school_database
from django.forms import ModelForm, TextInput


class schoolForm(ModelForm):
    class Meta:
        model = school_database
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            "name":"Name",
            "age":"Age",
            "subjectName":"subjectName",
            "topic":"Topic",
            "image":"Image",
            "video":"Video"
        }