from fastapi import FastAPI
from database_conn import Base, engine
from movies import router_movies

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Movie Service",
    summary="Movie Service",
    description="Movie Service",
    version="1.0.0"
)

router=router_movies, prefix="/v1")
