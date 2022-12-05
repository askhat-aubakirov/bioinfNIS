'''
if, elif, else
lect 14

for
lect 15

continue and break
lect 16 + 17

try and except
lect 18

functions
lect 19

modules and libraries
lect 20

oop
lect 21

inheritance
lect 22
'''

#space for code

pocket = ["ticket1", "ticket2", "ticket3"]
'''
for element in pocket:
  print(element)
'''
'''
#pop() - удаляет один элемент из выбранного списка
while pocket:
  pocket.pop()
  print(pocket)

for i in list:
  if i == "bottle of water":
    print()
  elif i == "":
    print

'''

#time to solve a question
''' 
Уравнение Харди-Вайнберга:

--- p + q = 1 ---
--- p^2  + 2pq + q^2 = 1 ---

где p2 – частота гомозиготных особей по доминантному аллелю (генотип АА), 2pq – частота гетерозигот (генотип Аa), q2 – частота гомозиготных особей по рецессивному аллелю (генотип аа).

Альбинизм у людей контролируется рецессивным аллелем диаллельного локуса (А, а). Среди 34500 родившихся в одном крупном административном регионе европейской страны родилось 2 ребенка, страдающих альбинизмом. Определите частоты аллелей (а) и (А), частоту гетерозиготных детей в этом регионе европейской страны, используя формулы из положений закона Харди-Вайнберга.
'''
'''
from math import sqrt

overall_num = 34500
alb_num = 2

freq_q_sqr = alb_num / overall_num
print(f"Frequency of homozygotes: {freq_q_sqr*100} %")
q = sqrt(freq_q_sqr)
p = 1 - q
freq_two_pq = 2 * p * q
print("Frequency of heterozygotes:", freq_two_pq * 100)

print(f"Frequency of heterozygotes: {freq_two_pq*100} %")

print(f"value of overall amount of samples is {overall_num}")

# functions

'''
'''
# 24 52 2.6
print(square (w))
return
'''
side1 = 52
d=side1**2

print(d)

def squareArea(a):
  return a**2


print(squareArea(5))
print(squareArea(2.6))
