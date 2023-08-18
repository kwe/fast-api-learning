from typing import List

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

class Reference(BaseModel):
  source: str
  source_text: str
  filename: str
  page: str
class Response(BaseModel):
    answer: str
    time: str
    references: List[Reference]

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.post("/prompt")
def read_prompt(prompt: str) -> Response:
  references = [
    Reference(
      source="Wikipedia",
      source_text="The number of the French department of Maine-et-Loire is 49.",
      filename="wikipedia.txt",
      page="https://en.wikipedia.org/wiki/Maine-et-Loire"
    ),
    Reference(
      source="Wikipedia",
      source_text="The number of the French department of Maine-et-Loire is 49.",
      filename="wikipedia.txt",
      page="https://en.wikipedia.org/wiki/Maine-et-Loire"
    ),
  ]
  return Response(answer="49",
          time="27 seconds",
          references=references,
  )

@app.post("/upload")
async def upload_file(file: UploadFile):
  return {"filename": file.filename}

