from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # The field that are present in Room Models or we can specify single field ['name' ,'body']
          