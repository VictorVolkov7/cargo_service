from geopy import distance


def distance_between(first_coord: tuple, second_coord: tuple) -> float:
    """
    Calculate the distance between two points in miles
    by using web services geopy.distance.
    :param first_coord: coordinates of the first point.
    :param second_coord: coordinates of the second points.
    :return: distance in miles.
    """
    first_point: tuple = first_coord
    second_point: tuple = second_coord
    distance_miles = distance.distance(first_point, second_point).miles
    return round(distance_miles, 2)
