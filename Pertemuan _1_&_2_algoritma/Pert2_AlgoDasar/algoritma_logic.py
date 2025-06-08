#study kasus
nilai_raport = 100

#if
# format dasar
# if kondisi :
#       apa yang akan kamu lakuakn jika kondidi terpenuhi
# kalau tidak terpenuhi program akan tetap dijalankan 
print("==========if============")
nilai_raport = 100
if nilai_raport >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
print("program akan terus berlanjut")

print("==========if-else============")
nilai_raport = 50
if nilai_raport >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
else :
    print("Kamu tidak lulus")

print("========Tenery=========")
nilai_raport = 50
pesan = "Lulus" if nilai_raport > 100 else "Tidak Lulus"
print(f"{pesan}")

print("=========== if elif else=========")
nilai_raport = 60

if nilai_raport >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
elif nilai_raport >= 50 and nilai_raport < 100:
    print("Kamu lulus dengan nilai paspasan")
else:
    print("kamu tidak lulus")


print("========if nested(bersarang)=========")
nilai_raport = 90
if nilai_raport >= 100:
    print("Selamat kamu lulus dalam test ini !!!")
elif nilai_raport >= 50 and nilai_raport < 100:
    # tipsnya cari syarat yang paling sedikit 
    if nilai_raport > 70: # iini disebut if nested bersarang 
        print("kamu lulus")
    else:
        print("Kamu lulus dengan nilai paspasan")
else:
    print("kamu tidak lulus")


#switch case
#di pakai saat kamu tau spesifik apa yang akandilakukan user

print("==================Switch Case============")
print("=========Menu===========")
print("1.Start")
print("2.End")
select = input("select =>")
match select:
    case"1":
        print("Start")
    case "2":
        print("End")
    case _ :
        print("Invalid input type")

