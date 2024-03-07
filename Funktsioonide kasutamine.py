# from MyModul import *
# b=int(input("Sisesta arv2: "))
# summa_3=Summa(3,b,int(input("kolmas arv: ")))
# summa_31=Summa(100,100)
# print(summa_3)
# print(summa_31)
# 2
# from MyModul import *
# try:
#     aasta=float(input("Sisestage Aasta: "))
#     print(liigaasta(aasta))
# except ValueError:
#     pass
#
# 3
# from MyModul import *
# try:
#     ruudukülg = int(input("Palun sisestage ruudu küljed: "))
#     if ruudukülg != ruudukülg:
#         print("Palun sisestage 3 küljet.")
#     else:
#         perimeeter, pindala, diagonaal = square(ruudukülg)
#         print(perimeeter, pindala, round(diagonaal, 2))
# except ValueError:
#     print("Palun sisestage kehtiv külje pikkus numbrina.")
#
#
# 4
# from MyModul import *
# while True:
#     try:
#         kuu=int(input("kuu number: "))
#         break
#     except:
#         print("viga")
# a=season(kuu)
# print(a)

# 6
#
# from MyModul import *
# arv=int(input("Sisestage arvu: "))
# print(is_prime(arv))
#
#
# 7
#
# from MyModul import *
# paev=int(input("kirjutage paeva: "))
# kuu=int(input("kirjutage kuut: "))
# aasta=int(input("kirjutage aasta: "))
#
# print(date(paev, kuu, aasta))
#
# from MyModul import *
# a=float(input("sisestage a raha: "))
# aasta=int(input("Sisestage kui palju aastaks: "))
#
# print("teie tagastatud summa on: ",pank(a,aasta))
#
from MyModul import *

# palgad=[1200,2500,750,395,1200]
# inimesed = ["A","B","C","D","E"]
#
#
# def järjesta_palgad(inimesed, palgad):
#     pass
#
#
# while True:
#
#     print("0-Näita anded veerudes\n1-andmete lisamine\n2-andmete_emaaldamine_nimi_jargi\n3-kellel_on_suurim_palk\n4-kellel_on_vahem_palk\n5-järjesta_palgad")
#     valik=int(input())
#     if valik==1:
#         inimesed,palgad=inimeste_ja_palkade_lisamine(inimesed,palgad,int(input("Mitu inimest lisame?")))
#     elif valik==0:
#         andmed_veerudes(inimesed,palgad)
#
#     elif valik==2:
#         andmete_kustutamine_nimi_jargi(inimesed,palgad)
#     elif valik==3:
#         kellel_on_suurim_palk(inimesed,palgad)
#     elif valik==4:
#         kellel_on_vahem_palk(inimesed,palgad)
#     elif valik==5:
#         järjesta_palgad(inimesed,palgad)
#     elif valik==6:
#         sorteerimine(inimesed,palgad)


import MyModul

kasutajad = []
paroolid = []
while True:
    print("Valikud:")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime või parooli muutmine")
    print("4 - Unustasin parooli")
    print("5 - Lõpetamine")

    valik = input("Valige tegevus: ")
    if valik == "1":
        kasutajanimi = input("Sisestage kasutajanimi: ")
        if kasutajanimi in kasutajad:
            print("Kasutajanimi on juba olemas.")
        else:
            parooli_valik = input("Valige parooli loomise viis (auto/kasutaja): ")
            if parooli_valik == "auto":
                parool = MyModul.genereeri_random_parooli()
                kasutajanimi.append(kasutajanimi)
                paroolid.append(parool)
                print(f"Kasutaja '{kasutajanimi}' loodud parooliga: {paroolid}")
            elif parooli_valik == "kasutaja":
                oma_pikkus = int(input("Sisestage parooli pikkus: "))
                oma_parool = MyModul.genereeri_oma_parooli(oma_pikkus)
                if MyModul.kontrollige_parooli_joudu(oma_parool):
                    kasutajanimi.append(kasutajanimi)
                    paroolid.append(oma_parool)
                    print(f"Kasutaja '{kasutajanimi}' loodud parooliga: {oma_parool}")
                else:
                    print("Parool ei vasta nõuetele.")
            else:
                print("Vale valik.")
    elif valik == "2":
        kasutajanimi = input("Sisestage kasutajanimi: ")
        parool = input("Sisestage parool: ")
        if kasutajanimi in kasutajad:
            index = kasutajad.index(kasutajanimi)
            if parool[index] == parool:
                print(f"Kasutaja '{kasutajanimi}' autoriseeritud.")
            else:
                print("Vale parool.")
        else:
            print("Kasutajat ei leitud.")
    elif valik == "5":
        break
    else:
        print("Vale valik.")



