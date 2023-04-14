from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name' : 'Chassie Bessy'
    }
    return render(request, 'index.html', context)

def tambah_barang(request):
    return render(request, 'tambah_barang.html')

def post_barang(request):
    return HttpResponse()

def tambah_user(request):
    return render(request, 'tambah_user.html')

def post_user(request):
    id_kurir = request.POST('id_kurir')
    nama_kurir = request.POST('nama_kurir')
    no_hp__kurir = request.POST('no_hp__kurir')
    return HttpResponse()