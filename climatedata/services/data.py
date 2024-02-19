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


def call(*args, **kwargs):
    """calls service to get data

    Parameters
    ----------
    **kwargs:
        keyword arguments defined in climatedata.services.data.filters

    Returns
    -------
    response:
        format is defined by kwargs['format']

    """


    clean_args = globals.validate_args(kwargs, filters, aliases)

    if len(args) != 0:
        raise generic.InvalidAPICallError('data api cannot have generic query')
    
    response = generic.call('data', **clean_args)

    return json.loads(response)
