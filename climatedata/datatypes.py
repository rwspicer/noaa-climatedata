"""
Data Types
----------

Metadata and unit conversion functions for GHCN data types
"""
names = {
    "PRCP" : 'total-daily-precipitation-mm',
    "SNOW" : 'total-daily-snowfall-mm',
    "SNWD" : 'total-daily-snow-depth-mm',
    "TMIN" : 'min-daily-air-tempererature-°C',
    "TMAX" : 'max-daily-air-tempererature-°C',
    "TOBS" : 'instantaneous-daily-air-tempererature-°C',
    "ACMH" : 'mean-midnight-midnight-cloudiness-%',
    "ACSH" : 'mean-sunrise-sunset-cloudiness-%',
    "AWDR" : 'mean-daily-wind-direction-°',
    "AWND" : 'mean-daily-wind-speed-m/s',
    "FMTM" : 'peak-daily-fastest-minute-wind-HHMM',
    "PGTM" : 'peak-daily-gust-time-HHMM',
    "PSUN" : 'total-daily-sunshine-%',
    "TSUN" : 'total-daily-sunshine-minutes',
    "TAVG" : 'mean-daily-air-tempererature-°C',
    "WDF1" : 'fastest-1-min-daily-wind-direction-°',
    "WDF2" : 'fastest-2-min-daily-wind-direction-°',
    "WDF5" : 'fastest-5-min-daily-wind-direction-°',
    "WDFG" : 'peak-daily-gust-direction-°',
    "WDFM" : 'peak-daily-wind-direction-°',
    "WDMV" : 'total-daily-wind-movement-km',
    "WESD" : 'total-daily-snow-water-equivalent-mm',
    "WSF1" : 'fastest-1-min-daily-wind-speed-m/s',
    "WSF2" : 'fastest-2-min-daily-wind-speed-m/s',
    "WSF5" : 'fastest-5-min-daily-wind-speed-m/s',
    "WSFG" : 'peak-daily-gust-m/s',
    "WSFI" : 'peak-daily-wind-speed-m/s',
    "WSFM" : 'peak-daily-fastest-minute-wind-m/s',
    "THIC" : 'total-daily-ice-thickness-on-water-mm',
}

units = {
    "PRCP" : "tenths of mm", 
    "SNOW" : "tenths of mm",
    "SNWD" : 'tenths of mm',
    "TMIN" : 'tenths of °C',
    "TMAX" : 'tenths of °C',
    "TOBS" : 'tenths of °C',
}

def from_tenths(x): 
    return x*0.10

def mm_to_in(x): 
    return x * 0.0393701

def c_to_f(x):
    return (x * 9/5) + 32

conversions = {
    "PRCP" : {
        'to_mm': from_tenths, 
        'to_in':lambda x: mm_to_in(from_tenths(x))
    }, 
    "SNOW" : {
        'to_mm': from_tenths, 
        'to_in':lambda x: mm_to_in(from_tenths(x))
    }, 
    "SNWD" : {
        'to_mm': from_tenths, 
        'to_in':lambda x: mm_to_in(from_tenths(x))
    }, 
    "TMIN" : {
        'to_deg_c': from_tenths,
        'to_deg_f':lambda x: c_to_f(from_tenths(x)) 
    },
    "TMAX" : {
        'to_deg_c': from_tenths,
        'to_deg_f':lambda x: c_to_f(from_tenths(x)) 
    },
    "TOBS" : {
        'to_deg_c': from_tenths,
        'to_deg_f':lambda x: c_to_f(from_tenths(x)) 
    },
}
