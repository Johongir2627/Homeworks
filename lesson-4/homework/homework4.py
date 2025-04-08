# Dictionary
# 1
a = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 2}
b = dict(sorted(a.items(), key=lambda item: item[1]))
c = dict(sorted(a.items(), key=lambda item: item[1], reverse=True))

print(f'Ascending: {b}')
print(f'Descending: {c}')




# 2
a = {0: 10, 1: 20}
a[2] = 30
print(a)




# 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic_1_2 = dic1.copy()
dic_1_2.update(dic2)
dic_1_2.update(dic3)

print(dic_1_2)



#4
n = int(input('Enter an integer: '))
b = {} 
for i in range(1, n+1):
    a = {i: i**2} 
    b.update(a) 
print(b)




#5
b = {} 
for i in range(1, 16):
    a = {i: i**2} 
    b.update(a) 
print(b)



# Sets
# 1
import random
f = []
for i in range(5):
    a = random.randint(1, 20)
    f.append(a)
print(set(f))




# 2
my_set = {1, 2, 3, 4, 5}

for i in my_set:
    print(i)




# 3
my_set = {2, 3, 5, 6, 7, 9}
my_set.add(8)
print(my_set)




# 4
my_set = {2, 3, 5, 6, 7, 9}
my_set.remove(5)
print(my_set)





# 5
my_set = {2, 3, 5, 6, 7, 9}
if 8 in my_set:
    my_set.remove(8)
print(my_set)
