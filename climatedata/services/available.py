"""
Available Services
------------------

Information on available web_services

"""
import os

### URLS
CDO_URL = 'https://www.ncei.noaa.gov/cdo-web/api/v2/'


class AvailableServiceError(Exception):
    pass

### available web_services from https://www.ncdc.noaa.gov/cdo-web/webservices/v2
services = [
    'datasets', 
    'datacategories',
    'datatypes',
    'locationcategories',
    'locations',
    'stations',
    'data',
    
]

# available web_services name maps
names = {
    
}

descriptions = {
    'datasets': 'A dataset is the primary grouping for data at NCDC.',
    'datacategories': 'A data category is a general type of data used to group similar data types.',
    'datatypes': 'A data type is a specific type of data that is often unique to a dataset.',
    'locationcategories': 'A location category is a grouping of similar locations.',
    'locations': 'A location is a geopolitical entity.',
    'stations': 'A station is a any weather observing platform where data is recorded.',
    'data': 'A datum is an observed value along with any ancillary attributes at a specific place and time.',

}

def get_url(service):
    """ Gets the url for the service

    Parameters
    ----------
    service: str
        a service defined in waterdata.services.available.services

    returns
    -------
    a url
    """
    if not service in services:
        raise AvailableServiceError (
            "service %s is not a valid web service" % service
        )
    
    url = os.path.join(CDO_URL, service)
    
    return url

