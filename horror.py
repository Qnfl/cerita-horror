print("Kamu baru bangun di tempat aneh")
print("Gelap. Dingin. Aku nggak inget gimana bisa nyampe sini.")
print("Di depanku ada dua jalan yang samar.")

print("\n1. Jalan ke kiri, ke arah suara tangisan pelan.")
print("2. Jalan ke kanan, ke arah bau aneh.")
choice = int(input("Mau ke mana? (1/2): "))

if choice == 1:
  print("\nAku jalan pelan ke kiri. Makin deket, tangisannya makin jelas.")
  print("Di balik pohon gede, ada bayangan membungkuk.")

  print("\n1. Coba sapa, siapa tau butuh bantuan.")
  print("2. Balik badan, lari kenceng!")
  choice = int(input("Pilih (1/2): "))

  if choice == 1:
    print("\n'Halo?' Bayangan itu ngangkat kepala. Matanya merah nyala.")
    print("'Aku hanya butuh... kehangatan,' katanya, suaranya dingin. Tangan ngulur ke arahku.")
    print("Badan kaku, dingin. Gelap. Aku nggak sendiri lagi.")
    print("\nTAMAT: TERJEBAK BARENG DIA")
  elif choice == 2:
    print("\nAku langsung muter balik, lari sekenceng-kencengnya. Tangisan di belakang makin kenceng.")
    print("Aku lari terus sampai jatuh di semak. Suara tangisan makin jauh.")
    print("Ngumpet sampai pagi. Pas matahari terbit, aku nemu jalan raya, berhasil keluar.")
    print("\nTAMAT: BERHASIL KABUR (KENA TRAUMA)")
  else:
    print("Pilihan tidak ada")

elif choice == 2:
  print("\nAku jalan ke kanan, sambil nutup hidung. Bau busuknya makin kuat.")
  print("Nggak jauh, ada altar batu, di atasnya ada benda aneh.")

  print("\n1. Coba deketin, pengen tau itu benda apa.")
  print("2. Mendingan nggak usah, cari jalan lain aja.")
  choice = int(input("Pilih (1/2): "))

  if choice == 1:
    print("\nAku mendekat. Benda itu boneka tua, matanya melotot.")
    print("Pas disentuh, boneka itu geter. Api nyala di matanya, terus barang sekitar nyala.")
    print("Suara tawa kenceng dari mana-mana. Badanku diiket, nggak bisa gerak.")
    print("Mata boneka terus ngeliat aku. Ini bukan boneka biasa.")
    print("\nTAMAT: JADI TUMBAL")
  elif choice == 2:
    print("\nAku mutusin nggak usah deketin altar. Bau busuknya bikin mual. Aku balik kanan, cari jalan lain.")
    print("Jalan terus, sampai nemu cahaya lampu kota di kejauhan.")
    print("Aku lari sekenceng-kencengnya. Akhirnya, aku keluar dari tempat aneh itu.")
    print("\nTAMAT: SELAMAT!")
  else:
    print("Pilihan tidak ada")

else:
  print("Pilihan tidak ada")

print("\nMakasih udah main!")