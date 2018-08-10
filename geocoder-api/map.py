import requests,html

APP_ID=None
APP_CODE=None


def get_api(req,app_id=APP_ID,app_code=APP_CODE):
    safe_req = html.escape(req)
    #req_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+safe_req+'&key='+api_key
    req_url = 'https://geocoder.api.here.com/6.2/geocode.json?app_id='+app_id+'&app_code='+app_code+'&searchtext='+safe_req
    #print(req_url)
    r = requests.get( req_url ).json();
    #print( req_url )
    return(r)


def get_latlng(req,app_id=APP_ID,app_code=APP_CODE):
    # Uncomment to see the structure of the response
    #print(get_api(req, app_id, app_code) )
    
    position_stuff = get_api(req, app_id, app_code )['Response']['View'][0]['Result'][0]["Location"]['DisplayPosition']
    #print(position_stuff)
    return (position_stuff['Latitude'], position_stuff['Longitude'])
    
def main():
    #print("TEST")
    input("Enter Geocode: ")
    print( get_latlng('560062', 'EqXnTKgpbIoGuIYekNN6','sabuhvdO6Brn2SxBZejrrQ') )



if __name__=='__main__':
    main()
else:
    print('[geocode]: loaded')
