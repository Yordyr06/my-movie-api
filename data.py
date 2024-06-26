from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel): 
	id: int = Field(ge = 1)
	title: str = Field(min_length = 5, max_length = 15)
	overview: Optional[str] = None
	year: int = Field(ge = 2000)
	rating: Optional[float] = None
	category: str = Field(min_length = 5, max_length = 10)

	class Config: 
		schema_extra = {
			"example": {
				"id": 0,
				"title": "My Movie",
				"overview": "A nice and exciting movie",
				"year": 2000,
				"rating": 1.0,
				"category": "Drama"
			}
		}

movies = [
  {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},

  {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]