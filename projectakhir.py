import numpy as np
from collections import defaultdict

usr_score = 0
bot_score = 0
usr_history = []
pattern_dict = defaultdict(list)
WIN_SCORE = 8
LEADERBOARD_FILE = "leaderboard.txt"

# Input nama pemain
username = input("Masukkan namamu: ")

# Tampilkan menu level
print("=== GAME TEBAK-TEBAKAN 0 ATAU 1 ===")
print("Pilih level kesulitan:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

# Input level
while True:
    level = input("Masukkan nomor level (1/2/3): ")
    if level in ['1', '2', '3']:
        level = int(level)
        break
    else:
        print("❌ Pilihan tidak valid. Masukkan 1, 2, atau 3.")

print(f"\n🕹️ Halo {username}, capai {WIN_SCORE} poin duluan untuk menang!\n")

# Game loop
while usr_score < WIN_SCORE and bot_score < WIN_SCORE:
    try:
        usr_input = input("Masukkan pilihanmu (0/1): ")
        if usr_input not in ['0', '1']:
            print("❌ Input harus 0 atau 1.")
            continue

        usr_choice = int(usr_input)

        # EASY
        if level == 1:
            prob = 0.5

        # MEDIUM
        elif level == 2:
            prob = sum(usr_history) / len(usr_history) if usr_history else 0.5

        # HARD
        elif level == 3:
            if len(usr_history) >= 2:
                key = (usr_history[-2], usr_history[-1])
                next_choices = pattern_dict[key]
                prob = sum(next_choices) / len(next_choices) if next_choices else 0.5
            else:
                prob = 0.5

        # Tebakan komputer
        comp_choice = np.random.binomial(1, prob, 1)[0]

        # Simpan pola (khusus level 3)
        if level == 3 and len(usr_history) >= 2:
            pattern_dict[(usr_history[-2], usr_history[-1])].append(usr_choice)

        usr_history.append(usr_choice)

        print(f"🧠 Komputer menebak: {comp_choice}")

        if comp_choice == usr_choice:
            bot_score += 1
            print("🤖 Komputer mendapat poin!")
        else:
            usr_score += 1
            print("🎉 Kamu mendapat poin!")

        print(f"Skor - {username}: {usr_score} | Bot: {bot_score}")
        print("-" * 30)

    except KeyboardInterrupt:
        print("\n👋 Game dihentikan.")
        break

# Tentukan pemenang
if usr_score == WIN_SCORE:
    result = "Menang"
    print(f"🏆 Selamat {username}, kamu menang!")
elif bot_score == WIN_SCORE:
    result = "Kalah"
    print(f"😔 Komputer menang. Coba lagi ya, {username}!")

# Simpan ke leaderboard
with open(LEADERBOARD_FILE, "a") as f:
    f.write(f"{username} - {result} | Skor: {usr_score}-{bot_score}\n")

# Tampilkan leaderboard
print("\n📋 Leaderboard (Riwayat Skor):")
try:
    with open(LEADERBOARD_FILE, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line.strip()}")
except FileNotFoundError:
    print("Belum ada skor tersimpan.")
