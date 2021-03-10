
# zad1

# a=23
# b=43
# c=2.45
# d=45.23
# e='ala'
# f='kot'
# g=23+2j
# h=543+34j
# print('zmienne typu integer: a=%(z1)d, b=%(z2)d'%{'z1':a, 'z2':b})
# print('zmienne typu float: c=%(z1)f, d=%(z2)f'%{'z1':c, 'z2':d})
# print('zmienne typu integer: e=%(z1)s, f=%(z2)s'%{'z1':e, 'z2':f})
# print('zmienne typu complex)')
# print(g)
# print(h)

# zad2

# def dodawanie (a,b):
#     return a+b
# def odejmowanie (a,b):
#     return a-b
# def dzielenie (a,b):
#     return a/b
# def mnozenie (a,b):
#     return a*b
# print ('wybierz operację, jaką chcesz wykonać.\ndodawanie- 1\nodejmowanie- 2\ndzielenie- 3\nmnożenie- 4')
# while True:
#     wybor = input()
#     if wybor in ('1','2','3','4'):
#         a = float(input('podaj pierwszą liczbę a='))
#         b = float(input('podaj drugą liczbę b='))
#
#         if wybor == '1':
#             print(dodawanie(a,b))
#
#         elif wybor == '2':
#             print(a, '-', b, '=', odejmowanie(a,b))
#
#         elif wybor == '3':
#             print(a, '/', b, '=', dzielenie(a, b))
#
#         elif wybor == '4':
#             print(a, '*', b, '=', mnozenie(a, b))
#         break
#     else:
#         print('wprowadzono niepoprawną opcję')
#     break

#zad3
#
# a,b,c,d,e,f=2,2,2,2,2,2
# a+=2
# print(a)
# b-=2
# print(b)
# c*=3
# print(c)
# d**=3
# print(d)
# e/=3
# print(d)
# e%=5
# print(e)

#zad4
#
# from math import*
# a=e
# print('a= ', a**10)
# b=(log10(5+sin(8)**2))**(1/6)
# print('b= ',b)

# zad5
#
# imie='PAWEŁ'
# nazwisko='LESZCZYŃSKI'
# print(imie.capitalize()+' '+nazwisko.capitalize())
#
# zad6

# tekst='run to the hills run for your lives run to the hills run for your lives'
# run='run'
# licznik=tekst.count(run)
# print('słowo run pojawia się %(zm)d razy'%{'zm':licznik})
#
# zad7
#
# napis='ala ma kota'
# print('pierwszy znak i ostatni znak:',napis[0],' ',napis[10])
#
# zad8
#
# tekst='run to the hills run for your lives run to the hills run for your lives'
# print(tekst.split(" "))
#
# zad9
#
# a=hex(25)
# print(a)
# b='tekst'
# print(b)
# c=23.12433
# print(c)
