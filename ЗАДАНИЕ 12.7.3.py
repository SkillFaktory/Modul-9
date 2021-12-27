per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} 
money=int(input("Сумма которую кладем под проценты:"))
deposit=[]
for key, value in per_cent.items():
    deposit.append(int(value*money/100))
print(deposit)
max_number = max(deposit)
print("Максимальная сумма, которую вы можете заработать:", max_number)
