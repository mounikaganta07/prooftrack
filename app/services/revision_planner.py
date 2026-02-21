from datetime import date, timedelta

DEFAULT_INTERVALS = [1, 3, 7, 14]


def build_revision_dates(start: date | None = None, intervals=None):
    if start is None:
        start = date.today()
    if intervals is None:
        intervals = DEFAULT_INTERVALS

    return [(start + timedelta(days=d), d) for d in intervals]