from django.db import models

# Create your models here.
class Pendapatan(models.Model):
    jumlah_pendapatan = models.BigIntegerField()
    tanggal_input = models.DateTimeField('tanggal input')


class Pengeluaran(models.Model):
    jumlah_pengeluaran = models.BigIntegerField()
    tanggal_input = models.DateTimeField('tanggal input')