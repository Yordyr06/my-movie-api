from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
  title = "My First FastAPI",
  version = "0.0.1",
)

movies = [
  {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

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