import requests
import pandas as pd

parks = pd.read_csv('public_parks_penang_island.csv')

# api-endpoint
URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"

#API key
api_key = myapikey

address_items = pd.DataFrame()

for latitude, longitude in zip(parks['NEW_LAT'], parks['NEW_LON']):
    
    # Defining a params dictionary for the parameters to be sent to the API 
    PARAMS = {
        'at': '{},{}'.format(latitude,longitude),
        'apikey': api_key
             }

    # Sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 

    # Extracting data in json format 
    data = r.json() 

    address_dict = {}

    address_dict['address'] = data['items'][0]['address']['label']
    address_dict['district_detected'] = data['items'][0]['address']['county']
    address_dict['city'] = data['items'][0]['address']['city']
    address_dict['postal_code'] = data['items'][0]['address']['postalCode']
    address_dict['lat'] = data['items'][0]['position']['lat']
    address_dict['lon'] = data['items'][0]['position']['lng']
    
    try:
        address_dict['lat_accessed'] = data['items'][0]['access'][0]['lat']
    except:
        address_dict['lat_accessed'] = "NA"
    
    try:
        address_dict['lon_accessed'] = data['items'][0]['access'][0]['lng']
    except:
        address_dict['lon_accessed'] = "NA"

    address_items = address_items.append(pd.DataFrame().from_dict(address_dict, orient='index').T)

# address_items

# reset index: initially was all zeroes, so that we can combine with the original parks df
address_items2 = address_items.reset_index()
address_items2.drop('index', axis=1, inplace=True)

# combine dfs
parks_combined = pd.concat([parks, address_items2], axis=1)
# parks_combined

# export data
parks_combined.to_csv('public_parks_penang_island_newinfo.csv', index=False)