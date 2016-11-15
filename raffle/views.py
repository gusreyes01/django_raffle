from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from raffle.forms import UploadFileForm, RaffleForm
from raffle.models import Raffle
from raffle.uploads import handle_uploaded_file


def home(request, pk):
    raffle = Raffle.objects.get(pk=pk)
    return render(request, 'raffle/home.html', locals())


def list(request):

    raffles = Raffle.objects.all()
    return render(request, 'raffle/list.html', locals())


def create(request):
    form = UploadFileForm()
    raffle_form = RaffleForm()

    if request.method == 'POST':
        obj = Raffle()
        obj.save()
        handle_uploaded_file(request, request.FILES['file'], obj)
        messages.success(request, "Sorteo creado exitosamente.")
        return redirect(reverse('list'))

    return render(request, 'raffle/create_raffle.html', locals())
