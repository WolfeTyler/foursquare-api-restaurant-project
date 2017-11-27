# Restaurant Finding API

This application utilizes the Google Maps API to geocode the cordinates of an address/city/country and then passes that information along with a food genre to the Foursquare API in order to recommend corresponding restaurants back to the user in the form of JSON data

## Getting Started

Download the project and to test locally simply run the view.py file which should initialize the application to your localhost:5000

### Prerequisites

* Python 3
* Flask
* Sqlalchemy
* Foursquare Developer API Keys
* Google Maps API Key

## Running the tests

User the tester.py file to run testing once you have the application running on a server. Read through the tester.py documentation to see what test scenarios are included in the coverage.

```
python tester.py
```

### New Restaurant POST Example

This POST example will find a restaurant in Bueonos Aires Argentina that specializes in Sushi and POST the record to your application database.

```
print "Test 1: Creating new Restaurants......"
url = address + '/restaurants?location=Buenos+Aires+Argentina&mealType=Sushi'
h = httplib2.Http()
resp, result = h.request(url,'POST')
if resp['status'] != '200':
  raise Exception('Received an unsuccessful status code of %s' % resp['status'])
print json.loads(result)
```

## Built With

* [Python Flask](http://flask.pocoo.org/) - The web framework used
* [Postman](https://www.getpostman.com/) - Used to test API calls (GET, POST, UPDATE)
* [Foursquare API](https://developer.foursquare.com/) - Setup a developer account to get the API keys for to use with this app
* [Google Maps API](https://developers.google.com/maps/documentation/geocoding/intro) - Setup an account and follow the Get a Key instructions

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
