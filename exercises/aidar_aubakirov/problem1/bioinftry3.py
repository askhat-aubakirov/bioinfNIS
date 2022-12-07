# Written by Aidar Aubakirov

# 07.12.2022 01:04 pm 
# I am satisfied with this solution
# Askhat

import random

len_mol1 = 121024
len_mol = len_mol1
time = 10800
mass_one = 345
count = 0
for i in range(time):
    speed = random.randint(50, 100)
    len_mol = len_mol - speed
    count += 1
    if len_mol <= 0:
        break
    else:
        continue
nukl_num = 2**(time/count)
total_mass = len_mol1 * 2 * mass_one * nukl_num
print(len(str(total_mass)))

