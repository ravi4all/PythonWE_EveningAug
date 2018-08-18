movies = [
    {"category":"action", "name":"Terminator", "type":"hollywood","year":1991},
    {"category":"comedy", "name":"Dhamaal", "type":"bollywood","year":2008},
    {"category":"drama", "name":"Sanju", "type":"bollywood","year":2018},
    {"category":"comedy", "name":"Hera Pheri", "type":"bollywood","year":2003},
    {"category":"action", "name":"Baahubali", "type":"bollywood","year":2017},
    {"category":"drama", "name":"Lucy", "type":"hollywood","year":2014},
    {"category":"comedy", "name":"Mask", "type":"hollywood","year":1998},
    {"category":"action", "name":"Avengers", "type":"hollywood","year":2012},
    {"category":"action", "name":"Bang Bang", "type":"bollywood","year":2015},
    {"category":"action", "name":"Terminator", "type":"hollywood","year":1991},
    {"category":"comedy", "name":"Dhamaal", "type":"bollywood","year":2008},
    {"category":"drama", "name":"Sanju", "type":"bollywood","year":2018},
    {"category":"comedy", "name":"Hera Pheri", "type":"bollywood","year":2003},
    {"category":"action", "name":"Baahubali", "type":"bollywood","year":2017},
    {"category":"drama", "name":"Lucy", "type":"hollywood","year":2014},
    {"category":"comedy", "name":"Mask", "type":"hollywood","year":1998},
    {"category":"action", "name":"Avengers", "type":"hollywood","year":2012},
    {"category":"action", "name":"Bang Bang", "type":"bollywood","year":2015},
]

print("""
Category | Name | Type | Year
""")

search = input("Search movie : ")

for i in range(len(movies)):
    if movies[i]['category'] == search or movies[i]['name'] == search or movies[i]['type'] == search or movies[i]['year'] == search:
        print(movies[i])