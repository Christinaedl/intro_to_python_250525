#integer(int)
#ini bilangan bulat 
#Contoh 0123
x = 32767 #limit dari intteger karakter
print("ini adalah contoh tipe data integer: {0}".format(x))

#float (bilangan desimal)
y = 3.14
print("ini adalah contoh tipe data float: {0}".format(y))

#kompleks
z = 2 + 3j
print("ini adalah contoh tipe data float: {0}".format(z))

# tipe data sequence
a = [ 1,2,3] #list sifat tipe data valuenya sebisa mungkin sama tipe datanya
print("ini adalah contoh tipe data list: {0}".format(a))
b = (4,5,6) #truplet
print("ini adalah contoh tipe data trouplet: {0}".format(b))
c = range(0,5)
print("ini adalah contoh tipe data range: {0}".format(c))

#text
nama = "Christina Eunike Daniela" #tipe data string
#sejarahnya dia terdiri dari char(255)
karakter = 'A'
print("ini adalah contoh tipe data karakter: {0}".format(karakter))

#set
f = {1,2,3} #tipe data yang tidak bisa diubah
print("ini adalah contoh tipe data set: {0}".format(f))
g = frozenset({4,5,6}) #frozen set
print("ini adalah contoh tipe data frozenset: {0}".format(g))

#Tipe data kondisi
#boolean(boot)
#isinya hanya dua yaitu True(1) & False(0)
kondisi_badab = True

#tipe data binary
i = 0b1000001
desimal = int(i)
print(" Conversi binary to Desimal : {0}".format(desimal))
char = chr(desimal)
print("conversi Desimal to Char : {0}".format(char))
print("Singkat binary to char :{0}".format(chr(int(i))))

j = bytearray(a)
print("Isis binary array variabel a : {0}".format(j))
z = memoryview(j)
print("Lokasi array dalam emmori(ram) : {0}".format(z))
