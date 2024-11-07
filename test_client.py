import requests

BASE_URL = 'http://localhost:8000/'

# Endpoint 1: Get all songs
def test_get_all_songs():
    print("Testing endpoint: Get all songs")
    response = requests.get(f"{BASE_URL}songs/")  
    if response.status_code == 200:
        print("Success:", response.json()) 
    else:
        print("Error:", response.status_code, response.text)

# Endpoint 2: Get song by title
def test_get_song_by_title(title):
    print(f"Testing endpoint: Get song by title '{title}'")
    response = requests.get(f"{BASE_URL}song/{title}/")
    if response.status_code == 200:
        print("Song details:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Endpoint 3: Rate a song 
def test_rate_song(title, rating):
    print(f"Testing endpoint: Rate song '{title}' with rating {rating}")
    response = requests.post(f"{BASE_URL}rate/{title}/", data={"star_rating": rating})
    if response.status_code == 200:
        print("Rating success:", response.json())
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    test_get_all_songs()
    test_get_song_by_title("All Night Long")  # Replace with an actual song title
    test_rate_song("All Night Long", 4.5)  # Replace with an actual song title and a rating
