# README

python interface to NOAA climate data online services. Namely services
described [here](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)

Some basic code and callback formatting is taken from my 
[USGS-Waterdata project](https://github.com/rwspicer/usgs-waterdata).
I did this to create a uniform style of interface.


## installation  
 
- Install packages from `requirements.txt`
- Run `python setup.py install`

## How to use

These services require that you get an API key from the 
[CDO token request page](https://www.ncdc.noaa.gov/cdo-web/token).

All services are called with the same format passing 
filters as keyword arguments to the service call functions. See each
services' documentation for valid filters. They return the response in the 
format specified. 

```
import climatedata

apikey = '' # add your api key

response = climatedata.services.data.call(
    token=apikey, 
    datasetid='GHCND', 
    stationid='GHCND:US1NCBC0005', 
    startdate='2010-01-01', enddate='2011-01-01',
    limit=366
)
```

`climatedata.formats` and `climate.utilities` also provide functions for 
collating, converting and saving responses to useful formats. 
These functions typically take the service function and keywords filters as 
some arguments. See the documentationin `climatedata.formats` and 
`climate.utilities`  for more info. For example to get all of the data for a
site.  

```
import climatedata

apikey = '' # add your api key

def my_callback(**kwargs):
    """custom call back to get all site data for all years between startdate 
    and enddate because data service has a max respnse of one years worth of 
    data
    """
    return climatedata.utilities.get_data_for_temporal_extent(
        climatedata.services.data.call, **kwargs
    )
    

data = climatedata.formats.as_DataFrame(
    my_callback, 
    token=apikey, 
    datasetid='GHCND',
    stationid='GHCND:US1NCBC0005',
    startdate='2017-08-23', enddate='2022-08-15'
)
```
