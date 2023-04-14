from django.db import models

# Create your models here.
class Kurir(models.Model):
    id_kurir = models.CharField(max_length=4, primary_key=True)
    nama_kurir = models.CharField(max_length=100)
    nomor_hp_kurir = models.CharField(max_length=13)
    area_pengiriman = models.CharField(max_length=200)

class Barang(models.Model):
    id_barang = models.CharField(max_length=4, primary_key=True)
    pemesan = models.CharField(max_length=50)
    alamat_barang = models.CharField(max_length=100)
    nomor_hp_pemesan = models.CharField(max_length=13)
    penerima = models.CharField(max_length=50)
    bukti = models.ImageField