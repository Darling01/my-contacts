from fastapi import FastAPI

from Src.lib.managedb import ManageDb

app = FastAPI()
md = ManageDb()

@app.get("/")
def root():
    return {"messege": "hola"}


@app.get("/api/contacts")
def get_all_contacts():
    return md.read_contacts()