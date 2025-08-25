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
