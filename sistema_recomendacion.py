from Rating import Rating 
from Movie import Movie


archivoEntradaRating = 'ratings.csv'
archivoEntradaMovies = 'movies.csv'


with open(archivoEntradaRating) as f1:
    ratingCSV = list (f1.readlines())

with open(archivoEntradaMovies,encoding="utf8") as f2:
    moviesCSV = list (f2.readlines())

ratings = []
movies = []

for ratingLine in ratingCSV:
    results = ratingLine.split(',')
    ratings.append(Rating(results[0],results[1],results[2],results[3]))

for moviesLine in moviesCSV:
    results = moviesLine.split(',')
    movies.append(Movie(results[0],results[1],results[2].rstrip("\n")))


userMovies = [
             {'title':'Toy Story',   'rating':8},
             {'title':'Seven',       'rating':5},
             {'title':'Taxi Driver', 'rating':9},
             {'title':'Rising Sun',  'rating':6},
             {'title':'Glory',       'rating':4}
             ]

print(userMovies[0])