class Movie:
  def __init__(
				self, 
				id: int,
        title: str,
        overview: str,
        year: int,
        rating: float,
        category: str
      ):
			self.id = id
			self.title = title
			self.overview = overview
			self.year = year
			self.rating = rating
			self.category = category

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