# GEP1316 Kodlama Okuryazarligi - Odev 3
# Berk Demir Guner - 2482965
# Ucak bagaji fazla agirlik ucreti hesaplayicisi

# Odev icin belirlenen ornek tarife degerleri (gercek havayolu tarifesi degildir).
UCRETSIZ_BAGAJ_HAKKI_KG = 20.0
FAZLA_BAGAJ_KG_UCRETI_TL = 150.0
UYE_INDIRIM_ORANI = 0.10

print("=== Ucak Bagaji Ucret Hesaplayici ===")
print(f"Ucretsiz bagaj hakki: {UCRETSIZ_BAGAJ_HAKKI_KG:.1f} kg")
print(f"Fazla bagaj ucreti: {FAZLA_BAGAJ_KG_UCRETI_TL:.2f} TL/kg")

# Yolcu ve ucus bilgileri metin (str) olarak alinir.
yolcu_adi = input("Yolcunun adi: ").strip()
ucus_kodu = input("Ucus kodu: ").strip().upper()

try:
    # Bagaj adedi tam sayiya (int), toplam agirlik ondalikli sayiya (float) donusturulur.
    bagaj_adedi = int(input("Bagaj adedi: "))
    toplam_agirlik_kg = float(input("Bagajlarin toplam agirligi (kg): ").replace(",", "."))

    # Uyelik cevabi karsilastirilir ve bool (True/False) degerine donusturulur.
    uyelik_cevabi = input("Indirimli uyelik var mi? (evet/hayir): ").strip().lower()
    if uyelik_cevabi not in ("evet", "hayir"):
        print("Hata: Uyelik icin sadece 'evet' veya 'hayir' yazin.")
    elif not yolcu_adi or not ucus_kodu:
        print("Hata: Yolcu adi ve ucus kodu bos birakilamaz.")
    elif bagaj_adedi < 0 or toplam_agirlik_kg < 0:
        # Negatif bagaj adedi veya agirlik kabul edilmez.
        print("Hata: Bagaj adedi ve agirlik negatif olamaz.")
    elif bagaj_adedi == 0 and toplam_agirlik_kg > 0:
        print("Hata: Bagaj adedi sifirken toplam agirlik sifirdan buyuk olamaz.")
    else:
        uyelik_var = uyelik_cevabi == "evet"

        # Fazla agirlik sifirdan kucuk olamayacagi icin max() kullanilir.
        fazla_kilo = max(0.0, toplam_agirlik_kg - UCRETSIZ_BAGAJ_HAKKI_KG)
        brut_ucret = fazla_kilo * FAZLA_BAGAJ_KG_UCRETI_TL

        # Uyelik varsa brut ucret uzerinden %10 indirim uygulanir.
        indirim = brut_ucret * UYE_INDIRIM_ORANI if uyelik_var else 0.0
        odenecek_tutar = brut_ucret - indirim

        print("\n--- Hesaplama Sonucu ---")
        print(f"Yolcu: {yolcu_adi}")
        print(f"Ucus: {ucus_kodu}")
        print(f"Bagaj adedi: {bagaj_adedi}")
        print(f"Toplam agirlik: {toplam_agirlik_kg:.2f} kg")
        print(f"Fazla agirlik: {fazla_kilo:.2f} kg")
        print(f"Indirim: {indirim:.2f} TL")
        print(f"Odenecek tutar: {odenecek_tutar:.2f} TL")

        # Karsilastirma operatoru ile bagajin hak dahilinde olup olmadigi belirtilir.
        if toplam_agirlik_kg <= UCRETSIZ_BAGAJ_HAKKI_KG:
            print("Durum: Bagaj, ucretsiz agirlik hakki icindedir.")
        else:
            print("Durum: Fazla bagaj ucreti uygulanir.")

except ValueError:
    # Sayisal alanlara harf gibi gecersiz deger girilirse program duzgun mesaj verir.
    print("Hata: Bagaj adedine tam sayi, agirlik alanina sayi girin.")
