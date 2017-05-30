from operator import attrgetter
from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
]
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]

name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
