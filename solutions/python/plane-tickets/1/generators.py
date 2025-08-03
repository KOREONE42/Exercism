"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Seat letters are generated from A to D.
    After D it should start again with A.
    """
    letters = ['A', 'B', 'C', 'D']
    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.
    """
    count = 0
    row = 1
    letters = ['A', 'B', 'C', 'D']
    
    while count < number:
        if row == 13:
            row += 1
            continue
        for letter in letters:
            if count >= number:
                break
            yield f"{row}{letter}"
            count += 1
        row += 1


def assign_seats(passengers):
    """Assign seats to passengers."""
    seat_generator = generate_seats(len(passengers))
    return {passenger: next(seat_generator) for passenger in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Returns a 12-character string: seat + flight_id + padding zeros.
    """
    for seat in seat_numbers:
        code = f"{seat}{flight_id}"
        padding = "0" * (12 - len(code))
        yield code + padding
