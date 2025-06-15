import random #ini disebut lib(python), package (java), header (C))

def random_generate(jumlah_data):
    list_data = []
    for index in range(jumlah_data):
        value = random.randint(1,100)
        list_data.append(value)
    return list_data

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0,n-i-1):
            if data[j] >data[j+1] :# ini pengurutan ASC (kecil ke besar atau A ~ Z)
                #temp = data[j]
                #data[j] = data[j+1]
                #data[j+1] = temp
                data[j], data[j+1] = data[j+1], data[j]

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if data[j] < data[min_index]:
                min_index = j
        data[i],data[min_index] = data[min_index],data[i]

def insertion_sort(data):
    for i in range (1,len(data)) :
        kunci = data[i]
        j = i - 1
        while j >= 0 and kunci < data[j]:
            data[j+1] = data [j]
            j -=1
        data[j+1] = kunci

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        kiri = data[:mid]
        kanan = data [mid:]
        merge_sort(kiri)#rekursif ini berbahaya karena menimbulkan infinite looping 
        merge_sort(kanan)
        # i = 0 
        # j = 0
        # k = 0
        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else :
                data[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1
        while j < len(kanan):
            data[k] = kanan [j]
            j +=1
            k +=1
def main():
    #error handleling
    #teknik program agar terus berjalan
    #keep it simple, stupid 
    #try:
        banyak_data = int(input("Banyak data yang akan di generate : "))
        #validatin
        #teknik untuk melakuakn pengecekan lebih lanjut
        #if banyak_data <= 0:
        #     print("banyak data harus lebih dari 0")
        #     main()
        # else:
        list_data = random_generate(banyak_data)
        print("==List Data Random: ")
        print(list_data)
        input("please press Enter to next step..............")
        #bubble_sort(list_data)
        #selection_sort(list_data)
        #insertion_sort(list_data)
        merge_sort(list_data)
        print("=======Setelah di sorting=====")
        print(list_data)
    # except:
    #     print("Masukan data dengan tipe numerik !!!")
    #     main()


if __name__ == "__main__":
    main()