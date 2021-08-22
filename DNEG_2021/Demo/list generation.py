from random import randrange

my_list = []

for i in range(200):
    n = randrange(-200, 200, 1)
    my_list.append(n)

print(my_list)