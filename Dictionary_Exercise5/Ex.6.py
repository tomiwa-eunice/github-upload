# Sets
# Ex.6.1
# Creation 1
movies = {"The Addams Family", "Ghostbusters", "Jurassic Park",
          "Pulp Fiction", "Home Alone", "The Matrix"}
print(movies)

# Creation 2
movies = set({"The Addams Family", "Ghostbusters", "Jurassic Park",
             "Pulp Fiction", "Home Alone", "The Matrix"})
print(movies)


# Ex.6.2
# Converting a list into a set
movies = ["The Addams Family", "Ghostbusters", "Jurassic Park",
          "Pulp Fiction", "Home Alone", "The Matrix"]
print(movies)

movies = set(movies)
print(movies)

# Methods in sets
# Adding elements into a set
movies.add('Star Wars')
print(movies)

# removing elements into a set
movies.remove('Ghostbusters')
print(movies)

# Size of the set
print(len(movies))

# Content in the movies set
print('Star Wars' in movies)
print('Ghostbusters' in movies)
# Alternative
for item in movies:
    print(item)

# Creating a shallow copy
movies.copy()
print(movies)

# Deleting the elements in a set
movies.clear()
print(movies)

# Ex.6.3
a = set('The Addams Family')
print(a)

# modified code
a = set({'The Addams Family'})
print(a)

# Ex.6.4
# sets and sets expressions
my_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

b = set(my_list)
print(b)

# Ex.6.5
# set operations
a = {1, 3, 6, 78, 35, 55}
b = {12, 24, 35, 24, 88, 120, 155}
print(a - b)
print(a & b)
print(a | b)
print(a ^ b)
print(a <= b)
print(a >= b)

# Ex.6.7
# set methods
print(a.difference(b))
print(a.intersection(b))
print(a.union(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))


# Ex.6.8
s = {"The Addams Family", "Ghostbusters", "Jurassic Park",
     "Pulp Fiction", "Home Alone", "The Matrix"}
for item in s:
    print(item)

print(s[1])
print(s[1:])
# TypeError: 'set' object does not support indexing


# Ex.6.9
# frozen set
s = set({"The Addams Family", "Ghostbusters", "Jurassic Park",
         "Pulp Fiction", "Home Alone", "The Matrix"})
print(s)
s.remove('The Matrix')
print(s)




