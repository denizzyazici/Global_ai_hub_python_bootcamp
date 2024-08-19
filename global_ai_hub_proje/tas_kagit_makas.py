import random

ad = input("Adınızı giriniz:")
print(f"Merhaba {ad.upper()}! Taş, kağıt, makas oyununa HOŞGELDİN! \n"
      "Oyunun kurallarını seninle gözden geçirelim. \n"
      "Taş, makası yener. \n"
      "Makas, kağıdı yener.\n"
      "Kağıt, taşı yener.\n"
      "Hangisini seçeceğini dikkatli düşün:).\n"
      "İlk iki turu alan oyunun GALİBİ olur.\n"
      "Bol şans!")
print("##############")

o = 1


def tas_kagit_makas_deniz_yazici(o):
    t = 1
    i = 1
    secenekler = ["taş", "kağıt", "makas"]
    baslangic = input("Oyuna başlamak için 'BAŞLA' yaz, Oyundan çıkmak için 'ÇIKIŞ' yaz:").upper()
    oyuncu_sayaci = 0
    pc_sayaci = 0

    if baslangic == "BAŞLA":

        while 0 <= oyuncu_sayaci <= 2 or 0 <= pc_sayaci <= 2:
            print(f"OYUN {o}, TUR {t}")
            secim = input("Taş, kağıt, makas veya ÇIKIŞ?").lower()

            if secim == "çıkış":
                print("Seninle tanışmak güzeldi. Bir dahaki sefere görüşmek üzere:)")
                break

            if secim not in secenekler:
                print(f"Geçersiz seçim: '{secim}'. Lütfen 'taş', 'kağıt' veya 'makas' kelimelerinden birini girin.")
                continue

            pc = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {pc}")

            if secim == pc:
                print("Berabere kaldınız!")
            elif secim == "taş" and pc == "makas":
                print("Bravo! Bu turun galibi sizsiniz.")
                oyuncu_sayaci += 1
            elif secim == "taş" and pc == "kağıt":
                print("Kağıt taşı sarar. Kazanan Robot oluyor!")
                pc_sayaci += 1
            elif secim == "kağıt" and pc == "taş":
                print("Bravo! Turun galibi siziniz.")
                oyuncu_sayaci += 1
            elif secim == "kağıt" and pc == "makas":
                print("Üzgünüz makas kağıdı keser.Galip Robot.")
                pc_sayaci += 1
            elif secim == "makas" and pc == "kağıt":
                print("Bravo! Tur sizin.")
                oyuncu_sayaci += 1
            elif secim == "makas" and pc == "taş":
                print("Taş makası ezdi ve turun galibi Robot oldu.")
                pc_sayaci += 1
            t += 1
            i += 1
            print("Oyuncu:", oyuncu_sayaci, "Robot:", pc_sayaci)
            print("###################")

            if oyuncu_sayaci == 2:

                print("TEBRİKLER, Oyunun galibi sensin:)")
                yeni_oyun = input("Oyuncu:Yeni bir Oyun daha oynamak istersen 'evet' istemiyorsan 'hayır' yaz.").lower()
                pc_secim = ["evet", "hayır"]
                pcs = random.choice(pc_secim)
                print("Robot: Yeni bir Oyun daha oynamak istersen 'evet' istemiyorsan 'hayır' yazabilirsin:", pcs)
                if yeni_oyun == "evet" and pcs == "evet":
                    o += 1
                    tas_kagit_makas_deniz_yazici(o)
                elif yeni_oyun != "evet" and yeni_oyun != "hayır":
                    print("geçersiz yanıt! Lütfen 'evet' ya da 'hayır' yanıtlarını giriniz:")

                elif yeni_oyun == "hayır" or pcs == "hayır":
                    print("Oyun için teşekkürler. Bir dahaki sefere görüşmek üzere.")
                    break

            elif pc_sayaci == 2:

                pc_secim = ["evet", "hayır"]
                pcs = random.choice(pc_secim)
                print("Oyunun galibi ROBOT oluyor::)")
                print("Yeni bir Oyun daha oynamak istersen 'evet' istemiyorsan 'hayır' yazabilirsin:", pcs)

                if pcs == "evet":
                    o += 1
                    tas_kagit_makas_deniz_yazici(o)
                elif pcs != "evet" and pcs != "hayır":
                    print("geçersiz yanıt! Lütfen 'evet' ya da 'hayır' yanıtlarını girniz.")
                elif pcs == "hayır":
                    print("Oyun için teşekkürler. Bir dahaki sefere görüşmek üzere.")
                break

    elif baslangic == "ÇIKIŞ":
        print("Seninle tanışmak güzeldi. Bir dahaki sefere görüşmek üzere:)")

    else:
        print("Geçersiz giriş. Lütfen 'BAŞLA' veya 'ÇIKIŞ' yazın.")
        tas_kagit_makas_deniz_yazici(o)


tas_kagit_makas_deniz_yazici(o)