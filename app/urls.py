from django.urls import path
from .views import index,tambah_barang,post_barang,tambah_user,post_user

urlpatterns = {
    path('index', index, name='index'),
    path('tambah_barang', tambah_barang, name='tambahbarang'),
    path('post_barang', post_barang, name='postbarang'),
    path('tambah_user', tambah_user, name='tambahuser'),
    path('post_user', post_user, name='postuser')
}