#1.
import json

# Specify the path to the JSON file
file_path = 'students.json'

try:
    # Open and load the JSON file
    with open(file_path, 'r') as file:
        students_data = json.load(file)
    
    # Iterate through each student and print their details
    for student in students_data.get('students', []):
        print(f"Name: {student.get('name', 'N/A')}")
        print(f"Age: {student.get('age', 'N/A')}")
        print(f"Grade: {student.get('grade', 'N/A')}")
        print("-" * 20)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from the file '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")








#2.
import requests

# OpenWeatherMap API URL and API key
api_url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key

# Specify the city
city = "Tashkent"

try:
    # Make a GET request to the API
    response = requests.get(api_url, params={"q": city, "appid": api_key, "units": "metric"})
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    weather_data = response.json()

    # Extract and print relevant information
    print(f"City: {weather_data['name']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except KeyError as key_err:
    print(f"Error parsing weather data: {key_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")











#3.
import json

# Specify the path to the JSON file
file_path = 'books.json'

# Load the JSON file
def load_books():
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": []}  # Return an empty structure if the file doesn't exist
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Starting with an empty list.")
        return {"books": []}

# Save the JSON file
def save_books(data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new book
def add_book():
    books_data = load_books()
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")
    books_data["books"].append({"title": title, "author": author, "year": year})
    save_books(books_data)
    print("Book added successfully!")

# Update an existing book
def update_book():
    books_data = load_books()
    title = input("Enter the title of the book to update: ")
    for book in books_data["books"]:
        if book["title"].lower() == title.lower():
            book["author"] = input(f"Enter new author (current: {book['author']}): ") or book["author"]
            book["year"] = input(f"Enter new year (current: {book['year']}): ") or book["year"]
            save_books(books_data)
            print("Book updated successfully!")
            return
    print("Book not found.")

# Delete a book
def delete_book():
    books_data = load_books()
    title = input("Enter the title of the book to delete: ")
    books_data["books"] = [book for book in books_data["books"] if book["title"].lower() != title.lower()]
    save_books(books_data)
    print("Book deleted successfully!")

# Main menu
def main():
    while True:
        print("\nBook Management System")
        print("1. Add a new book")
        print("2. Update an existing book")
        print("3. Delete a book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()









# 4. 
import requests
import random

# OMDB API URL and API key
api_url = "http://www.omdbapi.com/"
api_key = "your_api_key_here"  # Replace with your OMDB API key

def get_movies_by_genre(genre):
    try:
        # Make a GET request to the OMDB API to search for movies by genre
        response = requests.get(api_url, params={"apikey": api_key, "s": genre, "type": "movie"})
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        movies_data = response.json()

        # Check if movies are found
        if movies_data.get("Response") == "True":
            return movies_data.get("Search", [])
        else:
            print(f"No movies found for genre: {genre}")
            return []

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []

def recommend_movie():
    genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    movies = get_movies_by_genre(genre)

    if movies:
        # Pick a random movie from the list
        random_movie = random.choice(movies)
        print("\nRecommended Movie:")
        print(f"Title: {random_movie['Title']}")
        print(f"Year: {random_movie['Year']}")
        print(f"IMDB ID: {random_movie['imdbID']}")
    else:
        print("No recommendations available.")

if __name__ == "__main__":
    recommend_movie()
