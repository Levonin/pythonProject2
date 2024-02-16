#7
numbrid = []
try:
    num_count = int(input("Sisestage loendi elementide arv: ")) #kusime siit inimest kui palju elementi ta tahab
    for _ in range(num_count):
        numbrid.append(int(input("sisestage numbrit: ")))
    choice = int(input("Sisesta 1 tõusvas järjekorras või 2 kahanevas järjekorras: ")) #kusime kas ta tahab tousvas jarjekorras voi kahanevas
    if choice == 1:
        sorted_numbrid = sorted(numbrid, key=abs) #me kasutame funktsiooni sorted et sorteerida abs väärtuse
        print(sorted_numbrid)
    elif choice == 2:
        sorted_numbrid = sorted(numbrid, key=abs, reverse=True)
        print(sorted_numbrid)
    else:
        print("Vigane valik. Sisesta 1 tõusvas järjekorras või 2 kahanevas järjekorras.")

except ValueError:
    print("Vigane sisend. Palun sisestage kehtivad täisarvud.")

#9
try:
    nimi= input("kirjutage teie nimet: ").strip()
    if not nimi.isalpha():
        raise ValueError("nimi peab siseldama ainult tähtid")
    else:
        print(f"tere, {nimi.capitalize()}!")

    nimi_len = len(nimi)
    vookal = sum(1 for letter in nimi if letter.lower() in 'aeiou')
    Konsonandid = sum(1 for letter in nimi if letter.isalpha() and letter.lower() not in 'aeiou')
    print(f"Nime pikkus: {nimi_len}")
    print(f"vookaleid: {vookal}")
    print(f"Konsonantide tähed: {Konsonandid}")

    kirjad_sorteeritud = sorted(set(nimi))
    for kirjad in kirjad_sorteeritud:
            print(kirjad, end=" ")
except:
    print("Sisestusviga. Proovige uuesti.")




#12
from random import *
try:
    numbers = [randint(1, 100) for _ in range(10)]
    min_num = min(numbers)
    max_num = max(numbers)
    numbers[numbers.index(min_num)] = max_num
    numbers[numbers.index(max_num)] = min_num
    print(numbers)
except ValueError as e:
    print("Error:", e)


#11
import string
try:
    tahestik = string.ascii_lowercase
    result_1 = [kirjad for i, kirjad in enumerate(tahestik)]
    result_2 = [kirjad * (i+1) for i, kirjad in enumerate(tahestik)]
    print(result_1)
    print(result_2)
except Exception as e:
    print("Error:", e)


#18
from random import *
numbers = [randint(1, 10) for i in range(10)]
# kordamine elementi kahele * 2
result = [num * 2 for num in numbers]

print(result)

