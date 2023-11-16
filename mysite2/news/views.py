from django.shortcuts import render, get_object_or_404
from . import models

catID = 0

# Create your views here.
def all(request):
    if 'cari' in request.GET:
        cari = request.GET['cari']
        berita = models.berita.objects.filter(judul__icontains=cari)
    else :
        berita = models.berita.objects.all()

    context = {'beritas' : berita}
    return render(request, 'menu/all.html', context)

def isi(request, id):
    berita = get_object_or_404(models.berita, pk=id)
    context = {'beritas' : berita}
    return render(request, 'menu/isiberita.html', context)

def trending(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 1
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status ='publish')
    
    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/trending.html', context)


def internasional(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 2
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status ='publish')
    
    context = {'beritas' : berita, 'kategiori' : kategori}

    return render(request, 'menu/internasional.html', context)


def ekonomi (request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 3
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status ='publish')
    
    context = {'beritas' : berita, 'kategiori' : kategori}

    return render(request, 'menu/ekonomi.html', context)


def olahraga(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 4
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status ='publish')
    
    context = {'beritas' : berita, 'kategiori' : kategori}

    return render(request, 'menu/olahraga.html', context)    


def otomotif(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 5
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status ='publish')
    
    context = {'beritas' : berita, 'kategiori' : kategori}

    return render(request, 'menu/otomotif.html')


def hiburan(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 6
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status ='publish')
    
    context = {'beritas' : berita, 'kategiori' : kategori}

    return render(request, 'menu/hiburan.html')