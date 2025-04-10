from fastapi import FastAPI
from pydantic import BaseModel
from src.router.router import user
from fastapi.middleware.cors import CORSMiddleware
from src.router.lectorPdf import lectorPdf
from src.lib.manageDb import ManageDb

class ContactModel(BaseModel):
    id: int
    name: str
    phone: str

app = FastAPI()
md = ManageDb()

origins = [
    "http://localhost:3000/Login/Index",
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# uvicorn main:app --reload

app.include_router(user)
app.include_router(lectorPdf)

@app.get("/")
def root():
    return {"message:" "Cantala"}
