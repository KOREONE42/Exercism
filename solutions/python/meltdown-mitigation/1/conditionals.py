"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?
    """
    return (
        temperature < 800 and
        neutrons_emitted > 500 and
        (temperature * neutrons_emitted) < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').
    """
    generated_power = voltage * current
    efficiency_percentage = (generated_power / theoretical_max_power) * 100

    if efficiency_percentage >= 80:
        return 'green'
    elif 60 <= efficiency_percentage < 80:
        return 'orange'
    elif 30 <= efficiency_percentage < 60:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').
    """
    product = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold

    if product < lower_bound:
        return 'LOW'
    elif lower_bound <= product <= upper_bound:
        return 'NORMAL'
    else:
        return 'DANGER'