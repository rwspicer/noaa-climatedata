"""
Formats
-------

Functions for converting response formats
"""
from pandas import DataFrame

def as_DataFrame(callback,  **kwargs):
    """Converts response to DataFrame

    Parameters
    ----------
    callback: function or dict
        if function: a service callback
        if dict: the response of a service callback
    kwargs: dict
        dict of rest arguments

    Returns
    -------
    DataFrame
    """
    if type(callback) is dict:
        response = callback
    else:
        response = callback(**kwargs)

    table = DataFrame(response['results'])
    return table


def save_as_csv(filename, callback, **kwargs):
    """Converts response to csv file

    Parameters
    ----------
    filename: path
        name to save file
    callback: function or dict
        if function: a service callback
        if dict: the response of a service callback
        if DataFrame: result of as_DataFrame
    kwargs: dict
        dict of rest arguments
    """
    if type(callback) is dict:
        response = as_DataFrame(callback)
    elif type(callback) is DataFrame: 
        response = callback
    else:
        response = callback(**kwargs)
        response = as_DataFrame(callback)
    
    response.to_csv(filename, mode='w')

