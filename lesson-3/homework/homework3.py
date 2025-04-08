# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
fruits = ['apple', 'banana', 'cherry', 'pineapple', 'apricot']
print(fruits[2])




# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
a = [5, 6, 9, 5]
b = [6, 8, 9]
c = a + b
print(c)




# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
a = [1, 2, 5, 9, 7, 8, 6]
if len(a) % 2 == 1:
    print([a[0], a[len(a) // 2], a[-1]])
else:
    print([a[0], a[len(a) // 2-1], a[len(a) // 2], a[-1]])




# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Avengers: Endgame"]
movies_tuple = tuple(favorite_movies)
print(movies_tuple)





# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
# Step 1: Create a list of cities
cities = ["Washington", "London", "Istambul", "Tokyo", "Moscow",  "Paris", "Sydney"]

if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")





# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3, 4, 5]
duplicated = numbers * 2 
print(duplicated)





# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
a = [1, 2, 3, 4, 5]
a[0], a[-1] = a[-1], a[0]
print(a)





# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a[3:8])





#9. Count Occurrences in a List
#Create a list of colors and count how many times "blue" appears in the list.
a = ['red', 'blue', 'black', 'blue', 'white']
b = a.count('blue')
print(b)




#10. Find the Index of an Element in a Tuple
#Given a tuple of animals, find the index of "lion".
a = ['graffe', 'wolf', 'lion', 'cow']
print(a.index('lion'))




# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
a = (1, 2, 3)
b = (7, 8, 9)
c = a + b
print(c)





# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.
a = [1, 2, 3]
b = (6, 7, 8, 9)
print(len(a))
print(len(b))





# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
b = (5, 6, 7, 8, 9)
c = list(b)
print(c)





# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
b = (5, 6, 7, 8, 9)
print(f'max = {max(b)} \nmin = {min(b)}')





#15. Reverse a Tuple
#Create a tuple of words and print it in reverse order.
a = ['graffe', 'wolf', 'lion', 'cow']
b = a[::-1]
print(b)
