from math import cos, asin, sqrt, pi


def find_airport(airports, latitude, longitude):
    found = None
    nearest = 100000
    for a in airports:
        lat1 = float(latitude)
        lng1 = float(longitude)
        d = distance(lat1, lng1, float(a.latitude), float(a.longitude))
        if d < nearest:
            nearest = d
            found = a
    return (found, nearest)


def distance(
    lat1,
    lon1,
    lat2,
    lon2,
    ):

    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2
            * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))
