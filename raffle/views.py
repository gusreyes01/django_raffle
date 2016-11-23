import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from raffle.forms import UploadFileForm, RaffleForm
from raffle.models import Raffle, Banner
from raffle.uploads import handle_uploaded_file
from excel_utilities import WriteToExcel


def home(request, pk):
    banner = Banner.objects.all().latest('pk')
    raffle = Raffle.objects.get(pk=pk)
    return render(request, 'raffle/home.html', locals())


def list(request):
    banner = Banner.objects.all().latest('pk')
    raffles = Raffle.objects.all()
    return render(request, 'raffle/list.html', locals())


@csrf_exempt
def results(request, pk):
    if request.is_ajax():
        raffle = Raffle.objects.get(pk=pk)
        res = json.loads(request.body)
        raffle.results = res
        raffle.save()

        payload = {'success': True}
        return HttpResponse(json.dumps(payload), content_type='application/json')


@csrf_exempt
def save_winner(request, pk):
    if request.is_ajax():
        raffle = Raffle.objects.get(pk=pk)
        res = json.loads(request.body)
        raffle.winner = res
        raffle.save()

        payload = {'success': True}
        return HttpResponse(json.dumps(payload), content_type='application/json')



def winner(request, pk):
    banner = Banner.objects.all().latest('pk')
    raffle = Raffle.objects.get(pk=pk)
    return render(request, 'raffle/winner.html', locals())


def create(request):
    banner = Banner.objects.all().latest('pk')
    form = UploadFileForm()
    raffle_form = RaffleForm()

    if request.method == 'POST':
        obj = Raffle()
        obj.save()
        handle_uploaded_file(request, request.FILES['file'], obj)
        messages.success(request, "Sorteo creado exitosamente.")
        return redirect(reverse('list'))

    return render(request, 'raffle/create_raffle.html', locals())


def generate_excel(request, pk):
    if request.method == 'POST':

        raffle = Raffle.objects.get(pk=pk)

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=Resultados.xlsx'
        xlsx_data = WriteToExcel(raffle, request)
        response.write(xlsx_data)
        return response

    else:
        return HttpResponse('[]', status=200)

