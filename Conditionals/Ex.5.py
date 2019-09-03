#  Ex.5.1
# indexing a list
movies = ['The Adams Family', 'Ghostbusters', 'Jurassic Park',
          'Pulp Fiction', 'Home Alone', 'The Matrix']
print(movies[0])
print(movies[4])
print(movies[5])
print(movies[-1])
print(movies[-6])
print(movies[-10])
print(movies[9])

#Ex.5.2
# slicing
print(movies[0:2])
print(movies[3:5])
print(movies[:])
print(movies[3:])
print(movies[:5])
print(movies[-1:])
print(movies[-3:])
print(movies[-4:-2])
print(movies[-4:5])
print(movies[-4:2:-1])
print(movies[-4:9])

# Ex.5.3
# steps with slicing
print(movies[0::2])
print(movies[::3])
print(movies[0:5:1])
print(movies[0:5:2])
print(movies[0:5:])
print(movies[-4::3])
print(movies[-5:-1:2])
print(movies[-3:-9:1])
print(movies[::1])
print(movies[::-1])
print(movies[::2])
print(movies[::-2])

# Ex.5.4
# elements present in a list
print('Star Wars' in movies)
print('Jurassic' in movies)
print('Jurassic Park' in movies)
print('jurassic park' in movies)
print('Ghostbusters' in movies)

# Ex.5.5
# Changing elements in a list
movies[2] = 'Star Wars'
print(movies)

movies[-3:] = 'Gladiator', 'Casablanca', 'The Godfather'
print(movies)

#Ex.5.6
# List_methods
# append
movies.append('The Shawshank Redemption')
print(movies)
# extend
movies.extend(['Forrest Gump', 'The Dark Knight', 'Fight Club',
               'Saving Private Ryan'])
print(movies)
# insert
movies.insert(0, 'Back to the Future')
print(movies)
# remove
movies.remove('Forrest Gump')
print(movies)

# Ex.5.7
# deleting
del movies[0]
print(movies)
del movies[0:2]
print(movies)
del movies[:]
print(movies)
del movies
print(movies)


# Ex.5.8
tv_shows = [["Sherlock Holmes", "Drama", 2009],
            ["Planet Earth", "Documentary", 2006],
            ["Cosmos", "Documentary", 2014],
            ["Dr. Who", "Science fiction", 2005],
            ["Stranger Things ", " Science fiction", 2016],
            ["Game of Thrones", "Fantasy", 2011]]
print(tv_shows[1])
print(tv_shows[1:3])
print(tv_shows[2][0])
print(tv_shows[2][1])
print(tv_shows[2][2])
print(tv_shows[2][1:])
print(tv_shows[2][:])

# Ex.5.9
# Tuples
movies = ("The Addams Family", "Ghostbusters", "Jurassic Park",
          "Pulp Fiction", "Home Alone", "The Matrix")
print(movies[2])
movies[2]='Star Wars'


# Iterating over  element
# Ex.5.10
i= 1
while i <= 10:
    print(i)
    i = i + 1
print("Finished")

i = 0
while i < 9:
    i = i + 1
    if i==5 or i ==7:
        continue                # Back to the while statement
    else:
        print(i)
print(i+1)

# Ex. 5.11
# printing using while loops
movies = ['The Adams Family', 'Ghostbusters', 'Jurassic Park',
          'Pulp Fiction', 'Home Alone', 'The Matrix']
i = 0
while i < len(movies):
    print(movies)
    i = i + 1
print('Finished')
