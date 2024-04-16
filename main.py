from fastapi import FastAPI


app = FastAPI(
  title = "My First FastAPI",
  version = "0.0.1",
)

@app.get("/", tags=["Home"])
def message():
  return "Hello World!"
