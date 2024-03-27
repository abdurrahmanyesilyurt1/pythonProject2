class Personel:
    def __init__(self, ad, departman, calisma_yili, maas):
        self.ad = ad
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas

    def __str__(self):
        return f"Ad: {self.ad}, Departman: {self.departman}, Çalışma Yılı: {self.calisma_yili}, Maaş: {self.maas}"


class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print(personel)

    def maas_zammi(self, personel, zam_orani):
        personel.maas += personel.maas * zam_orani / 100

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)


personel1 = Personel("Abd", "bilgisayar", 5, 3000)
personel2 = Personel("mlk", "yazilim", 2, 2000)

firma = Firma()
firma.personel_ekle(personel1)
firma.personel_ekle(personel2)
firma.personel_listele()
firma.maas_zammi(personel1, 10)  # %10 zam yapılıyor.
firma.personel_listele()
firma.personel_cikart(personel1)
firma.personel_listele()
