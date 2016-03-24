# prism-test

- Code + test for ksum is in `ksum_test.py`.
- Code + test for salesman is in `salesman_test.py`.

Both files include tests, that can be run with py.test:
```
$ py.test
========================================================================== test session starts ===========================================================================
platform darwin -- Python 2.7.10, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/jules/Dropbox/code/python/prism, inifile: setup.cfg
collected 11 items 

ksum_test.py ..........
salesman_test.py .

======================================================================= 11 passed in 1.68 seconds ========================================================================
```

## salesman

```
$ python salesman_test.py -h
usage: python salesman_test.py -u <unit> [filename]
    with unit = miles or km
```

If no filename is provided the script will read from stdin, so both of these work:
```
python salesman_test.py cities.txt
python salesman_test.py < cities.txt
```

`unit` can be given with short or long option, default is miles:
```
python salesman_test.py --unit km cities.txt 
python salesman_test.py -u km cities.txt 
```

I used Google's geocoder api to get locations from addresses (it doens't seem to require a developer key right now). I didn't handle any error conditions (Google being down, API limit reached etc.) or edge cases related to the geocoder (wrong address etc.).

I used [Geopy](https://github.com/geopy/geopy) to avoid having to write a client, but then realised that [geolocation-python](https://pypi.python.org/pypi/geolocation-python/0.2.0) may have been a better choice since it includes different modes of transportation which would have been handy for the bonus question.

If I had more time I would switch client to support different transportation modes. If I had a bunch more time I would poke at Python3 with tulip/asyncio (I'm still mostly used to 2.7 :/) or grequests to do the geolocation queries in parallel.

## ksum

I only had time for the bruteforce solution - comlexity O(n ^ min(k, n-k)) (details in the solution file). Within the time I had I didn't find a solution with significantly better big-O complexity, although a number of heuristics can be used to reduce the average time.
