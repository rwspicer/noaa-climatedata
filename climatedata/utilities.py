"""
Utility Functions
----------------
"""
from . import services
import copy
from datetime import datetime

class MaxAttemptError(Exception):
    """Exception raised if max attempts exceeded, likely due to server-side error"""
    pass


def attempt(callback, max_tries=10, verbose=False, **kwargs):
    """
    """
    success = False
    for idx in range(1,max_tries):
        if verbose: print('attempt %s' % idx)
        try:
            rsp = callback(**kwargs)
            success = True
            break
        except services.generic.BadResponseError as e:
            pass
    if not success:
        raise MaxAttemptError('attempts exceeded')
    return rsp

def depaginate(callback, **kwargs):
    """De-paginates multi page results, calls callback multiple times
    until all pages of data have been retrieves and merges results into a single
    response.

    Parameters
    ----------
    callback: function 
        a service callback
    kwargs: dict
        dict of rest arguments

    Returns
    -------
    Dict
    """
    if not 'limit' in kwargs:
        kwargs['limit'] = 100

    j_init = callback(**kwargs) # INIT JSON
    # print(j_init['metadata']['resultset'])
    # print(j_init)
    if j_init == {}:
        return {
            'metadata':{}, 'results':[]
        }
    count = j_init['metadata']['resultset']['count']
    limit = j_init['metadata']['resultset']['limit']
    offset = j_init['metadata']['resultset']['offset'] + limit

    j_com = copy.deepcopy(j_init) # COMBINED JSON

    while offset <= count:
        kwargs['offset'] =  offset
        # print ('offset %s' % offset)

        j_next = attempt(callback, 20, **kwargs)
        
        j_com['results'] += j_next['results']
        offset+=limit

    j_com['metadata']['resultset']['limit']=count

    return j_com



def get_data_for_temporal_extent(callback, **kwargs):
    """Calls services multiple times to fetch all data between 
    kwargs['startdate'] and kwargs['enddate'] then De-paginates and merges 
    results into a single response. This function creates a work around for 
    the fact that the services can only retrieve a single years worth of data


    Parameters
    ----------
    callback: function 
        a service callback
    kwargs: dict
        dict of rest arguments

    Returns
    -------
    Dict
    """
    sd = datetime.strptime(kwargs['startdate'], '%Y-%m-%d')
    ed = datetime.strptime(kwargs['enddate'], '%Y-%m-%d')
    date_ranges = []
    for y in range(sd.year, ed.year):
        date_ranges.append([datetime(y,1,1), datetime(y,12,31)])
    date_ranges[0][0]=sd
    date_ranges.append([datetime(ed.year,1,1), ed])

    results = []

    # data_missing = []
    for dr in date_ranges:
        # print(dr)
        kwargs['startdate'] = dr[0].strftime( '%Y-%m-%d')
        kwargs['enddate'] = dr[1].strftime( '%Y-%m-%d')

        rsp = depaginate(callback, **kwargs)
        results += rsp['results']

    return {
        'metadata': {
            'resultset': {
                'offset': 1, 'count': len(results), 'limit': len(results)
                },
            # 'missing_ranges': [
            #     (dr[0].strftime( '%Y-%m-%d'),dr[1].strftime( '%Y-%m-%d')) for dr in data_missing
            # ]
            }, 
        'results':results
    }
