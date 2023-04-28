from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Admin
from .models import Kurir
from .models import Barang
from .models import TaskDelivery
from django.contrib import messages
from functools import wraps
# from .decorators import login_required

# Create your views here.
def login_required():
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.session.get('logged_in'):
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'LOGIN TERLEBIH DAHULU')
                return redirect('LoginPage')
        return wrapper
    return decorator

# load login_required
def LoginPage(request):
    return render(request, 'login.html')

def login_post(request):
    # Cek apakah user yang login sudah benar
    userid = request.POST.get('userid', '').upper()
    username = request.POST.get('username', '').upper()
    password = request.POST.get('password', '').upper()
    if userid == 'RPL14' and username == 'SISTEM KURIR' and password == '1111':
        # Simpan data session
        request.session['logged_in'] = True
        request.session['userid'] = userid
        messages.success(request, 'BERHASIL LOGIN')
        return redirect('index')
    else:
        messages.error(request, 'USER TIDAK DITEMUKAN')
        return redirect('LoginPage')

@login_required()
#index
def index(request):
    # data_barang = Barang.objects.all()  # use .all() to get all objects
    # data_kurir = Kurir.objects.all()
    # data_task = TaskDelivery.objects.all()

    # context = {
        # 'data_barang': data_barang ,
        # 'data_kurir' : data_kurir, # use : instead of = in dictionary
        # 'data_task' : data_task
    # }
    # return render(request, 'index.html')
    return redirect(request.META.get('HTTP_REFERER', '/'))


#logout
def logout(request):
    # Hapus data session
    request.session.flush()
    messages.success(request, 'BERHASIL LOGOUT')
    return redirect('LoginPage')


#CRUD Kurir
def tambah_kurir(request):
    return render(request, 'kurirs/tambah_kurir.html')

def post_kurir(request):
    id_kurir = request.POST['id_kurir']
    nama = request.POST['nama']
    no_telepon = request.POST['no_telepon']
    area_pengiriman = request.POST['area_pengiriman']
    if Kurir.objects.filter(id_kurir=id_kurir).exists():
        messages.error(request, 'USER ID SUDAH DIGUNAKAN')
        return render(request, 'kurirs/tambah_kurir.html')
    else:
        tambah_kurir = Kurir(
            id_kurir=id_kurir,
            nama=nama,
            no_telepon=no_telepon,
            area_pengiriman=area_pengiriman
        )
        tambah_kurir.save()
        messages.success(request, 'KURIR BERHASIL DITAMBAHKAN.')
    return redirect('/index_kurir')

def index_kurir(request):
    data_kurir = Kurir.objects.all()
    context = {
        'data_kurir' : data_kurir
    }
    return render(request, 'kurirs/index_kurir.html', context)

def update_kurir(request, id_kurir):
    data_kurir = Kurir.objects.get(id_kurir=id_kurir)
    context = {
        'data_kurir': data_kurir
    }
    return render (request, 'kurirs/update_kurir.html', context)

def post_update_kurir(request):
    #ambil data post
    id_kurir = request.POST['id_kurir']
    nama = request.POST['nama']
    no_telepon = request.POST['no_telepon']
    area_pengiriman = request.POST['area_pengiriman']
    #proses update
    kurir = Kurir.objects.get(id_kurir=id_kurir)
    try:
        no_telepon = int(no_telepon)
        kurir.nama = nama
        kurir.no_telepon = no_telepon
        kurir.area_pengiriman = area_pengiriman
        kurir.save()
        messages.success(request, 'BERHASIL UPDATE DATA KURIR')
    except ValueError:
        messages.error(request, 'PERIKSA KEMBALI NO TELEPON ANDA!')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_kurir(request, id_kurir):
    Kurir.objects.get(id_kurir=id_kurir).delete()
    messages.success(request, 'BERHASIL HAPUS KURIR')
    return redirect(request.META.get('HTTP_REFERER', '/'))









#CRUD Barang
def tambah_barang(request):
    return render(request, 'barangs/tambah_barang.html')

def post_barang(request):
    id_barang = request.POST['id_barang']
    nama_pemesan = request.POST['nama_pemesan']
    status_barang = request.POST['status_barang']
    no_hp = request.POST['no_hp']
    tujuan = request.POST['tujuan']
    nama_penerima = request.POST['nama_penerima']

    if Barang.objects.filter(id_barang=id_barang).exists():
        messages.error(request, 'ID BARANG SUDAH DIGUNAKAN')
        return render(request, 'barang/tambah_barang.html')
    else:
        tambah_barang = Barang(
            id_barang=id_barang,
            nama_pemesan=nama_pemesan,
            status_barang=status_barang,
            no_hp=no_hp,
            tujuan=tujuan,
            nama_penerima=nama_penerima,
        )
        tambah_barang.save()
        messages.success(request, 'BERHASIL TAMBAH BARANG')
    return redirect('barangs/index_barang')

def index_barang(request):
    data_barang = Barang.objects.all()
    context = {
        'data_barang' : data_barang
    }
    return render(request, 'barangs/index_barang.html', context)

def update_barang(request, id_barang):
    data_barang = Barang.objects.get(id_barang=id_barang)
    context = {
        'data_barang': data_barang
    }
    return render (request, 'barang/update_barang.html', context)

def post_update_barang(request):
    #ambil data post
    id_barang = request.POST['id_barang']
    nama_pemesan = request.POST['nama_pemesan']
    tujuan = request.POST['tujuan']
    no_hp = request.POST['no_hp']
    nama_penerima = request.POST['nama_penerima']
    status_barang = request.POST['status_barang']
    #proses update
    barang = Barang.objects.get(id_barang=id_barang)
    try:
        no_hp = int(no_hp)
        barang.nama_pemesan = nama_pemesan
        barang.tujuan = tujuan
        barang.no_hp = no_hp
        barang.nama_penerima = nama_penerima
        barang.status_barang = status_barang
        barang.save()
        messages.success(request, 'BERHASIL UPDATE DATA BARANG')
        return render(request, '/index_barang')
    except ValueError:
        messages.error(request, 'PERIKSA KEMBALI NO TELEPON ANDA!')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_barang(request, id_barang):
    barang = Barang.objects.get(id_barang=id_barang)
    barang.delete()
    messages.success(request, 'BERHASIL HAPUS BARANG')
    return redirect(request.META.get('HTTP_REFERER', '/'))








#CRUD Task
def tambah_task(request):
    daftar_kurir = Kurir.objects.all()
    context = {
        'daftar_kurir':daftar_kurir,
    }
    return render(request, 'taskDeliverys/tambah_task.html',context)

def post_task(request):
    id_task = request.POST['id_task']
    waktu_pos = request.POST['waktu_pos']
    waktu_pod = request.POST['waktu_pod']
    if waktu_pos == '' :
        bukti_pos = ''
        bukti_pod = request.FILES['bukti_pod']
        waktu_pos = None
    if waktu_pod == '':
        bukti_pos = request.FILES['bukti_pos']
        bukti_pod = ''
        waktu_pod = None
    jml_paket_pos = request.POST['jml_paket_pos']
    jml_paket_pod = request.POST['jml_paket_pod']

    area_pengiriman = request.POST.get('area_pengiriman')
    kurir = Kurir.objects.filter(area_pengiriman=area_pengiriman).first()

    if TaskDelivery.objects.filter(id_task=id_task).exists():
        messages.error(request, 'TASK ID SUDAH DIGUNAKAN')
        return render(request, 'taskDeliverys/tambah_task.html')
        # kurir = Kurir.objects.filter(id=id_kurir).first()
        # if kurir is None:
        #     messages.error(request, 'TIDAK DITEMUKAN KURIR DENGAN ID INI')
        #     return render(request, 'tambah_task.html')

        # barang = Barang.objects.filter(id=id_barang).first()
        # if barang is None:
        #     messages.error(request, 'TIDAK DITEMUKAN BARANG DENGAN ID INI')
        #     return render(request, 'tambah_task.html')
    else :
        tambah_task = TaskDelivery(
            id_task=id_task,
            waktu_pos=waktu_pos,
            waktu_pod=waktu_pod,
            bukti_pos=bukti_pos,
            bukti_pod=bukti_pod,
            jml_paket_pos=jml_paket_pos,
            jml_paket_pod=jml_paket_pod,
            id_kurir=kurir,
            # barang=barang,
        )
        tambah_task.save()
        messages.success(request, 'BERHASIL TAMBAH TASK')
    return redirect('index')

def index_task(request):
    data_task = TaskDelivery.objects.all()
    context = {
        'data_task' : data_task
    }
    return render(request, 'taskDeliverys/index_task.html', context)

def update_task(request, id_task):
    data_task = TaskDelivery.objects.get(id_task=id_task)
    context = {
        'data_task': data_task
    }
    return render (request, 'taskDeliverys/update_task.html', context)

def post_update_task(request):
    #ambil data post
    id_task = request.POST['id_task']
    waktu_pos = request.POST['waktu_pos']
    waktu_pod = request.POST['waktu_pod']
    if waktu_pos == '' :
        bukti_pos = ''
        bukti_pod = request.FILES['bukti_pod']
        waktu_pos = None
    if waktu_pod == '':
        bukti_pos = request.FILES['bukti_pos']
        bukti_pod = ''
        waktu_pod = None
    jml_paket_pos = request.POST['jml_paket_pos']
    jml_paket_pod = request.POST['jml_paket_pod']
    # id_kurir = request.POST['kurir']
    #proses update
    task = TaskDelivery.objects.get(id_task=id_task)
    try:
        id_task = id_task
        task.waktu_pos = waktu_pos
        task.bukti_pos = bukti_pos
        task.waktu_pod = waktu_pod
        task.bukti_pod = bukti_pod
        task.jml_paket_pos = jml_paket_pos
        task.jml_paket_pod = jml_paket_pod
        # task.id_kurir = id_kurir
        task.save()
        messages.success(request, 'BERHASIL UPDATE DATA TASK')
    except ValueError:
        messages.error(request, 'PERIKSA KEMBALI ID TASK!')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_task(request, id_task):
    TaskDelivery.objects.get(id_task=id_task).delete()
    messages.success(request, 'BERHASIL HAPUS TASK')
    return redirect(request.META.get('HTTP_REFERER', '/'))



#home & contach
def home(request):
    return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')