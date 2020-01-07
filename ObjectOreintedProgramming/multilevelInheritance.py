class Dad:
    basketball=1
class Son(Dad):
    dance=1
    def isDance(self):
        return f"Yes i dance {self.dance} no of times"
class GrandSon(Son):
    dance=6
    def isDance(self):
        return f"Yes i Dance very awesomly {self.dance} no of times"

darry=Dad()
larry=Son()
marry=GrandSon()
print(larry.isDance())
print(marry.isDance())
print(marry.basketball)