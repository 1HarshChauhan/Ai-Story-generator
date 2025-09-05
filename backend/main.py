from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
    title="adventure time",
    description="this is me starting to do fastapi things",
    version="0.1",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    
)

app.get("/")
def Home():
    return {message:"Hello world"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app",host="localhost",port=8000,reload=True)
