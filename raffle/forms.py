from django import forms

from raffle.models import Raffle


class RaffleForm(forms.ModelForm):


    class Meta:
        fields = '__all__'
        model = Raffle


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Excel de Participantes')
