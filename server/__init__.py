import sys
sys.path.append(".")
from fastapi import FastAPI, Form

app = FastAPI(docs_url="/")

from server.endpoints.calculator import router as router_calculator

app.include_router(router_calculator, prefix="/calc")


# to run the server execute this file
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, port=8080)
