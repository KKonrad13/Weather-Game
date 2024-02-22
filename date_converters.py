import datetime as dt
from math import ceil

def convert_unix_to_datetime_txt(unix, format, timezone_offset):
    utc_dt = dt.datetime.utcfromtimestamp(unix)
    local_dt = utc_dt + dt.timedelta(seconds=timezone_offset)
    return local_dt.strftime(format)

def convert_timezone_offset_from_seconds_to_hours(timezone_offset):
    converted_timezone = "{:.1f}".format(timezone_offset / 3600)
    converted_timezone_as_float = float(converted_timezone)
    additional_sign = "+" if converted_timezone_as_float >= 0 else ""
    if float(converted_timezone_as_float) == ceil(converted_timezone_as_float):
        return f'UTC{additional_sign}{int(converted_timezone_as_float)}'
    else:
        return f'UTC{additional_sign}{converted_timezone}'
