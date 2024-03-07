# def Summa(arv1:int,arv2:int,arv3=0) -> int:
#     """ Funktsioon tagastab kolme arvu summa
#         Summa(arv1,arv2,arv3)
#     :param int arv1: Arv1 Sisestab kasutaja
#     :param int arv2: Arv2 Sisestab kasutaja
#     :param int arv3: Vaikimisi arv3 võrdub nulliga
#     :rtype: int
#     """
#
#     s=arv1+arv2+arv3
#     return s
# def IntKontroll():
#
#     def arithmetic(x: int, y: int, op:str) -> float:
#         """ Funktsioon tagastab kolme arvu summa
#             arithmetic(x, y, op)
#         :param int x: x sisestab kasutaja
#         :param int y: y sisestab kasutaja
#         :param str op: str sisestab kasutaja
#         :rtype: int
#         """
#         if op == "+":
#             return x + y
#         if op == "-":
#             return x - y
#         if op == "*":
#             return (x * y)
#         if op == "/":
#             if y == 0:
#                 print("jagamine nulliga ei ole võimalik")
#             else:
#                 print("tundmatu toiming")
# #
# #
# #
# #
# def liigaasta(aasta:int)->bool:
#     """ funktsioon loeb kas on liigasta voi ei
#     liigaasta(aasta:int)
#     :param int aasta: aasta sisestab kasutaja
#     :rtype: bool
#     """
#     if aasta % 4 == 0 and aasta % 100!=0:
#         return True
#     else:
#         return False
#
# # 3
# import math
#
# def square(ruudukülg:float)->tuple:
#     """ funktsioon tagastab kolm väärtusi(umbermoot,pindala,diagonaal)
#     square(ruudukülg:float)
#     :param float ruudukülg: ruudu_külg sisestab kasutaja
#     :rtype: tuple
#     """
#
#
#     umbermoot = 4 * ruudukülg
#     pindala = ruudukülg ** 2
#     diagonaal = ruudukülg * math.sqrt(2)
#     return umbermoot, pindala, diagonaal
#
#
# def season(a:int)->str:
#     """funktsioon tagastab hooaega nimetusi(talv, kevad, suvi,sügis)
#     season(a:int)
#     param int a: kuut sisestab kasutaja
#     return: str
#     """
#
#     while True:
#         if a>0 and a<13:
#             break
#         else:
#             try:
#                 a=int(input("Ainult 1-12!\n  sisesta veel kord number: "))
#             except:
#                 print("viga andmetüübiga")
#     if a==12 or a==1 or a==2:
#         s="talv"
#     elif a>2 and a<6:
#         s="kevad"
#     elif a in range (6,9,1):
#         s="suvi"
#     elif 9<=a<=11:
#         s="sugis"
#     return s
#
#
# def is_prime(arv:int)->bool:
#     """funktsioon tagastab arvu(0,1000) kas ta on lihtne voi ei
#     is_prime(arv:int)
#     param int arv:arvu sisestab kasutaja
#     rtype:bool
#     """
#
#     y = 0
#     for i in range(1, arv + 1):
#         if arv % i == 0:
#             y += 1
#     if y > 2:
#         return False
#     else:
#         return True
#
#
#
#
#
#
# def date(paev:int,kuu:int,aasta:int)->bool:
#         """funktsioon tagastab true kui kuu paev on kalendris(paev,kuu,aasta)
#         date(paev:int,kuu:int,aasta:int)
#         :param int paev: paeva sisestab kasutaja
#         :param int kuu: kuu sisestab kasutaja
#         :param int aasta: aasta sisestab kasutaja
#         return:bool
#         """
#
#         paeva_in_kuu = {1: 31,
#                         2: 29 if liigaasta(aasta) else 28,
#                         3: 31,
#                         4: 30,
#                         5: 31,
#                         6: 30,
#                         7: 31,
#                         8: 31,
#                         9: 30,
#                         10: 31,
#                         11: 30,
#                         12: 31}
#
#         if 1 <= kuu <= 12 and 1 <= paev <= paeva_in_kuu[kuu]:
#             return True
#         else:
#             return False
#
#
# def pank(a:float,aasta:int)->bool:
#     """funktsioon tagastab summat mis on kontos kasutajal(a,aasta)
#     pank(a:float,aasta:int)
#     :param float a: a sisestab kasutaja
#     :param int aasta: aasta sisestab kasutaja
#     rtype:any
#     """
#     for i in range(aasta):
#         a *= 1.1
#     return a

# def inimeste_ja_palkade_lisamine(i: list, p: list, n=1) -> any:
#     """funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
#     :param  list i: inimeste järjend
#     :param  list p: palgate järjend
#     :param  list n: inimeste arv
#     :rtype: list,list
#     """
#     if n >= 0:
#         for j in range(n):
#             nimi = input("Nimi: ").capitalize()
#             palk = int(input("Palk: "))
#             i.append(nimi)
#             p.append(palk)
#     return i, p
#
#
# def andmed_veerudes(i: list, p: list):
#     """funktsioon kuvab ekraanile kahe järjendite andmed veerudes
#     :param  list i: inimeste järjend
#     :param  list p: palgate järjend
#     """
#
#     for j in range(len(i)):
#         print(i[j], "-", p[j])
#
#
# def andmete_kustutamine_nimi_jargi(i: list, p: list) -> any:
#     """funktsioon kustutab andmeid ja tagastab listid .
#
#     :param  list i: inimeste järjend
#     :param  list p: palgate järjend
#     :rtype: list,list
#     """
# def kellel_on_suurim_palk(i:list,p:list)->list:
#     """Funktsioon näitab kellel on suurim palk
#     :param list i:Inimeste järjend
#     :param list p:Inimeste järjend
#
#     """
#     nimed=[]
#     max_palk=max(p)
#     ind=-1
#     for palk in p:
#         if palk==max_palk:
#             ind+=1
#             nimi=i[p.index(palk,ind)]
#             nimed.append(nimi)
#     return nimed
#
# def kellel_on_vahem_palk(i:list,p:list)->list:
#     """Funktsioon näitab kellel on väiksem palk
#     :param list i:Inimeste järjend
#     :param list p:Inimeste järjend
#
#     """
#     nimed=[]
#     min_palk=min(p)
#     ind=-1
#     for palk in p:
#         if palk==min_palk:
#             ind+=1
#             nimi=i[p.index(palk,ind)]
#             nimed.append(nimi)
#     return nimed
#
#
#
#     nimi = input("keda kustutada ära(nimi): ")
#     for j in range(0, len(i)):
#         if nimi in i:
#             i.remove(nimi)
#             p.pop(j)
#     return i,p
#
#
#
# def sorteerimine (i:list,p:list):
#     """funktsioon tagastab sorteeritud palgad
#     :param list i: Inimeste jarjend
#     :param list p: palgade jarjend
#     """
#
#
#
#     for n in range(0,len(i)):
#         for m in range(n,len(i)):
#             if p[n]>p[m]:
#                 p[m],p[n]=p[n],p[m]
#                 i[m], i[n] = i[n], i[m]
#     return i,p


import random
import string


def genereeri_random_parooli(str0:str, str1:int, str2:str)->any:

    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    parool = ''.join([random.choice(ls) for x in range(12)])
    return parool


def genereeri_oma_parooli(pikkus:int)->int:
    parool = ""
    for i in range(pikkus):
        t = random.choice(string.ascii_letters)
        numbrid= random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        t_num = [t, str(numbrid)]
        parool += random.choice(t_num)
    return parool


def kontrollige_parooli_joudu(parool):
    kas_on_digit = any(char.isdigit() for char in parool)
    kas_on_upper = any(char.isupper() for char in parool)
    kas_on_lower = any(char.islower() for char in parool)
    kas_on_special = any(char in string.punctuation for char in parool)

    return kas_on_digit and kas_on_upper and kas_on_lower and kas_on_special

