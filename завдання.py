#masha 20.02.2022
print('Задача 1')
a= ('Salut')
print(a)
b= ("la revedere")
a=b
print(a)

print('Задача 2')
Name='masha'
print('Hello,',Name,'would you like to learn some Python today?')

print('Задача 3')
famous_person='Сократ'
message=' "Я знаю, що я нічого не знаю." '
print(famous_person +' once said '+ message)

print('Задача 4')
Namee=("  masha  ")
prieteni=('\n Sofia \t Arina \n Sasha \t Masha ')
print(prieteni)
g= Namee.lstrip()
y = Namee.rstrip()
z = Namee.strip()
print("jgekls", g,"wefaejf")
print("kragj", y,"jfhdfd")
print("fghvdrf", z,"kdfjf")
#adresa
print('Задача 5')
print('masha \n Укріїна  \n Чернівці́ \n Емінеску \n 6')

#метри в різних одиницях
print('Задача 6')
m = float(input("un numar de-l traduce: "))
livra = m * 3.280840
inci = m * 39.370
mile = m * 0.00062137
ярди= m * 1.0936
print('metri',m ,'\nlivra',livra  ,'\n inci',inci,'\nmile',mile,'\nярди',ярди)

print('Задача 7')
vacanta=int(input('introduceti un numar, ca sa aflati cate secunde sunt intr-o zi de vacanta: '))
ore_vacanta=24*vacanta
minute_vacanta=60*ore_vacanta
secende_vacanta=60*minute_vacanta
print('ore{0:10}, minute{1:10}, secunde{2:10}' .format(ore_vacanta, minute_vacanta, secende_vacanta))

print('Задача 8')
C = int(input('temperatura in grade:'))
F = C*32+9/5
K = C+273.15
print('celsia {:15,.2f}\n farengeit {:15,.2f} \n calvin  {:15,.2f}'.format(C,F,K))

print('Задача 9')
Num =int(input('Ведіть будь яке 4-ох значне число:'))
mii= Num // 1000
sute= (Num % 1000) //100
zecimi= (Num % 100) //10
unitate=Num%10
suma= mii+sute+zecimi+unitate
print('{}+{}+{}+{}={}'.format(mii,sute,zecimi,unitate,suma))

print('Задача 10')
import math
x1=39.9075000
y1 = 116.3972300
x2 = 50.4546600
y2 = 30.5238000
M1= math.radians(x1)
M2= math.radians(x2)
K1= math.radians(y1)
K2= math.radians(y2)

distantie = 6371.032 * math.acos(math.sin(M1) * math.sin(M2) + math.cos(M1) * math.cos(M2) * math.cos(K1 - K2))
print(f'{distantie:.3f}')
