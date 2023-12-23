from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

BUILD_FOLDER = "../ui/build/"
INDEX_FILE = BUILD_FOLDER + "index.html"

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=BUILD_FOLDER + "static"), "static")


@app.get("/api/health")
async def health():
    return {"status": "healthy"}


@app.get("/api/health/{name}")
async def health_name(name: str):
    return {"status": "healthy", "name": name}


@app.get("/{rest_of_path:path}")
async def react_app():
    return FileResponse(INDEX_FILE)
