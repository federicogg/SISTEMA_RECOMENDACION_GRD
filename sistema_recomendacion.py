from Rating import Rating 

archivoEntrada = 'ratings.csv'


with open(archivoEntrada) as f:
    ratings = list (f.readlines())



for ratingLine in ratings:
    results = ratingLine.split(',')
    print (results[0])
    
    




