# 1
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_leap(2000))
print(is_leap(2100))
print(is_leap(2024))
print(is_leap(1993))





# 2
n = int(input().strip())

if n % 2 == 1: 
    print("Weird")
elif 2 <= n <= 5: 
    print("Not Weird")
elif 6 <= n <= 20:  
    print("Weird")
else:  
    print("Not Weird")







# 3.1 
a = int(input())
b = int(input())

if a % 2 != 0:
    a += 1 
if b % 2 != 0:
    b -= 1 

if a > b:
    print("")  
else:
    c = range(a, b + 1, 2)
    print(*c)  






# 3.2
a = int(input())
b = int(input())

a += (a % 2)
b -= (b % 2)

print(*list(range(a, b + 1, 2)) * (a <= b))
