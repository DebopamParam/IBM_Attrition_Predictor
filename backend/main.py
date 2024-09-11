from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "I Love u ghoru"}

@app.get("/items/")
def read_item():
    return {"item": "Meaw"}
