metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
]
from operator import itemgetter

# Sort tuple by second parameter

# same, as key=lambda _list: _list[1]
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

