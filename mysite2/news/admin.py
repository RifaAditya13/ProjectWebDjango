from django.contrib import admin
from . models import berita, kategori, customuser
# Register your models here.

admin.site.register(customuser)

class categoriesAdmin(admin.ModelAdmin):
    list_display = ['namakategori']
    search_fields = ['namakategori']

admin.site.register(kategori, categoriesAdmin)

class beritaAdmin (admin.ModelAdmin):
    # List Display
    list_display = ['judul', 'deskripsi', 'isi', 'kategori', 'kategoriID', 'gambar', 'penulis', 'fotopenulis', 'publikasi', 'status']
    search_fields = ['judul', 'kategori_name']
    autocomplete_fields = ['kategori']

admin.site.register(berita, beritaAdmin)