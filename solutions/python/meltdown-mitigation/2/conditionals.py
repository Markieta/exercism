"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted) -> bool:
    """Verify criticality is balanced."""

    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage, current, theoretical_max_power) -> str:
    """Assess reactor efficiency zone."""

    efficiency = ((voltage * current) / theoretical_max_power) * 100
    
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold) -> str:
    """Assess and return status code for the reactor."""

    product = temperature * neutrons_produced_per_second
    
    if product < 0.9 * threshold:
        return "LOW"
    elif product <= 1.1 * threshold and 0.9 * threshold <= product:
        return "NORMAL"
    else:
        return "DANGER"
