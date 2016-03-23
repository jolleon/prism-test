import pytest
from geopy.geocoders import GoogleV3
from geopy.distance import vincenty

g = GoogleV3()

def distance(l1, l2):
	d = vincenty((l1.latitude, l1.longitude), (l2.latitude, l2.longitude))
	return d

def distances(cities):
	positions = [g.geocode(c) for c in cities]

	result = []
	for i in range(len(cities) - 1):
		d = distance(positions[i], positions[i+1])
		result.append(d.miles)

	return result



def test_distances():
	cities = ["Paris, France", "New York City, USA", "Nuuk, Greenland"]
	expected = [3631, 1852]

	d = distances(cities)
	assert len(d) == len(expected) == len(cities) - 1

	margin = 10 # all geocoders are not equal
	for e, x in zip(expected, d):
		assert e - margin < x < e + margin


