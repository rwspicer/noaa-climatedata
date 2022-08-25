"""
Stations Service
----------------
"""
from . import generic
from . import globals
import json


## Filters
filters = {
    'datasetid':        globals.default,
    'locationid':       globals.default,
    'datacategoryid':   globals.default,
    'datatypeid':       globals.default,
    'extent':           globals.default,
    # 'stationid':        globals.default
}

filters.update(globals.filters)

## Aliases
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
    
    response = generic.call('stations', **clean_args)

    return json.loads(response)
