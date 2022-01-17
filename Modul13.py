print("Укажите количество билетов которое хотите купить")
count=int(input())
i=1
summ=0
while i<=count:
    print("Укажите возраст",i,"посетителя")
    age=int(input())
    if age<18:
        summ+=0
    elif age<25:
        summ+=990
    else: 
        summ+=1390
    i+=1
if count>=3:
    summ=summ*0.9
print("Общая сумма вашего заказа ",summ," рублей")