"""
Generic Service interface
-------------------------
"""
import os
import copy

import requests
import validators


from . import available

class ValidURLError(Exception):
    """Exception raised if URL is invalid"""
    pass

class BadResponseError(Exception):
    """Exception raised if HTTP response is not 200"""
    pass

class NoDataError(Exception):
    """Exception raised if no data is returned"""
    pass

def execute(urlbase, **kwargs):
    """Execute a HTTP request by joining REST like arguments to an url
    Parameters
    ----------
    urlbase: str
        service url
    kwargs: dict 
        key value pairs to pass as REST argument
    Exceptions
    ----------
    ValidURLError, BadResponseError, NoDataError 
        These are returned if if response is invalid in some form 
    
    Returns
    -------
    str
        response text if response is valid
    """
    args_copy = copy.copy(kwargs)
    headers = {
        'token': args_copy['token']
    }
    del(args_copy['token'])
    args = '&'.join([ '%s=%s' % (k, args_copy[k]) for k in args_copy])
    args = '?' + args.replace(', ',',').replace('[','').replace(']','')

    url = os.path.join(urlbase, args)
    # print(url)
    if 'https://' not in url:
        url = 'https://' + url
   
        # print(url)
    if not validators.url(url):
        raise ValidURLError('URL invalid: %s' % url)

    r = requests.get(url, headers = headers)
    if r.status_code != 200:
        raise BadResponseError('Invalid Response: %s' % r.status_code + r.text)

    if r.text == 'No sites/data found using the selection criteria specified':
        raise NoDataError(r.text)
        
    return r.text

def call(service, **kwargs):
    """Generic call to REST url
    Parameters
    ----------
    service: str
        name of available service see available.py
    kwargs: dict 
        key value pairs to pass as REST argument
    
    Returns
    -------
    str
        response text
    """
    base_url = available.get_url(service)
    
    return execute(base_url, **kwargs)

    


    

