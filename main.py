from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import List
from jwt_manager import create_token, validate_token


from data import ( movies, Movie )

app = FastAPI(
  title = "My First FastAPI",
  version = "0.0.1",
)


class JWTBearer(HTTPBearer):
  async def __call__(self, request: Request):
    auth = await super().__call__(request)
    data = validate_token(auth.credentials)
    if data['username'] != 'admin':
      raise HTTPException(status_code = 401, detail = "Unauthorized")

class User(BaseModel):
  username: str
  password: str


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


@app.get(
    "/movies", 
    tags = ['Movies'], 
    response_model = List[Movie], 
    status_code = 200,
  )
def get_movies() -> List[Movie]: 
  return JSONResponse(status_code = 200, content = movies)


@app.get(
    "/movies/{movie_id}",
    tags = ['Movies'], 
    response_model = Movie, 
    status_code = 200
  )
def get_movie(movie_id: int = Path(ge = 1)) -> Movie:
  for movie in movies:
    if movie["id"] == movie_id:
      return JSONResponse(status_code = 200, content = movies)
  return JSONResponse(status_code = 404, content = {"message": "Movie added successfully"})


@app.get(
    '/movies/', 
    tags = ['Movies'], 
    response_model = List[Movie], 
    status_code = 200
  )
def get_movies_by_category(category: str = Query(min_length = 5, max_length = 10)) -> List[Movie]:
    data = [ item for item in movies if item["category"] == category ]
    return JSONResponse(status_code = 200, content = data)


@app.post(
    '/login',
    tags = ['Auth'],
  )
def login(user: User):
  if user.username == "admin" and user.password == "admin":
    token = create_token(data = {"username": user.username})
    return JSONResponse(status_code = 200, content = {"token": token})
  return JSONResponse(status_code = 401, content = {"error": "Invalid credentials"})


@app.post(
    '/movies', 
    tags = ['Movies'], 
    response_model = dict,
    status_code = 201
  )
def add_movie(new_movie: Movie) -> dict:
  movies.append(new_movie)
  return JSONResponse(status_code = 201, content = {"message": "Movie added successfully"})


@app.put(
    '/movies/{movie_id}', 
    tags = ['Movies'], 
    response_model = dict,
    status_code = 200
  )
def update_movie(movie_id: int, movie: Movie) -> dict:
  for item in movies:
    if item["id"] == movie_id:
      item["id"] = id
      item["title"] = movie.title
      item["overview"] = movie.overview
      item["year"] = movie.year
      item["rating"] = movie.rating
      item["category"] = movie.category
      return JSONResponse(status_code = 200, content = {"message": "Movie added successfully"})
  return JSONResponse(status_code = 404, content = {"error": "Movie movie not found"})


@app.delete(
    '/movies/{movie_id}',
    dependencies = [Depends(JWTBearer())],
    tags = ['Movies'], 
    response_model = dict,
    status_code = 200
  )
def delete_movie(movie_id: int) -> dict:
  for movie in movies:
    if movie["id"] == movie_id:
      movies.remove(movie)
      return JSONResponse(status_code = 200, content = {"message": "Movie deleted successfully"})
  return JSONResponse(status_code = 404, content = {"error": "Movie movie not found"})