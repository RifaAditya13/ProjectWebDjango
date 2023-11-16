from django.shortcuts import render
from news import models as mdl

# Create your views here.
def isi (request, pk):
    berita = mdl.berita.object.get(pk=pk)
    context = {'beritas' : berita}
    return render (request, 'berita/isiberita.html', context)