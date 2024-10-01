from fastapi import FastAPI, Request, HTTPException,Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from pathlib import Path
import uvicorn

app=FastAPI()
user={
    1:{
        "username":"Jatin", 
        "password":"Jatin@123"
    }
}

@app.get("/")
def Home():
    html_path = Path("New_Home.html")
    html_content = html_path.read_text()
    return HTMLResponse(content=html_content)

@app.get("/landing")
def landing_page():
      html_path=Path("Chat.html")
      html_content=html_path.read_text()
      return HTMLResponse(content=html_content)

@app.get("/login")
def login(username: str = None, password: str = None):
    if username and password:
        for users in user.values():
            if users["username"] == username and users["password"] == password:
                return RedirectResponse(f"/landing?username={username}", status_code=302)
        return RedirectResponse(url="/login?error=true", status_code=302)

    html_path = Path("Login.html")
    html_content = html_path.read_text()
    return HTMLResponse(content=html_content)

@app.get("/register")
def get_register():
    html_path = Path("Register.html")
    html_content = html_path.read_text()
    return HTMLResponse(content=html_content)


@app.post("/register")
def register_user(username: str = Form(...), password: str = Form(...)):
    new_user_id = len(user) + 1
    user[new_user_id] = {"username": username, "password": password}
    return RedirectResponse(url="/login", status_code=302)

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)