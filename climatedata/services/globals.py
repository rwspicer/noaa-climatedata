"""
Globals
-------
"""
from datetime import date

# Default filter function
default = lambda a, oa: True

def valid_date_str(date_str): # need to have a datetime version
    """Tests if date string has valid forma
    
    parameters
    ----------
    date_str: string
    Returns
    -------
    Bool 
        True if format is 'YYYY-MM-DD'
    """
    try:
        y, m, d = [int(f) for f in date_str.split('-')]
        date(y,m,d)
    except:
        return False
    return True

# DefaultFilters 
filters = {
    'token': default,
    'startdate':    lambda a, oa: valid_date_str(a),
    'enddate':      lambda a, oa: valid_date_str(a),
    'sortfield':    lambda a, oa: a in ['id', 'name', 'mindate', 'maxdate', 'datacoverage'],
    'sortorder':    lambda a, oa: a in ['asc', 'desc'],
    'limit':        lambda a, oa: default,
    'offset':       lambda a, oa: default
}

# Default Aliases
aliases = {

}

def validate_args(kwargs, filters, aliases):
    """Checks that arguments pass filter functions
    Parameters
    ----------
    kwargs: dict
        dict of Rest Service parameters
    filters: dict
        dict of validator function matching format <function __main__.f(a, oa)>
        and returns an bool, where a is the agumnet and oa is the list of
        other arguments
    aliases:
        dict mapping alias names to cannon names
    
    Retunrs
    -------
    dict
        cleaned and cannon argument dict
    """
    clean_args = {}
    for arg in kwargs:
        if arg in aliases:
            clean_args[aliases[arg]] = kwargs[arg]
        else:
            clean_args[arg] = kwargs[arg]

    for arg in clean_args:
        clean_args[arg] = str(clean_args[arg])
    
    for arg in clean_args:
        
        other = set(clean_args.keys())
        other.remove(arg)
        if not filters[arg](clean_args[arg], other):
            print('Filter: %s, is invalid' % arg )
            return None
    return clean_args

