from fastapi import FastAPI
from web import explorer
from web import creature

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)

"""
@app.get("/")
def top():
    return "tutaj góra"

@app.get("/echo/{thing}")
def echo(thing: str):
    return f"showing {thing}"
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
    