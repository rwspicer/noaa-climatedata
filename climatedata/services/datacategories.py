"""
Data Categories Service
-----------------------
"""
from . import generic
from . import globals
import json

# filters 
filters = {
    'datasetid':   globals.default,
    'locationid':   globals.default,
    'stationid':    globals.default,
}

filters.update(globals.filters)

# aliases 
aliases = {
}

def call(**kwargs):
    """calls service to get daily waterdata

    Parameters
    ----------
    **kwargs:
        keyword arguments defined in waterdata.services.daily_data.filters

    Returns
    -------
    response:
        format is defined by kwargs['format']

    """
    clean_args = globals.validate_args(kwargs, filters, aliases)
    
    response = generic.call('datacategories', **clean_args)

    return json.loads(response)
