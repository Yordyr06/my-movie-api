from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

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
def add_movie(
  id: int = Body(...),
  title: str = Body(...),
  overview: str = Body(...),
  year: int = Body(...),
  rating: float = Body(...),
  category: str = Body(...)
):
  new_movie = Movie(
    id = id,
    title = title,
    overview = overview,
    year = year,
    rating = rating,
    category = category
  )
  movies.append(new_movie)
  return {"message": "Movie added successfully"}