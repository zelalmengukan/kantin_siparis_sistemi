class Urun:
    def __init__(self, urun_adi, fiyat):
        self.urun_adi = urun_adi
        self.fiyat = fiyat

    def bilgi(self):
        return f"{self.urun_adi} - {self.fiyat} TL"


# Kantin ürünleri ve fiyatları (Sözlük)
kantin_urunleri = {
    "tost": 50,
    "çay": 10,
    "meyve suyu": 25,
    "su": 5
}

# Urun nesnelerinin oluşturulması
urun_objeleri = {}
for urun_adi, fiyat in kantin_urunleri.items():
    urun_objeleri[urun_adi] = Urun(urun_adi, fiyat)

# Menü Döngüsü
while True:
    print("\n--- Kantin Sipariş Sistemi ---")
    print("1 - Ürünleri Gör")
    print("2 - Sipariş Ver")
    print("3 - Çıkış")
    
    secim = input("Seçiminiz (1-3): ").strip()

    if secim == "1":
        print("\n--- Kantin Menüsü ---")
        for urun in urun_objeleri.values():
            print(urun.bilgi())

    elif secim == "2":
        istek = input("Sipariş etmek istediğiniz ürünün adını girin: ").strip().lower()
        if istek in urun_objeleri:
            print("Sipariş alındı")
            print(urun_objeleri[istek].bilgi())
        else:
            print("Ürün bulunamadı")

    elif secim == "3":
        print("Program kapandı")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
