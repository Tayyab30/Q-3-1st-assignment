from fastapi import FastAPI

app = FastAPI()

@app.get("/getdata")
def getData():
    print("Hello World")
    return {name: "Tayyab"}