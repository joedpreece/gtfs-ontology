SERVICE_ID_DEF = """
Identifies a set of dates when service is available for one or more routes.
"""

MONDAY_DEF = """
Indicates whether the service operates on all Mondays in the date range specified by the start_date and end_date fields. Note that exceptions for particular dates may be listed in calendar_dates.txt. Valid options are:

1 - Service is available for all Mondays in the date range.
0 - Service is not available for Mondays in the date range.
"""

TUESDAY_DEF = """
Functions in the same way as monday except applies to Tuesdays
"""

WEDNESDAY_DEF = """
Functions in the same way as monday except applies to Tuesdays
"""

THURSDAY_DEF = """
Functions in the same way as monday except applies to Tuesdays
"""

FRIDAY_DEF = """
Functions in the same way as monday except applies to Tuesdays
"""

SATURDAY_DEF = """
Functions in the same way as monday except applies to Tuesdays
"""

SUNDAY_DEF = """
Functions in the same way as monday except applies to Sundays.
"""

START_DATE_DEF = """
Start service day for the service interval.
"""

END_DATE_DEF = """
End service day for the service interval. This service day is included in the interval.
"""