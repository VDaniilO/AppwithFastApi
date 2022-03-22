import uvicorn
from fastapi import FastAPI

from endpoints import users
from db.base import database

app = FastAPI(title = "Match test")
app.include_router(users.router, prefix = "/users", tags = ["users"] )


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



if __name__ ==  "__main__":
    uvicorn.run("main:app", port = 8000, host = "0.0.0.0", reload = True)
