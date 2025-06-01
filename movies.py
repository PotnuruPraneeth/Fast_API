from models import movie_validate,MovieResponse,MovieRequest
from schemas import Movie
from sqlalchemy.orm import Session
from database_conn import SessionLocal
from fastapi import APIRouter,Depends,HTTPException

router_movies = APIRouter()
'''✅ router = APIRouter() — What it means:
This line creates a new router object using FastAPI's APIRouter class.
A router is like a mini FastAPI app that helps
 you organize your routes (endpoints) more cleanly and modularly.
'''
''' Why use APIRouter?
Helps organize your code into modules (e.g., user, auth, movies routes separately).
Makes your project scalable and clean.
Each module can have its own router and then be added to the main app.
'''
def get_db():
    db=SessionLocal() #Create a new SQLAlchemy session (database connection)
    try:#try block beacuse if any error any thing happes then we have to close the database
        yield db # Yield the session to the caller (FastAPI)
                # Pause here and return `db` to the caller ('all_movies`)
                #So FastAPI pauses at yield and injects the db session
                # object(gointo)  the all_movies function parameter.
                #yield pauses the function and gives control to FastAPI.
    finally:
        db.close()# Close the session when done
#If you didn’t use try...finally, and something unexpected happened (error, timeout, etc.),
#  the session might stay open (not closed), leading to Memory leaks,Too many open DB connections,
# Unpredictable behavior in production so after that we need to close.
'''🧠 Why yield Instead of return?
If you used return db, FastAPI would have no way to run cleanup code afterward. That’s why:
✅ yield = lets FastAPI resume and clean up
❌ return = no way to run cleanup logic'''
@router_movies.get("/movies")
def all_movies(db: Session = Depends(get_db)): #session is typehinting,so it validate it's a type 
                                              #Session is a class from SQLAlchemy that represents a database session 
                                              # that means SessionLocal= sessionmaker() is session instance
    #db: Session = Depends(get_db) This tells FastAPI: "Before calling list_movies,
    #  get the db parameter by running get_db().
    # Dependency injection: Easy to reuse get_db() in multiple routes.
    return db.query(Movie).all()

@router_movies.get("/movies/{movie_id}",response_model=MovieResponse) #just for validating with pydamatic model.
def movie_id(movie_id:int,db: Session = Depends(get_db))->MovieResponse:
    movie_idd = (db.query(Movie).
             filter(Movie.id == movie_id).first())  #( ) if you write the code in multiple lines thst's it
    if movie_idd == None:
        raise  HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    return movie_idd
'''| Part                            | Meaning                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `db`                            | This is the database session object (from `Session = Depends(get_db)`).                                   |
| `db.query(Movie)`               | This creates a SQL SELECT query on the `Movie` table.                                                     |
| `.filter(Movie.id == movie_id)` | This adds a WHERE condition to select only the row where the ID matches.                                  |
| `.first()`                      | This executes the query and returns the **first row** that matches the condition, or `None` if not found. |
| `movie_idd = ...`               | This assigns the result (a `Movie` instance or `None`) to the variable `movie_idd`.                       |
it's like this (SELECT * FROM movies WHERE id = <movie_id> LIMIT 1);
in my sql'''


'''| Method     | Returns              | When to use                                                       |
| ---------- | -------------------- | ----------------------------------------------------------------- |
| `.first()` | One object or `None` | If you expect **0 or 1** row.                                     |
| `.all()`   | List of all results  | If you expect **many rows**.                                      |
| `.one()`   | One object           | If you’re sure **exactly one** row exists (else it raises error)..
one() expects exactly one result from the query.
 If that condition is not met, it raises an exception |
'''
@router_movies.post("/movies",response_model=MovieRequest) #here we have to pass the parameter of the paydamatic class which is sutable + database 
def creat_movie(Moviee:MovieRequest,db: Session = Depends(get_db))->MovieRequest: # parameters are paydamatic class, database
    new_movie = Movie(**Moviee.model_dump())  # passing all arguments to Movie class sqlalchemy orm . it like creating instances
    db.add(new_movie) # conneting to database
    db.commit()
    db.refresh(new_movie)
    return new_movie
'''What is happening here?
1. Moviee.model_dump()
This calls a Pydantic model's method model_dump() which returns all the fields of Moviee as a dictionary.
Moviee.title = "Inception"
Moviee.rating = 4.8
Moviee.model_dump() 
# returns {'title': 'Inception', 'rating': 4.8}

2. ** (double asterisk) operator
This is called dictionary unpacking in Python. 
It takes the dictionary returned by model_dump() and passes its keys and 
values as named arguments to the Movie constructor.

3.Movie(...)
This usually refers to a SQLAlchemy ORM model class representing a movie table row.
 By passing these arguments, you're creating a new Movie instance populated 
 with the data from the Pydantic model.

4.How does model_dump() return a dictionary from a Pydantic model?
Pydantic models aren't dictionaries, but they have methods to convert themselves into dictionaries.

In Pydantic v2, the method to get a dictionary representation is .model_dump().
In Pydantic v1, the equivalent method was .dict().
like this **Moviee.model_dump()--> {
  "title": "Inception",
  "rating": 4.8,
  "description": "A mind-bending thriller",
  "language": "English",
  "duration": 2.5
} 
and then
new_movie = Movie(
    title="Inception",
    rating=4.8,
    description="A mind-bending thriller",
    language="English",
    duration=2.5
)
just for infomation **kwargs means extra paramets it can accepts 
'''