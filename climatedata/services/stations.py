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
    'stationid':        globals.default
}

filters.update(globals.filters)

## Aliases
aliases = {
}

def call(*args, **kwargs):
    """calls service to get stations

    Parameters
    ----------
    **kwargs:
        keyword arguments defined in climatedata.services.stations.filters

    Returns
    -------
    response:
        format is defined by kwargs['format']

    """
    clean_args = globals.validate_args(kwargs, filters, aliases)
    
    
    if len(args) == 1:
        clean_args['specifically'] = args[0]
    elif len(args) > 1:
        raise generic.InvalidAPICallError(
            'api cannot have multiple generic queries'
    )

    response = generic.call('stations', **clean_args)
    return json.loads(response)
