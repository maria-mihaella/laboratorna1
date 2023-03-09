print('Вправа 1')
print(60*60)

print('Вправа 2')
hour= int(input('Скільки годин:'))
print(hour*60*60)

print('Вправа 3')
seconds_per_hour=60*60
print(seconds_per_hour*24)

print('Вправа 4')
seconds_per_day=60*60*24
print(seconds_per_day)

print('Вправа 5')
print(seconds_per_day / seconds_per_hour)

print('Вправа 6')
print(seconds_per_day // seconds_per_hour)

print('Вправа 7')
print(5 + 7)
print(13 - 1)
print(24 / 2)
print(3 * 4)

print('Вправа 8')
a=('10')
print('Моє улюблене число',a,)

print('Вправа 9')
# nume=ім'я
nume= 'masha'
print(str.lower(nume))
print(str.upper(nume))
print(str.swapcase(nume))

#поем
print('Вправа 10')
poem ='''Yes, I'll smile, indeed, through tears and weeping
Sing my songs where evil holds its sway,
Hopeless, a steadfast hope forever keeping,
I shall live! You thoughts of grief, away!'''
#1
print(poem)
print(poem[:15])
#2
print(len(poem))
#3
print(poem.startswith('Yes'))
#4
print(poem.endswith('I shall live!'))
#5
print(poem.find(','))
#6
print(poem.rfind(','))
#7
print(poem.count(','))
#8
print(poem.isalnum())
