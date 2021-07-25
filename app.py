from fastapi import FastAPI
from Routers.posts import router as postsRouter


app =FastAPI(
     title="My first FastAPI",
     version="1.0.0",
    openapi_tags = [{
        "name":"Posts"
    }]
)

app.include_router(postsRouter)
