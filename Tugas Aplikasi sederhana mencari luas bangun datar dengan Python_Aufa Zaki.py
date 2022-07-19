def header():
    nama = input("Nama Kamu : ")
    nim = input("Nim Kamu : ")

    print("................................................")
    print("..... Selamat Datang ",nama," .....")
    print("..... Ini NIM Kamu ",nim,".....")
    print("................................................")

def luas_persegi() :
    print (' ' )
    print ('1.Question mencari luas persegi')
    x= float(input ("panjang sisi : "))
    luasp= x*x
    print (' ')
    print ('luas perseginya adalah : ' , luasp , 'cm2')

def luas_pp () :
    print (' ' )
    print ('2.Question mencari luas persegi panjang')
    print (' ')
    x= float(input('masukkan panjangnya : '))
    print (' ' )
    y= float(input ('masukkan lebarnya : '))
    c = x*y
    print (' ' )
    print ('luas persegi panjangnya adalah : ' , c , 'cm2')

def luas_segitiga () :
    print (' ' )
    print ('3.Question mencari luas segitiga' )
    print (' ')
    x= float(input('masukkan alas segitiga : '))
    y= float(input('masukkan tinggi segitiga :'))
    a=0.5*x*y
    print (' ' )
    print ('luas segitiganya adalah : ' , a, 'cm2')
    
def luas_lingkaran () :
    print (' ' )
    print (' 4.Question mencari luas lingkaran ')
    print (' ')
    x= float(input('masukkan jari-jari lingkaran : '))
    luas = 22/7*x*x
    print ('')
    print ('luas lingkarannya adalah : ' , luas , 'cm2')
              
def luas_jg () :
    print (' ' )
    print (' 5.Question mencari luas jajaran genjang ')
    print (' ')
    x= float(input('masukkan tinggi jajaran genjang : '))
    y= float (input('masukkan alas jajaran genjang :' ))
    luas = x*y
    print ('')
    print ('luas jajaran genjang adalah : ' , luas , 'cm2')

def luas_trapesium () :
    print (' ' )
    print (' 6.Question mencari luas trapesium ')
    print (' ')
    x= float(input('masukkan sisi atas trapesium : '))
    y= float(input('masukkan sisi bawah trapesium : '))
    z= float(input('masukkan tinggi trapesium : '))
    luas = (x+y)*z/2
    print ('')
    print ('luas trapesiumnya adalah : ' , luas, 'cm2')
             
def luas_bk () :
    print (' ' )
    print (' 7.Question mencari luas belah ketupat ')
    print (' ')
    x= float(input('masukkan diagonal 1 : '))
    y= float(input('masukkan diagonal 2 : ' ))
    luas = 0.5*x*y
    print ('')
    print ('luas belah ketupatnya adalah : ', luas, 'cm2')


header()
luas_persegi()
luas_pp()
luas_segitiga()
luas_lingkaran()
luas_jg()
luas_trapesium()
luas_bk()


print("Terimakasih Sampai Jumpa Kembali:V ")
print(" by Faza26 ")