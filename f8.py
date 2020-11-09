print(str(round(12.145641, 2)) + ' ' + str(round(105.4587, 2)) + ' ' + str(round(0.125484, 2)) + ' ' + str(round(-14.5214, 2)))



a = "+1"
b = "+2"
c = "+3"
print(a[1:], b[1:], c[1:])

d = "02"
e = "03"
f = "04"
g = "05"
print(d[1:], e[1:], f[1:], g[1:])

h = "2.000"
i = "3.000.000"
hh = h.replace(".","")
print(hh)



def table(string):
  eredmeny = ""
  lenght = 10 - len(string)
  while 0 < lenght:
    eredmeny = eredmeny + '*'
    lenght = lenght - 1
  print(eredmeny + string)


table("10")
table("20")
table("100")
table("1000")
table("10000")
table("20000")



szam1 = int(12.11)
szam2 = int(-105.87)
szam3 = int(147.125484)
szam4 = int(-14.5214)
print(szam1, szam2, szam3, szam4)




def table2(string):
  if int(string) %2 == 0:
    eredmeny = ""
    lenght = 15 - len(string)
    while 0 < lenght:
      eredmeny = eredmeny + ' '
      lenght = lenght - 1
    print(eredmeny + string)
  else:
    eredmeny = ""
    lenght = 15 - len(string)
    while 0 < lenght:
      eredmeny = eredmeny + ' '
      lenght = lenght - 1
    print(string + eredmeny)



table2("1001")
table2("1020")
table2("3333")
table2("4040")
table2("8008")
table2("999")
table2("6666")
table2("10007")
table2("80088")
table2("10001")
table2("100000")