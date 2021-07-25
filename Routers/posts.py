from fastapi import APIRouter,Response
from Config.db import conn
from Models.posts import posts
from Schemas.posts import post as Post
from starlette.status import HTTP_204_NO_CONTENT

router = APIRouter()

@router.get('/api')
def root():
    return {"api":"/api"}

@router.get('/api/posts',tags=["Posts"])
def getPosts():
    return conn.execute(posts.select()).fetchall()

@router.post('/api/post',tags=["Posts"])
def addPost(post: Post):
    result = conn.execute(posts.insert().values({"post":post.post,"user":post.user}))
    return conn.execute(posts.select().where(posts.c.id == result.lastrowid)).first()

@router.delete('/api/post/{id}',tags=["Posts"])
def removePost(id:str):
    conn.execute(posts.delete().where(posts.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@router.put('/api/post/{id}',tags=["Posts"])
def updatePost(id:str,post:Post):
    conn.execute(posts.update().values(user = post.user,post=post.post).where(posts.c.id == id))
    return conn.execute(posts.select().where(posts.c.id == id)).first()