from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from data import ( movies, Movie )

app = FastAPI(
  title = "My First FastAPI",
  version = "0.0.1",
)

@app.get("/", tags = ["Home"])
def message():
  return HTMLResponse('''
    <html>
      <head>
        <title>My First FastAPI</title>
      </head>
      <body>
        <h1>Hello World</h1>
      </body>
    </html>
  ''')


@app.get("/movies", tags = ['Movies'])
def get_movies():
  return movies


@app.get("/movies/{movie_id}", tags = ['Movies'])
def get_movie(movie_id: int):
  for movie in movies:
    if movie["id"] == movie_id:
      return movie
  return {"error": "Movie not found"}


@app.get('/movies/', tags = ['Movies'])
def get_movies_by_category(category: str, year: int):
  for movie in movies:
    if movie["category"] == category or movie["year"] == year:
      return movie
  return {"error": "Movie not found"}


@app.post('/movies', tags = ['Movies'])
def add_movie(new_movie: Movie):
  movies.append(new_movie)
  return {"message": "Movie added successfully"}


@app.put('/movies/{movie_id}', tags=['Movies'])
def update_movie(movie_id: int, movie: Movie):
  for item in movies:
    if item["id"] == movie_id:
      item["id"] = id
      item["title"] = movie.title
      item["overview"] = movie.overview
      item["year"] = movie.year
      item["rating"] = movie.rating
      item["category"] = movie.category
      return {"message": "Movie updated successfully"}
  return {"error": "Movie not found"}


@app.delete('/movies/{movie_id}', tags=['Movies'])
def delete_movie(movie_id: int):
  for movie in movies:
    if movie["id"] == movie_id:
      movies.remove(movie)
      return {"message": "Movie deleted successfully"}
  return {"error": "Movie not found"}