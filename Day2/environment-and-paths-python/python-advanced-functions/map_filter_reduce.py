from collections import namedtuple

# Shape of the dataset is:
# name of the city, country abbreviation, population in M, coordinates
metro_data = [
    ("Tokyo", "JP", 9.273, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 18.98, (28.613889, 77.208889)),
    ("Mexico City", "MX", 8.855, (19.433333, -99.133333)),
    ("New York-Newark", "US", 8.623, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 12.18, (-23.547778, -46.635833)),
    ]

# Lambda functions
LatLong = namedtuple("LatLong", "lat long")
MetroPolis = namedtuple("Metropolis", "name cc pop coord")

metro_areas = [MetroPolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]

for area in metro_areas:
    print(area)

# Let's create a mapping lambda function to calculate the population of a given
# MetroPolis in numbers instead of Millions. That is to say we need to multiply
# each element with 10^6. We can use mapping to apply this lambda on
# each element of metro areas :)

calculate_millions = lambda metropolis: "Not implemented"

print(list(map(calculate_millions, metro_areas)))

# Let's create a filtering lambda function to filter only the cities that are located 
# in the south hemisphere. We can use filter to apply this lambda on each element of
# metro areas :)

south_hemisphere = lambda metropolis: "Not implemented"

print(list(filter(south_hemisphere, metro_areas)))
