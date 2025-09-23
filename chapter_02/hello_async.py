from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get("/hi")
async def greet():
    await asyncio.sleep(1)  # Simulate a delay
    return "Hello, Async World!"

if __name__ == "__main__":
    uvicorn.run("hello_async:app")