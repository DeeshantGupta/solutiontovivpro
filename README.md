# solutiontovivpro

Problem 1.1:
Write a working program that takes this JSON file as input and normalizes it to
generate a table as below. You can keep this normalized data in memory or in
database or write to a file.

python prob1.py

will save the output in a csv file output.csv

Problem 1.2:
Write a backend REST APIs to serve normalized data generated in step 1.1. We believe
APIs for enabling following two use cases are MUST HAVE in order to make it practically
useful backend project.
1.2.1 [MUST HAVE] Front end should be able to request ALL the items in a normalized
data set.
Bonus point if you can implement pagination in API.
1.2.2 [MUST HAVE] Given a title as input, return all the attributes of that song
1.2.3 [ NICE TO HAVE] User should be able to rate a song using star rating ( 5 start being
highest). Please be mindful of the fact that this requires normalized data to have one
more column say star rating.
1.2.4 [BONUS] Write Unit tests

Features
List all songs: Retrieves all songs from the database with pagination support.
Get song details by title: Retrieve all attributes of a song by providing its title.
Rate a song: Users can rate a song on a scale of 0 to 5 stars.
Endpoints

GET /songs/ - Fetches all songs with pagination (10 per page).
GET /song/<title>/ - Fetches the details of a song by its title.
POST /rate/<title>/ - Allows users to rate a song between 0 to 5 stars.

Example Requests
Get all songs (paginated)
bash
curl -X GET http://localhost:8000/songs/

Get song by title
bash
curl -X GET http://localhost:8000/song/All Night Long/

Rate a song
bash
curl --location 'http://localhost:8000/rate/All Night Long/' \
--header 'Content-Type: application/json' \
--data '{"star_rating": 4}'

Installation
Prerequisites
Make sure you have the following installed:

Python 3.x
Django
Django Rest Framework

Clone the repository

bash
git clone https://github.com/yourusername/song-api.git

cd song-api

Set up a virtual environment

bash
python -m venv env
source env/bin/activate # For Windows use: env\Scripts\activate

Install dependencies
bash
pip install -r requirements.txt

Apply database migrations
bash
python manage.py migrate

Run the development server
bash
python manage.py runserver

The API will be available at http://localhost:8000/.

Testing the API
To test the API, you can use tools like curl, Postman, or any HTTP client to send requests to the endpoints mentioned above or you can use the script test_client.py
