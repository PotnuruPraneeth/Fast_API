from models import movie_validate,MovieResponse,MovieRequest
from schemas import Movie
from sqlalchemy.orm import Session
from database_conn import SessionLocal
from fastapi import APIRouter,Depends,HTTPException

router_movies = APIRouter()

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



@router_movies.post("/movies",response_model=MovieRequest) #here we have to pass the parameter of the paydamatic class which is sutable + database 
def creat_movie(Moviee:MovieRequest,db: Session = Depends(get_db))->MovieRequest: # parameters are paydamatic class, database
    new_movie = Movie(**Moviee.model_dump())  # passing all arguments to Movie class sqlalchemy orm . it like creating instances
    db.add(new_movie) # conneting to database
    db.commit()
    db.refresh(new_movie)
    return new_movie
