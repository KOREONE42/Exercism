# -*- coding: utf-8 -*-
from datetime import datetime

class LedgerEntry:
    def __init__(self, date=None, description=None, change=None):
        self.date = date
        self.description = description
        self.change = change

def create_entry(date_str, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date_str, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry

def format_date(date_obj, locale):
    """
    Format the date explicitly to guarantee the correct separators.
    
    For en_US, returns MM/DD/YYYY.
    For nl_NL, returns DD-MM-YYYY.
    """
    if locale == 'en_US':
        return f"{date_obj.month:02d}/{date_obj.day:02d}/{date_obj.year:04d}"
    elif locale == 'nl_NL':
        return f"{date_obj.day:02d}-{date_obj.month:02d}-{date_obj.year:04d}"
    else:
        return f"{date_obj.month:02d}/{date_obj.day:02d}/{date_obj.year:04d}"

def format_description(description):
    """
    Return a 25-character string for the description.
    If longer than 25 characters, truncate to 22 and append "..."
    Otherwise, pad on the right.
    """
    if len(description) > 25:
        return description[:22] + "..."
    else:
        return description.ljust(25)

def format_change(change, currency, locale):
    """
    Format the change value as a right–aligned string in a fixed-width field.
    
    For en_US:
      - Negative amounts are wrapped in parentheses.
      - Positive amounts get a trailing space.
      - Thousands are separated by commas.
    For nl_NL:
      - The value is first formatted in the en_US style then commas and
        periods are swapped (to match Dutch formatting).
      - A leading '-' is added for negative numbers.
    
    The canonical tests require that the final field width be 13 characters.
    """
    field_width = 13  # final fixed width for the change column
    if locale == 'en_US':
        symbol = "$" if currency == "USD" else "€"
        value = abs(change) / 100.0
        # Format with thousands separator if needed.
        formatted_value = f"{value:,.2f}"
        if change < 0:
            # Negative: wrapped in parentheses.
            formatted = f"({symbol}{formatted_value})"
        else:
            # Positive: add a trailing space.
            formatted = f"{symbol}{formatted_value} "
        return formatted.rjust(field_width)
    elif locale == 'nl_NL':
        symbol = "$" if currency == "USD" else "€"
        value = abs(change) / 100.0
        formatted_us = f"{value:,.2f}"
        # Swap the grouping separators: commas become periods and decimals become commas.
        temp = formatted_us.replace(",", "#").replace(".", ",").replace("#", ".")
        if change < 0:
            formatted = f"{symbol} -{temp} "
        else:
            formatted = f"{symbol} {temp} "
        return formatted.rjust(field_width)
    else:
        return ""

def format_entries(currency, locale, entries):
    """
    Format the ledger entries into a table.
    
    The header is chosen based on locale.
    Entries are sorted by date, then by change, then by description.
    """
    if locale == 'en_US':
        header = "Date       | Description               | Change       "
    elif locale == 'nl_NL':
        header = "Datum      | Omschrijving              | Verandering  "
    else:
        header = ""
    
    # Sort the entries without mutating the input list.
    sorted_entries = sorted(entries, key=lambda e: (e.date, e.change, e.description))
    
    lines = [header]
    for entry in sorted_entries:
        date_str = format_date(entry.date, locale)
        description_str = format_description(entry.description)
        change_str = format_change(entry.change, currency, locale)
        # Note: The expected rows use the same " | " separator as the header.
        line = f"{date_str} | {description_str} | {change_str}"
        lines.append(line)
    
    return "\n".join(lines)
