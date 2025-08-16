from datetime import datetime, timedelta
from typing import Union

_ISO_FMT = "%Y-%m-%dT%H:%M:%S"

# --- Utilities ---------------------------------------------------------------

def _parse_dt(start: Union[str, datetime]) -> datetime:
    """Accept a datetime or ISO string (YYYY-MM-DDTHH:MM:SS)."""
    if isinstance(start, datetime):
        return start
    try:
        return datetime.strptime(start, _ISO_FMT)
    except Exception as e:
        raise ValueError(f"Invalid start datetime: {start!r}") from e

def _fmt(dt: datetime) -> str:
    return dt.strftime(_ISO_FMT)

def _first_workday_at_8(year: int, month: int) -> datetime:
    d = datetime(year, month, 1, 8, 0, 0)
    while d.weekday() >= 5:  # 5=Sat, 6=Sun
        d += timedelta(days=1)
    return d

def _last_day_of_month(year: int, month: int) -> datetime:
    if month == 12:
        return datetime(year, 12, 31)
    return datetime(year, month + 1, 1) - timedelta(days=1)

def _last_workday_at_8(year: int, month: int) -> datetime:
    d = _last_day_of_month(year, month).replace(hour=8, minute=0, second=0, microsecond=0)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d

# --- Main --------------------------------------------------------------------

def delivery_date(start: Union[str, datetime], description: str) -> str:
    """
    Translate a delivery date description into an absolute datetime (ISO string).

    Rules:
      - NOW  -> start + 2h
      - ASAP -> if start < 13:00 then today 17:00 else tomorrow 13:00
      - EOW  -> Mon/Tue/Wed -> Friday 17:00; Thu/Fri -> Sunday 20:00
      - <N>M -> first workday 08:00 of month N (this year if start.month < N, else next year)
      - Q<N> -> last workday 08:00 of quarter N (this year if start in/before QN, else next year)
    """
    dt = _parse_dt(start)
    desc = description.strip().upper()

    # --- Fixed keywords ---
    if desc == "NOW":
        return _fmt(dt + timedelta(hours=2))

    if desc == "ASAP":
        if dt.hour < 13:
            return _fmt(dt.replace(hour=17, minute=0, second=0, microsecond=0))
        else:
            tmr = dt + timedelta(days=1)
            return _fmt(tmr.replace(hour=13, minute=0, second=0, microsecond=0))

    if desc == "EOW":
        wd = dt.weekday()  # Mon=0..Sun=6
        if wd <= 2:  # Mon/Tue/Wed -> Friday 17:00
            target = dt + timedelta(days=(4 - wd))
            return _fmt(target.replace(hour=17, minute=0, second=0, microsecond=0))
        else:        # Thu/Fri (and weekends handled sensibly) -> Sunday 20:00
            target = dt + timedelta(days=(6 - wd))
            return _fmt(target.replace(hour=20, minute=0, second=0, microsecond=0))

    # --- Variable: <N>M ---
    if desc.endswith("M") and desc[:-1].isdigit():
        N = int(desc[:-1])
        if not (1 <= N <= 12):
            raise ValueError(f"Month spec out of range: {description!r}")
        year = dt.year if dt.month < N else dt.year + 1
        return _fmt(_first_workday_at_8(year, N))

    # --- Variable: Q<N> ---
    if desc.startswith("Q") and desc[1:].isdigit():
        N = int(desc[1:])
        if not (1 <= N <= 4):
            raise ValueError(f"Quarter spec out of range: {description!r}")

        end_month = {1: 3, 2: 6, 3: 9, 4: 12}[N]
        current_q = (dt.month - 1) // 3 + 1
        year = dt.year if current_q <= N else dt.year + 1
        return _fmt(_last_workday_at_8(year, end_month))

    raise ValueError(f"Unknown description: {description!r}")
