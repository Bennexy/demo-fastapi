from logging import debug
from fastapi import FastAPI, Form



app = FastAPI(docs_url="/")


@app.post("/add")
async def add(value_1: int = Form(...), value_2: int = Form(...)):
    return value_1 + value_2


@app.post("/multiply")
async def multiply(value_1: int = Form(...), value_2: int = Form(...)):
    return value_1 * value_2










# to run the server execute this file
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, port=8080)
