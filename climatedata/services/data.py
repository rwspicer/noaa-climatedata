"""
Data Service
------------
"""
from . import generic
from . import globals
import json

# Filters
filters = {
    'datasetid':   globals.default,
    'datatypeid':   globals.default,
    'locationid':   globals.default,
    'stationid':    globals.default,
    'includemetadata': lambda a, oa: a in ['true', 'false']
}

filters.update(globals.filters)

#alaises
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
    
    response = generic.call('data', **clean_args)

    return json.loads(response)
