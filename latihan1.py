# => Variabel
# Variabel adalah tempat menyimpan data
# Penulisan variabel dalam Python juga memiliki aturan tertentu, yaitu:
# 1). Karakter pertama harus berupa huruf atau garis bawah/underscore ( _ ).
# 2). Karakter selanjutnya dapat berupa huruf, garis bawah/underscore ( _ ) atau angka.
# 3). Karakter pada nama variabel bersifat sensitif (case-sensitif). Artinya huruf kecil dan huruf besar dibedakan. Sebagai contoh, variabel œnama dan œNama adalah variabel yang berbeda.


# Menaruh / assignment nilai =

a = 10
x = 5
panjang = 100

# Pemanggilan pertama :

print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

# Penamaan Variabel =

nilai_y = 20 # Dengan menggunakan underscore
juta10 = 30 # Menaruh angka harus setelah huruf
nilaiz = 40 # Besar kecilnya tulisan berbeda maka nama variabel tersebut juga berbeda
nilaiZ = 50

# Pemanggilan Kedua :
print("Nilai a pertama = ", a)
a = 17
print("Nilai a kedua = ", a)

# Assignment indirect
b = a
print("Nilai b adalah = ", b)

# => Tipe Data
# 1). Integer = tipe data yang berisi angka bulat (bukan koma
# bukan pecahan)

data_integer = 50
print("data : ", data_integer)
print("bertipe : ", type(data_integer))

# 2). Float = tipe data yang berisi angka desimal/pecahan

data_float = 50.5
print("data : ", data_float)
print("bertipe : ", type(data_float))

# 3). String = tipe data yang berisi kumpulan karakter

data_string = "brian"
print("data : ", data_string)
print("bertipe : ", type(data_string))

# 4). Boolean = tipe data yang berisi pilihan berupa kondisi true/false

data_bool = true
print("data : ", data_bool)
print("bertipe : ", type(data_bool))