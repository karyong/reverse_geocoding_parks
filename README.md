## Reverse geocoding
Reverse geocoding is to get the addresses from latitudes and longitudes.

The aim of this project is to identify the city where the parks located.
I used the location API from the [HERE developer](https://developer.here.com/), with main reference to [this tutorial](https://developer.here.com/blog/reverse-geocoding-a-location-using-python).


## Dataset
- Input file: List of public parks in Penang island, along with their type, size, district, latitude and longitude (public_parks_penang_island.csv)
- Output file: Concatenated input file with the results obtained: district obtained from HERE, address, city, lat, lon, and lat and lon accessed (not sure what differences between these two) (public_parks_penang_island_newinfo.csv).



