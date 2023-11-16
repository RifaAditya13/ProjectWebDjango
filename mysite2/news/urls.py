from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('trending/', views.trending, name='trending'),
    path('internasional/', views.internasional, name='internasional'),
    path('ekonomi/', views.ekonomi, name='ekonomi'),
    path('olahraga/', views.olahraga, name='olahraga'),
    path('otomotif/', views.otomotif, name='otomotif'),
    path('hiburan/', views.hiburan, name='hiburan'),
    path('isi<int:id>', views.isi, name='isi'),
]