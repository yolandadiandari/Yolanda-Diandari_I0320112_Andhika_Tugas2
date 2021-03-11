nama_depan = "Yolanda"
nama_belakang = "Diandari"

tanggal_lahir = 28
bulan_lahir = 7
tahun_lahir = 2001
tempat_lahir = "Wonogiri"

tanggal_sekarang = 11
bulan_sekarang = 3
tahun_sekarang = 2021

alamat_lingkungan = "Gubugan"
kecamatan = "Nguntoronadi"
kabupaten = "Wonogiri"
asal_sekolah = "SMA N 1 Wonogiri"
universitas = "Universitas Sebelas Maret"
jurusan = "Teknik Industri"
nim = "I0320112"

berat_badan = 55
tinggi_badan = 155
ukuran_sepatu = 23.5

hobi = "membaca"
novel_favorit = "Laut Bercerita, Supernova : Ksatria, Putri, dan Bintang Jatuh, "
penulis_favorit = "Kahlil Gibran, Nizami, Dee Lestari"
idola_favorit = "Kaisar Julius"
motto_hidup = "I come, i see, i get it"

umur_dalambulan = ((tanggal_sekarang - tanggal_lahir) / 30 ) + ((bulan_sekarang - bulan_lahir)) + ((tahun_sekarang-tahun_lahir) * 12)
umur_dalamtahun = ((tanggal_sekarang - tanggal_lahir) / 365) + ((bulan_sekarang - bulan_lahir)/12) + (tahun_sekarang - tahun_lahir)

print("-----DATA DIRI-----")
print("Nama:" ,nama_depan, nama_belakang)
print("NIM: " ,nim)
print("Jurusan:" ,jurusan)
print("Tempat, Tanggal Lahir:" ,tempat_lahir,",", tanggal_lahir,"-", bulan_lahir,"-", tahun_lahir)
print("Alamat:" ,alamat_lingkungan, kecamatan, kabupaten)
print("Asal SMA:" ,asal_sekolah)
print("Umur dalam Bulan:" , int (umur_dalambulan) ,"bulan")
print("Tinggi Badan:" ,tinggi_badan ,"cm")
print("Berat Badan:" ,berat_badan ,"kg")
print("Ukuran Sepatu:" ,ukuran_sepatu ,"cm")
print("Hobi:",hobi)
print("Novel Favorit:" ,novel_favorit)
print("Penulis Favorit:" ,penulis_favorit)
print("Idola:" ,idola_favorit)
print("Motto:" ,motto_hidup)





