# 1 is_prime(n) funksiyasi

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True  


print(is_prime(7))
print(is_prime(10))
print(is_prime(11))











# 2 digit_sum(k) funksiyasi
n = int(input("Enter a number: "))

def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

digit_sum(n)









# 3 Ikki sonning darajalari

def power(n):
    for i in range(1, n):
        global b
        b = 2 ** i
        if b < n:
            print(b)
power(20)









# Working with JSON
import json
import os
import requests

with open("actors.json", "r") as file:
    actors = json.load(file)

if not os.path.exists("Projects"):
    os.mkdir("Projects")
os.chdir("Projects")

for actor in actors:
    os.mkdir(actor["name"])
    os.chdir(actor["name"])
    image_filename = f'{actor['name'].replace(' ', '_')}.jpg'
    with open(image_filename, "wb") as file:
        file.write(requests.get(actor['image']).content)
    os.chdir("..")
os.chdir("..")
