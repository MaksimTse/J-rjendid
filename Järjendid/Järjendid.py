from math import *


spisok=[] #tühi järjend
numbers=[1,2,3,4,5] #numbriline järjend
abc=['Abc','B','C'] 
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
#while True:
#    print('1 - lisage loendisse täht\n2 - liiminimekirjad\n3 - lisage positsioonile täht\n4 - kustutuda element\n5 - sorteerib tähed alustades kapitalist ja A kuni Z\n6 - sorteerib tähed alustades kapitalist ja A kuni Z aga vastupidi')
#    print('7 - kustutab valitud tähe numbri järgi \n8 - eemaldab tähe ja jätab tühiku \n9 - kuvatakse sisestatud numbri all\n10 - puhastab järjend')
#    valik=int(input())
#    if valik==1:
#        a=input('sisesta täht: ')
#        slovo_list.append(a)
#        print(f'sa lisatud {a}',slovo_list)
#    elif valik==2:
#        slovo_list.extend(abc)
#        print(slovo_list)
#    elif valik==3:
#        a=input('Sisestage täht, mida soovite lisada: ')
#        i=int(input('Sisestage positsiooni number, kuhu soovite tähe lisada: '))
#        slovo_list.insert(i-1,a) #0,1,2...
#        print(slovo_list)
#    elif valik==4:
#        a=input("Sisesta täht, mille tahad kustutuda: ")
#        n=slovo_list.count(a)
#        if n>0:
#            for x in range(n):
#                slovo_list.remove(a)
#        else:
#             print('Otsitav kiri on puudu')
#        print(slovo_list)
#    elif valik == 5:
#        slovo_list.sort()
#        print(slovo_list)
#    elif valik == 6:
#        slovo_list.sort(reverse=True)
#        print(slovo_list)
#    elif valik == 7:
#        a=int(input('Sisestage number, millel on kustutatav täht: '))
#        slovo_list.pop(a)
#        print(slovo_list)
#    elif valik == 8:
#        a=input('Sisetage täht: ')
#        r=int(input('Mitu tähte jagada?: '))
#        x = slovo.split(a,r)
#        print(x)
#    elif valik == 9:
#        a = int(input('sisestage number: '))
#        print(slovo_list[a-1])
#    elif valik == 10:
#        slovo_list.clear()
#        print(slovo_list)

while True:
    print('1 - lisage loendisse täht\n2 - liiminimekirjad\n3 - lisage positsioonile täht\n4 - kustutuda element\n5 - sorteerib tähed alustades kapitalist ja A kuni Z\n6 - sorteerib tähed alustades kapitalist ja A kuni Z aga vastupidi')
    print('7 - kustutab valitud tähe numbri järgi \n8 - eemaldab tähe ja jätab tühiku \n9 - kuvatakse sisestatud numbri all\n10 - puhastab järjend')
    while True:
        try:
            valik = int(input("Sisestage oma valik: "))
            if valik < 1 or valik > 10:
                raise ValueError("Palun sisestage arv vahemikus 1 kuni 10.")
            break
        except ValueError as e:
            print(e)
    if valik == 1:
        while True:
            try:
                a = input('sisesta täht: ')
                if not a.isalpha():
                    raise ValueError("Sisestage kehtiv märk.")
                break
            except ValueError as e:
                print(e)
        slovo_list.append(a)
        print(f'sa lisatud {a}', slovo_list)
    elif valik == 2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik == 3:
        while True:
            try:
                a = input('Sisestage täht, mida soovite lisada: ')
                if not a.isalpha():
                    raise ValueError("Sisestage kehtiv märk.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                i = int(input('Sisestage positsiooni number, kuhu soovite tähe lisada: '))
                if i < 1:
                    raise ValueError("Palun sisestage positiivne arv.")
                break
            except ValueError as e:
                print(e)
        slovo_list.insert(i-1, a) #0,1,2...
        print(slovo_list)
    elif valik == 4:
        while True:
            try:
                a = input("Sisesta täht, mille tahad kustutuda: ")
                if not a.isalpha():
                    raise ValueError("Sisestage kehtiv märk.")
                break
            except ValueError as e:
                print(e)
        n = slovo_list.count(a)
        if n > 0:
            for x in range(n):
                        slovo_list.remove(a)
        else:
            print('Otsitav kiri on puudu')
        print(slovo_list)
    elif valik == 5:
        slovo_list.sort()
        print(slovo_list)
    elif valik == 6:
        slovo_list.sort(reverse=True)
        print(slovo_list)
    elif valik == 7:
        while True:
            try:
                a = int(input('Sisestage number, millel on kustutatav täht: '))
                if a < 0:
                    raise ValueError("Sisestage mittenegatiivne arv.")
                break
            except ValueError as e:
                print(e)
        slovo_list.pop(a)
        print(slovo_list)
    elif valik == 8:
        while True:
            try:
                a = input('Sisetage täht: ')
                if not a.isalpha():
                    raise ValueError("Sisestage kehtiv märk.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                r = int(input('Mitu tähte jagada?: '))
                if r < 1:
                    raise ValueError("Sisestage kehtiv märk.")
                break
            except ValueError as e:
                print(e)
        x = slovo.split(a,r)
        print(x)
    elif valik == 9:
        while True:
            try:
                a = int(input('sisestage number: '))
                if a < 1:
                    raise ValueError("Sisestage kehtiv märk.")
                break
            except ValueError as e:
                print(e)
        print(slovo_list[a-1])
    elif valik == 10:
        slovo_list.clear()
        print(slovo_list)
