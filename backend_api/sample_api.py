from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=9506,proxy_headers=True)