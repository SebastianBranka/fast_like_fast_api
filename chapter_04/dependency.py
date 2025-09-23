from fastapi import FastAPI, Depends, Query

app = FastAPI()

def user_dep(name: str = Query(default=None), password: str = Query(default=None)):
    return {"name": name, "valid": True}

@app.get("/user")
def get_user(user:dict = Depends(user_dep)) -> dict:
    return user

@app.get("/check_user", dependencies=[Depends(user_dep)])
def ceck_user() -> bool:
    return True