import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/app")
sys.path.append("/app/backend")

from fastapi import FastAPI, status
from starlette.responses import RedirectResponse
from backend.routes.predict import router as predict_router
from backend.routes.monitor import router as monitor_router

app = FastAPI(title="Pneumonia Detection API", version="1.0.0")

app.include_router(predict_router, prefix="/api")
app.include_router(monitor_router, prefix="/monitor")

@app.get("/")
def main():
    return RedirectResponse(url="/docs")

@app.get("/healthcheck", tags=["healthcheck"], status_code=status.HTTP_200_OK)
def get_api_status() -> str:
    return "ok"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000)
