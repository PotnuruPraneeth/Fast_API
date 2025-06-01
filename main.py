from fastapi import FastAPI
from database_conn import Base, engine
from movies import router_movies

Base.metadata.create_all(bind=engine)
'''SQLAlchemy:
Looks at all classes that inherited from Base.
Reads the __tablename__, columns, types, etc.
Sends CREATE TABLE SQL statements to the DB.'''

'''| Concept                   | Explanation                                    |
| ------------------------- | ---------------------------------------------- |
| `Base` knows subclasses   | ✅ Yes, **after they are defined/imported**     |
| Happens automatically?    | ✅ Yes, **but only when you run the code**      |
| Without running the code? | ❌ No — Python must run to register the classes |
'''
app = FastAPI(
    title="Movie Service",
    summary="Movie Service",
    description="Movie Service",
    version="1.0.0"
)

#✅ app.include_router(router=router, prefix="/v1") — What it does:
#This tells the main FastAPI app (app) to include all the routes from the router,
# and add the prefix /v1 in front of them.
'''GET /v1/hello
→ {"message": "Hello"} #message is the function of router as i have taken from chatgpt.
'''
app.include_router(router=router_movies, prefix="/v1")
