"""
Locations Service
-----------------
"""
from . import generic
from . import globals
import json

# filters
filters = {
    'datasetid':            globals.default,
    'locationcategoryid':   globals.default,
    'datacategoryid':       globals.default,
}

filters.update(globals.filters)

# aliases
aliases = {
}

def call(*args, **kwargs):
    """calls service to get locations

    Parameters
    ----------
    **kwargs:
        keyword arguments defined in climatedata.services.locationcategories.filters

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
    
    
    response = generic.call('locations', **clean_args)

    return json.loads(response)
