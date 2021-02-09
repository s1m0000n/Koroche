from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import text_api


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(text_api.router)
templates = Jinja2Templates(directory="templates")


@app.get('/')
async def main(request: Request, response_model=HTMLResponse):
    """
    SPA Web-Page View
    """
    return templates.TemplateResponse("main.html", {'request': request})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9001)
