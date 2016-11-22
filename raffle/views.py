import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from raffle.forms import UploadFileForm, RaffleForm
from raffle.models import Raffle
from raffle.uploads import handle_uploaded_file


def home(request, pk):
    raffle = Raffle.objects.get(pk=pk)
    return render(request, 'raffle/home.html', locals())


def list(request):
    raffles = Raffle.objects.all()
    return render(request, 'raffle/list.html', locals())


@csrf_exempt
def results(request, pk):
    if request.is_ajax():
        raffle = Raffle.objects.get(pk=pk)
        res = json.loads(request.body)
        print(res)
        raffle.results = res
        raffle.save()
        return HttpResponse('success')


def winner(request, pk):
    raffle = Raffle.objects.get(pk=pk)
    return render(request, 'raffle/winner.html', locals())


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
