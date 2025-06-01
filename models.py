"""This module will have validate 
"""

from pydantic import BaseModel,Field

class movie_validate(BaseModel):
    title:str=Field(...,min_length=1, max_length=255)
    description:str=Field(...,min_length=1, max_length=1000)
    language:str=Field(...,min_length=1, max_length=50)
    duration:float=Field(...,gt=0)
    rating:float=Field(...,gt=0,le=5)

class MovieRequest(movie_validate):
    """This represent the Request of movie
    in the api 
    """
'''class MovieRequest(MovieValidate):
    id: Optional[int] = None  # id optional in requests like this we can do by creating only or not use  id as it is optinal
    you can use in post request as it is overriding and rest field remains same 
'''

class MovieResponse(movie_validate):
    id: int

    model_config = {
        "from_attributes": True
    }

    # below is old version
    #class Config:
     #   orm_mode = True
#"When used in a get request with response_model=MovieResponse, only the fields defined in MovieResponse (like id)
#  will be included in the JSON response. Other fields like title, description, etc., will be excluded. The orm_mode =
#  True setting is what allows
#  FastAPI to convert the SQLAlchemy model object into a dictionary-like structure that Pydantic can use to generate JSON."
'''@router.get("/movies/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).get(movie_id)
    print(movie.secret_code)  # ✅ You can access it here in backend
    return movie  # ❌ But it won’t be returned in the API response'''
#All fields in the SQLAlchemy model (including sensitive ones like secret_code) will be returned — unless 
# you explicitly define a response_model to filter them. so that 's where pydamatic helps.
'''orm_mode
extra
allow_mutation
anystr_strip_whitespace
use_enum_values
validate_assignment
json_encoders
alias_generator
allow_population_by_field_name
arbitrary_types_allowed
copy_on_model_validation
keep_untouched
schema_extra
title
description
underscore_attrs_are_private
validate_all
min_anystr_length
max_anystr_length
env_prefix (for settings)'''


'''Pydantic features, such as:
1 Validation:
It checks that id is an integer and greater than 0.
It checks that title is a string and within the specified length.
2. Serialization:
You can convert the object to a dictionary or JSON easily:
movie = MovieValidate(id=1, title="Inception")
print(movie.dict())  # {'id': 1, 'title': 'Inception'}
3. Error Handling:
If invalid data is passed, it raises a ValidationError.
4. Documentation support (e.g., FastAPI):
FastAPI reads the model and auto-generates OpenAPI (Swagger) docs.'''