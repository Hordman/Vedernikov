"# -- coding: utf-8 --"
print("Введите свой возраст")
age=int(input())
print("Вас зовут Иван?(1-да, 0-нет)")
a=int(input())
if a == 1:
    print("Извините Иванам нельзя")
elif age <= 0:
    print("Вас не существует")
elif age >= 75:
    print("Вы уже старый для обучения ")
elif age==16 or age>=16:
    print("Поздравляю вы поступили во ВГУИТ")
elif age <16:
    b = 16 - age
    if b <= 9:
        print("Вам учиться ещё",b,"лет")
    else: print("Вы ещё слишком молодой")
