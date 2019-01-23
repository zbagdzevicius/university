import csv
import matplotlib.pyplot as plt
import sys
import random

class Ro_ro_vilkikas():
    def __init__(self, nasumas, keliamoji_jega, kroviniai_laive, kroviniai_terminale):
        self.nasumas = nasumas
        self.veikia = True
        self.gedimu_prastovos = 0
        self.krovimo_laikas = 0
        self.uzimtas_tikrinimu_laikas = 0
        self.keliamoji_jega = keliamoji_jega
        self.gedimu_log = []
        self.patikros_log = []
        self.log=[[],[]]
        self.kroviniai = kroviniai_laive + kroviniai_terminale
        self.laikas = 0

    def tikrinti_ar_vilkikas_veikia(self):
        if self.veikia == True:
            patikros_laikas = random.randint(1, 5)
            self.uzimtas_tikrinimu_laikas = self.uzimtas_tikrinimu_laikas + patikros_laikas
            print('Vilkiko veikimo patikros laikas:', patikros_laikas, 'min')
            self.patikros_log.append(patikros_laikas)
        else:
            taisymo_laikas = random.randint(25,60)
            patikros_laikas = random.randint(1, 5)
            print('Vilkiko veikimo patikros laikas:', patikros_laikas, 'min')
            print('Aptiktas gedimas, vilkikas bus taisomas', taisymo_laikas, 'min')
            self.veikia = True
            print('Vilkikas pataisytas')
            self.gedimu_prastovos = self.gedimu_prastovos + taisymo_laikas
            self.uzimtas_tikrinimu_laikas = self.uzimtas_tikrinimu_laikas + patikros_laikas
            self.gedimu_log.append(taisymo_laikas)
            self.patikros_log.append(patikros_laikas)


    def krovinio_svorio_patikra(self):
        print('tikrinama ar krovinys tinkamas krauti')
        krovinio_svoris = random.randint(1,85)
        if krovinio_svoris <= self.keliamoji_jega:
            print('krovinys praėjo patikrą')
            patikros_laikas = random.randint(1, 5)
            self.uzimtas_tikrinimu_laikas = self.uzimtas_tikrinimu_laikas + patikros_laikas
            print('Krovinys buvo tikrinamas', patikros_laikas, 'min')
            self.uzimtas_tikrinimu_laikas = self.uzimtas_tikrinimu_laikas + patikros_laikas
            self.patikros_log.append(patikros_laikas)
        else:
            print('krovinys nepraėjo patikros, taisomos specifikacijos')
            patikros_laikas = random.randint(5, 10)
            print('specifikacijos sutvarkytos, tęsiamas darbas')
            self.uzimtas_tikrinimu_laikas = self.uzimtas_tikrinimu_laikas + patikros_laikas
            print('Krovinys buvo tikrinamas', patikros_laikas, 'min')
            self.uzimtas_tikrinimu_laikas = self.uzimtas_tikrinimu_laikas + patikros_laikas
            self.patikros_log.append(patikros_laikas)

    def kelti(self):
        self.krovinio_svorio_patikra()
        self.tikrinti_ar_vilkikas_veikia()
        print('pradedami krovimo darbai')
        krovimo_laikas = 60 / self.nasumas
        print('krovimas užtruko', krovimo_laikas, 'min')
        self.krovimo_laikas = self.krovimo_laikas + krovimo_laikas
        self.atnaujinti_duomenis(self.patikros_log,self.gedimu_log)
        if random.randint(1,50) <= 2:
            self.veikia = False

    def atnaujinti_duomenis(self,patikros_laikai,gedimu_laikai):
        self.log[0] = patikros_laikai
        if self.log[0] == self.log[1]:
            self.log.pop()
        self.log[1] = gedimu_laikai
        self.laikas = self.gedimu_prastovos + self.krovimo_laikas + self.uzimtas_tikrinimu_laikas

class Laivas():
    def __init__(self):
        self.laikas = 0

    def iplaukti(self):
        print('laivas įplaukia')
        sugaistas_laikas = int(random.randint(12,35))
        print('laivas įplaukė per', sugaistas_laikas, 'min')
        self.laikas = self.laikas + sugaistas_laikas

    def isplaukti(self):
        print('laivas išplaukia')
        sugaistas_laikas = int(random.randint(10, 29))
        print('laivas išplaukė per', sugaistas_laikas, 'min')
        self.laikas = self.laikas + sugaistas_laikas


class Kontrole():
    def __init__(self,laivo_grimzle,uosto_gylis):
        self.laikas = 0
        self.laivo_grimzle = laivo_grimzle
        self.uosto_gylis = uosto_gylis

    def tikrinti_laiva(self):
        print('Kontrolės punktas\n---***---\n','tikrinamas laivas')
        if self.uosto_gylis>self.laivo_grimzle:
            print('laivas praėjo patikrą')
            self.laikas = self.laikas + int(random.expovariate(1/12))
            self.praleisti_laiva()
        elif self.laikas is 0:
            print('kontrolė galimai papirkta')
            '''
            TODO sukurti daugiau metodų kontrolei ateities modelyje
            '''
        else:
            sys.exit('laivas nepraėjo saugumo patikros, prašome paleisti simuliaciją iš'
                  ' naujo pakeitus laivo grizmlę bei uosto gylį, uosto gylis privalo būti didesnis už grimzlę')

    def praleisti_laiva(self):
        print('Duotas leidimas įplaukti')
        print('kontrolėje sugaišta:', self.laikas, 'min')

class Roro_terminalas():
    def __init__(self, kroviniu_skaicius_terminale, kroviniu_skaicius_laive):
        self.esamas_kroviniu_skaicius_terminale = kroviniu_skaicius_terminale
        self.esamas_kroviniu_skaicius_laive = kroviniu_skaicius_laive
        self.terminalo_statistika = []


    def iskrauta_reminale(self):
        self.esamas_kroviniu_skaicius_terminale = self.esamas_kroviniu_skaicius_terminale + 1
        self.esamas_kroviniu_skaicius_laive = self.esamas_kroviniu_skaicius_laive - 1
        self.terminalo_statistika.append(self.esamas_kroviniu_skaicius_terminale)
        print('krovinys iškrautas')

    def ikrauta_is_terminalo(self):
        self.esamas_kroviniu_skaicius_terminale = self.esamas_kroviniu_skaicius_terminale - 1
        self.esamas_kroviniu_skaicius_laive = self.esamas_kroviniu_skaicius_laive + 1
        self.terminalo_statistika.append(self.esamas_kroviniu_skaicius_terminale)
        print('krovinys įkrautas')


class Modelis():
    def __init__(self):
        self.nuskaityti_duomenis()
        self.isvesti_nustatytus_duomenis()

        terminalas = Roro_terminalas(self.kroviniu_skaicius_terminale,self.kroviniu_skaicius_laive)
        self.vilkikas = Ro_ro_vilkikas(self.nasumas,self.keliamoji_jega,self.kroviniu_skaicius_terminale,self.kroviniu_skaicius_laive)
        kontrole = Kontrole(self.laivo_grimzle, self.uosto_gylis)
        laivas = Laivas()
        kontrole.tikrinti_laiva()
        laivas.iplaukti()
        print('\n---!!!------!!!---\nPradėtas krovinių krovimas į terminalą iš laivo')
        while terminalas.esamas_kroviniu_skaicius_laive > 0:
            print('\n---***---\nIš laivo iškraunamas krovinys nr',
                  self.kroviniu_skaicius_laive - terminalas.esamas_kroviniu_skaicius_laive + 1)
            self.vilkikas.kelti()
            terminalas.iskrauta_reminale()
        print('\n---!!!------!!!---\nPradėtas krovinių įkrovimas į laivą iš terminalo')
        for x in range(terminalas.esamas_kroviniu_skaicius_terminale):
            print('\n---***---\nĮ laivą įkraunamas krovinys nr', x+1)
            self.vilkikas.kelti()
            terminalas.ikrauta_is_terminalo()
        print('\n---***---\nBaigti krovimo darbai')
        laivas.isplaukti()

        plt.plot(self.vilkikas.patikros_log)
        plt.title('Vilkiko patikros trukmės')
        plt.ylabel('Vilkiko patikros trukmė, min')
        plt.xlabel('Patikros skaičius')
        plt.show()
        if len(self.vilkikas.gedimu_log) > 1:
            plt.plot(self.vilkikas.gedimu_log)
            plt.title('Gedimų taisymo trukmės')
            plt.xlabel('Gedimo skaičius')
            plt.ylabel('Gedimo taisymo trukmė, min')
            plt.show()
        plt.plot(terminalas.terminalo_statistika)
        plt.title('Krovinių skaičius terminale')
        plt.xlabel('Krovinio krovimo skaičius')
        plt.ylabel('Krovinių skaičius terminale')
        plt.show()


        self.laivo_prastovos_laikas = self.sugaistas_laikas(self.vilkikas.laikas + kontrole.laikas)
        self.laikas = self.sugaistas_laikas(self.vilkikas.laikas + laivas.laikas + kontrole.laikas)
        self.patikru_laikas = kontrole.laikas + self.vilkikas.uzimtas_tikrinimu_laikas
        self.rezultatai()

    def nuskaityti_duomenis(self):
        with open('AM duomenys 17-TS-2 D.Šileva.csv', newline='', encoding='utf-8') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for row in spamreader:
                self.laivo_grimzle = int(row['laivo grimzlė'])
                if self.laivo_grimzle < 0:
                    print('laivo grimzlė negali būti neigiamas skaičius, nustatoma 100 metrų')
                    self.laivo_grimzle = 100
                self.kroviniu_skaicius_laive = int(row['konteineriai laive'])
                if self.kroviniu_skaicius_laive < 0:
                    print('konteineriai laive negali būti neigiamas skaičius, nustatoma 0 konteinerių')
                    self.kroviniu_skaicius_laive = 0
                self.uosto_gylis = int(row['uosto gylis'])
                if self.uosto_gylis < 0:
                    print('uosto gylis negali būti neigiamas skaičius, nustatoma 120 metrų')
                    self.uosto_gylis = 120
                self.nasumas = int(row['ro-ro vilkiko našumas'])
                if self.nasumas < 0:
                    print('ro-ro vilkiko našumas negali būti neigiamas skaičius, nustatomas 1')
                    self.nasumas = 1
                self.keliamoji_jega = int(row['ro-ro vilkiko keliamoji jėga'])
                if 65 > self.keliamoji_jega > 80:
                    print('keliamoji galia privalo būti minimaliai 65 tonos, maksimaliai 80 tonų')
                    self.keliamoji_jega = 80
                self.kroviniu_skaicius_terminale = int(row['krovinių skaičius terminale'])
                if self.kroviniu_skaicius_terminale < 0:
                    print('krovinių skaičius negali būti neigiamas skaičius, nustatomas 0')
                    self.kroviniu_skaicius_terminale = 0
                break

    def isvesti_nustatytus_duomenis(self):
        print('Nustatyti duomenys:\n---!!!------!!!---\nLaivo grimzlė: ', self.laivo_grimzle,
              '\nkroviniu_skaicius_laive:', self.kroviniu_skaicius_laive,
              '\nuosto gylis:', self.uosto_gylis,
              '\nro-ro vilkiko našumas:', self.nasumas,
              '\nro-ro vilkiko keliamoji jėga:', self.keliamoji_jega,
              '\nkrovinių skaičius terminale:', self.kroviniu_skaicius_terminale,'\n')

    def sugaistas_laikas(self, laikas_minutemis):
        paros = laikas_minutemis//60//24
        valandos = (laikas_minutemis - (paros*24*60))//60
        minutes = laikas_minutemis%60
        return paros,"paros",valandos,"valandos",minutes,"minutės"

    def rezultatai(self):
        with open('AM rezultatai 17-TS-2 D.Šileva.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Bendras sugaištas laikas',
                          'Sugaištas gedimų laikas',
                          'Sugaištas patikrų laikas',
                          'Laivo prastovos laikas',
                          'Laivo bei terminalo krovinių suma',
                          'Gedimų skaičius',
                          ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Bendras sugaištas laikas' : self.laikas,
                             'Sugaištas gedimų laikas': self.sugaistas_laikas(self.vilkikas.gedimu_prastovos),
                             'Sugaištas patikrų laikas': self.sugaistas_laikas(self.patikru_laikas),
                             'Laivo prastovos laikas' : self.laivo_prastovos_laikas,
                             'Laivo bei terminalo krovinių suma': self.vilkikas.kroviniai,
                             'Gedimų skaičius': len(self.vilkikas.gedimu_log),
                             })

Modelis()