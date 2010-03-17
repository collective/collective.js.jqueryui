from zope.i18n import translate
import time


def get_datepicker_date_format(request):
    """Return a localized date format we can use with the datepicker
    jqueryui plugin. The date format is retrieved from the
    date_format_short_datepicker msgid in the plonelocales i18n domain.
    Return 'mm/dd/yy' if no translation has been found.
    """
    date_format = translate(u"date_format_short_datepicker",
                            domain="plonelocales",
                            context=request)
    if date_format == u"date_format_short_datepicker":
        return 'mm/dd/yy'
    return date_format


def transform_to_percent(date_format):
    """Transform a jquery `date_format` to a date format that time.strptime
    understand. Replace "mm" by "%m", "dd" by "%d", and "yy" by "%Y".

    >>> transform_to_percent("mm/dd/yy")
    "%m/%d/%Y"
    >>> transform_to_percent("dd/mm/yy")
    "%d/%m/%Y"
    >>> transform_to_percent("yy/mm/dd")
    "%Y/%m/%d"
    >>> transform_to_percent("yy-mm-dd")
    "%Y/%m/%d"
    >>> transform_to_percent("dd.mm.yy")
    "%d.%m.%Y"
    >>> transform_to_percent("dd.mm.yy.")
    "%d.%m.%Y."
    >>> transform_to_percent("yy.mm.dd.")
    "%Y.%m.%d."
    """
    return date_format.replace(
        "mm", "%m").replace(
        "dd", "%d").replace(
        "yy", "%Y")


def parseDate(datestr, request):
    """Parse datestr and return a tuple (year, month, day)
    request parameter is necessary to retrieve the date_format from
    the language extracted from the request.
    """
    date_format = transform_to_percent(get_datepicker_date_format(request))
    return time.strptime(datestr, date_format)[:3]
