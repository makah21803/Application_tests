from random import randrange

my_list = []

for i in range(100000):
    n = randrange(-50000, 50000, 1)
    my_list.append(n)

print(my_list)