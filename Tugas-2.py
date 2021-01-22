#!/usr/bin/env python
# coding: utf-8

# In[44]:


print("Selamat Datang !")
print("+====== MENU ======+")
daftar_menu = ['1.Daftar Kontak','2.Tambah Kontak','3.Keluar']
print(*daftar_menu, sep='\n')


# In[45]:


data_kontak = ["Nama : Hafizh Akbar Alam","No Hp = 08181881","Nama : Yuhu","No Hp : 081474747"]
print(*data_kontak, sep='\n')


# In[46]:


print(input("pilih_menu:"))


# In[89]:


data_kontak = ["Nama : Hafizh Akbar Alam","No Hp = 08181881","Nama : Yuhu","No Hp : 081474747"]
print("Selamat Datang !")
print("+====== MENU ======+")
daftar_menu = ['1.Daftar Kontak','2.Tambah Kontak','3.Keluar']
print(*daftar_menu, sep='\n')
daftar_menu = input("Pilih Menu : ")
#print(input("daftar_menu:"))
if (daftar_menu == '1'):
    print(*data_kontak, sep='\n')
elif (daftar_menu == '2'):
    def masukkan_kontak():
        while True:
            nama_kontak = str(input("Nama yang ingin ditambahkan ke List:\n"))
            no_telefon = str(input("No telefon yang ingin ditambahkan ke list:\n"))
            data_kontak.append(nama_kontak)
            data_kontak.append(no_telefon)
            pilihan = str(input("Mau menambahkan lagi? Y/N\n"))
            if pilihan == 'Y' or pilihan == 'y':
                pass
            elif pilihan == 'N' or pilihan == 'n':
                return
            else:
                print("pilihan salah")
        print("Kontak  berhasil ditambahkan")
    masukkan_kontak()
elif(daftar_menu == '3'):
    print("Program Selesai, Sampai Jumpa !")
else:
    print("Menu tidak ada")


# In[ ]:





# In[ ]:




