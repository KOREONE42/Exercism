from datetime import datetime, timedelta

_ISO_FMT = "%Y-%m-%dT%H:%M:%S"

def _parse_start(start):
    if isinstance(start, datetime):
        return start
    # assume ISO string like "YYYY-MM-DDTHH:MM:SS"
    return datetime.strptime(start, _ISO_FMT)

def _format(dt: datetime) -> str:
    return dt.strftime(_ISO_FMT)

def _first_workday_at_8(year: int, month: int) -> datetime:
    d = datetime(year, month, 1, 8, 0, 0)
    while d.weekday() >= 5:  # Sat=5, Sun=6
        d += timedelta(days=1)
    return d

def _last_day_of_month(year: int, month: int) -> datetime:
    if month == 12:
        return datetime(year, 12, 31)
    return datetime(year, month + 1, 1) - timedelta(days=1)

def _last_workday_at_8(year: int, month: int) -> datetime:
    d = _last_day_of_month(year, month).replace(hour=8, minute=0, second=0, microsecond=0)
    while d.weekday() >= 5:  # back up to Fri if weekend
        d -= timedelta(days=1)
    return d

def delivery_date(start, description):
    """
    start: ISO string 'YYYY-MM-DDTHH:MM:SS' or datetime
    description: 'NOW' | 'ASAP' | 'EOW' | '<N>M' | 'Q<N>'
    returns ISO string 'YYYY-MM-DDTHH:MM:SS'
    """
    dt = _parse_start(start)
    desc = description.strip().upper()

    # --- Fixed ---
    if desc == "NOW":
        return _format(dt + timedelta(hours=2))

    if desc == "ASAP":
        if dt.hour < 13:
            return _format(dt.replace(hour=17, minute=0, second=0, microsecond=0))
        else:
            tmr = dt + timedelta(days=1)
            return _format(tmr.replace(hour=13, minute=0, second=0, microsecond=0))

    if desc == "EOW":
        wd = dt.weekday()  # Mon=0..Sun=6
        if wd <= 2:  # Mon/Tue/Wed -> Friday 17:00
            days_until_fri = 4 - wd
            target = dt + timedelta(days=days_until_fri)
            return _format(target.replace(hour=17, minute=0, second=0, microsecond=0))
        else:       # Thu/Fri (and weekends fall here too) -> Sunday 20:00
            days_until_sun = 6 - wd
            target = dt + timedelta(days=days_until_sun)
            return _format(target.replace(hour=20, minute=0, second=0, microsecond=0))

    # --- Variable: <N>M ---
    if desc.endswith("M") and desc[:-1].isdigit():
        N = int(desc[:-1])
        year = dt.year
        if dt.month < N:
            return _format(_first_workday_at_8(year, N))
        else:
            return _format(_first_workday_at_8(year + 1, N))

    # --- Variable: Q<N> ---
    if desc.startswith("Q") and desc[1:].isdigit():
        N = int(desc[1:])
        # end month of the quarter
        end_month = {1: 3, 2: 6, 3: 9, 4: 12}[N]
        year = dt.year
        current_q = (dt.month - 1) // 3 + 1

        if current_q <= N:  # before or in N-th quarter this year
            return _format(_last_workday_at_8(year, end_month))
        else:               # after N-th quarter -> next year
            return _format(_last_workday_at_8(year + 1, end_month))

    raise ValueError(f"Unknown description: {description}")
