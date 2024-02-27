import datetime as dt
from math import ceil

def convert_unix_to_datetime_txt(unix, format, timezone_offset=0):
    utc_dt = dt.datetime.utcfromtimestamp(unix)
    local_dt = utc_dt + dt.timedelta(seconds=timezone_offset)
    return local_dt.strftime(format)

def convert_timezone_offset_from_seconds_to_UTC(timezone_offset):
    converted_timezone = "{:.1f}".format(timezone_offset / 3600)
    converted_timezone_as_float = float(converted_timezone)
    additional_sign = "+" if converted_timezone_as_float >= 0 else ""
    if float(converted_timezone_as_float) == ceil(converted_timezone_as_float):
        return f'UTC{additional_sign}{int(converted_timezone_as_float)}'
    else:
        return f'UTC{additional_sign}{converted_timezone}'

def seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    time_components = []
    
    if hours > 0:
        time_components.append(f"{int(hours)} hours")
    if minutes > 0:
        time_components.append(f"{int(minutes)} minutes")
    if seconds > 0:
        time_components.append(f"{int(seconds)} seconds")
    
    return ', '.join(time_components)