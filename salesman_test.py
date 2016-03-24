import pytest
from geopy.geocoders import GoogleV3
from geopy.distance import vincenty
import fileinput
import sys, getopt

g = GoogleV3()

MILES = "miles"
KM = "km"

def distance(l1, l2):
	return vincenty((l1.latitude, l1.longitude), (l2.latitude, l2.longitude))

def distances(cities, unit=MILES):
	positions = [g.geocode(c) for c in cities]

	result = []
	for i in range(len(cities) - 1):
		d = distance(positions[i], positions[i+1])
		if unit == MILES:
			result.append(d.miles)
		else:
			result.append(d.kilometers)

	return result



def test_distances():
	cities = ["Paris, France", "New York City, USA", "Nuuk, Greenland"]
	expected = [3631, 1852]

	d = distances(cities)
	assert len(d) == len(expected) == len(cities) - 1

	margin = 10 # all geocoders are not equal
	for e, x in zip(expected, d):
		assert e - margin < x < e + margin



def print_help():
	print("usage: {} -u <unit> [filename]".format(sys.argv[0]))
	print("    with unit = {} or {}".format(MILES, KM))


if __name__ == "__main__":
	unit=MILES

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hu:", ["unit="])
	except getopt.GetoptError:
		print_help()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print_help()
			sys.exit()
		elif opt in ("-u", "--unit"):
			if arg not in (MILES, KM):
				print("Invalid unit: {}".format(arg))
				print_help()
				sys.exit(2)
			unit = arg

	cities = [line[:-1] for line in fileinput.input(args)]
	d = distances(cities, unit)
	print("Success! Your vacation itinerary is:\n")
	for i in range(len(cities) - 1):
		print("    {0} -> {1}: {2:.2f} {3}".format(cities[i], cities[i+1], d[i], unit))
	print("\nTotal distance covered in your trip: {0:.2f} {1}".format(sum(d), unit))
