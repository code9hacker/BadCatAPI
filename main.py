#####
# This main file acts as a controller for APIs
#####

from fastapi import FastAPI

global app
app = FastAPI()


@app.get("/")
def getIndex():
    return "FastAPI server is up"


@app.get("/printName")
def printName(name: str):
    return 'Hello,' + name