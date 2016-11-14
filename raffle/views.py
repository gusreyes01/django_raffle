from django.shortcuts import render
# Create your views here.
from raffle.forms import UploadFileForm
from raffle.uploads import handle_uploaded_file


def home(request):
    return render(request,'raffle/home.html', {})

def create(request):
    form = UploadFileForm()

    if request.method == 'POST':
        handle_uploaded_file(request, request.FILES['file'])

    return render(request, 'raffle/create_raffle.html', {'form': form})