def main():
#while
#saat kita tau syarat tapi masih ragu dengan jalan menuju syaratnya
#sifat utamanya
#cek terlenbih dahulu  baru dijalankan
    index = 0
    print("=============ini tentang while=======")
    while index <= 1000:
        print(f"{index}. Sorry Beb !!!!")
        index += 1
    #do while
    #sifat dikerjakan dulu baru di cek
    #tidk ada di python tapi ada di java, javascript, atau keluraga C, C++, dan C#
    print("=============for=======")
    #for
    #for dipakai saat kamu tau syarat dan cara menujunya
    for value in range (1,10):
        print(f"index of {value}")

    makanan=  ['daging', 'ayam', 'sayur', 'Semangka', 'Melon', 'Nanas']
    for value in makanan:
        print(f"{value}")


if __name__ == "__main__" : #format dasar untuk memberitahukan kalau program yang dijalankan pertama kali 
    main()