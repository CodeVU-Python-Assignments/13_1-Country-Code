import urllib.request
import urllib.parse
import urllib.error
import json

def print_country_code_from_geocoding() -> None:
    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
        
        
    print('implement me')


# The original examples are a loop, write this to run once
if __name__ == "__main__":
    print_country_code_from_geocoding()
