"""
Complete thermocouple registry using the new abstract base class architecture.

This module provides a factory pattern for accessing all thermocouple types
through a unified interface while maintaining all original NIST data and
calculation accuracy.

All thermocouple instances inherit from the abstract Thermocouple base class
and provide identical calculation methods with type-specific data.
"""

# Import all thermocouple type classes from types subdirectory
from .base import Thermocouple
from .types.type_b_class import TypeB
from .types.type_e_class import TypeE
from .types.type_j_class import TypeJ
from .types.type_k_class import TypeK
from .types.type_n_class import TypeN
from .types.type_r_class import TypeR
from .types.type_s_class import TypeS
from .types.type_t_class import TypeT

# Registry of all available thermocouple classes
_THERMOCOUPLE_CLASSES: dict[str, type[Thermocouple]] = {
    "K": TypeK,
    "J": TypeJ,
    "E": TypeE,
    "T": TypeT,
    "N": TypeN,
    "R": TypeR,
    "S": TypeS,
    "B": TypeB,
}

# Available thermocouple types (currently implemented)
THERMOCOUPLE_TYPES = list(_THERMOCOUPLE_CLASSES.keys())


def get_thermocouple(tc_type: str) -> Thermocouple:
    """
    Factory function to get a thermocouple instance by type.

    Parameters:
    -----------
    tc_type : str
        The thermocouple type designation (e.g., "K", "J", "E", etc.)
        Case insensitive.

    Returns:
    --------
    Thermocouple
        An instance of the requested thermocouple type inheriting from
        the Thermocouple abstract base class.

    Raises:
    -------
    ValueError
        If the requested thermocouple type is not available.

    Example:
    --------
    >>> tc_k = get_thermocouple("K")
    >>> voltage = tc_k.temperature_to_voltage(100.0)  # 100°C -> voltage
    >>> temp = tc_k.voltage_to_temperature(0.004096)  # 4.096 mV -> temperature
    """
    tc_type_upper = tc_type.upper()

    if tc_type_upper not in _THERMOCOUPLE_CLASSES:
        available = ", ".join(sorted(THERMOCOUPLE_TYPES))
        raise ValueError(f"Thermocouple type '{tc_type}' not available. Available types: {available}")

    return _THERMOCOUPLE_CLASSES[tc_type_upper]()


# Convenience functions for direct usage without creating instances
def temperature_to_voltage(tc_type: str, temperature: float, reference_junction_temp: float = 0.0) -> float:
    """
    Convert temperature to voltage for a specific thermocouple type.

    Parameters:
    -----------
    tc_type : str
        The thermocouple type designation (e.g., "K", "J", "E")
    temperature : float
        Temperature in degrees Celsius
    reference_junction_temp : float, optional
        Reference junction temperature in degrees Celsius (default: 0.0)

    Returns:
    --------
    float
        Voltage in volts

    Example:
    --------
    >>> voltage = temperature_to_voltage("K", 100.0)
    >>> print(f"{voltage:.6f} V")  # 0.004096 V
    """
    tc = get_thermocouple(tc_type)
    return tc.temperature_to_voltage(temperature, reference_junction_temp)


def voltage_to_temperature(tc_type: str, voltage: float, reference_junction_temp: float = 0.0) -> float:
    """
    Convert voltage to temperature for a specific thermocouple type.

    Parameters:
    -----------
    tc_type : str
        The thermocouple type designation (e.g., "K", "J", "E")
    voltage : float
        Voltage in volts
    reference_junction_temp : float, optional
        Reference junction temperature in degrees Celsius (default: 0.0)

    Returns:
    --------
    float
        Temperature in degrees Celsius

    Example:
    --------
    >>> temp = voltage_to_temperature("K", 0.004096)
    >>> print(f"{temp:.2f} °C")  # 100.00 °C
    """
    tc = get_thermocouple(tc_type)
    return tc.voltage_to_temperature(voltage, reference_junction_temp)


def voltage_to_temperature_with_reference(tc_type: str, voltage: float, reference_junction_temp: float) -> float:
    """
    Convert voltage to temperature with explicit reference junction compensation.

    This is an alias for voltage_to_temperature() with explicit reference temperature.

    Parameters:
    -----------
    tc_type : str
        The thermocouple type designation (e.g., "K", "J", "E")
    voltage : float
        Voltage in volts
    reference_junction_temp : float
        Reference junction temperature in degrees Celsius

    Returns:
    --------
    float
        Temperature in degrees Celsius
    """
    return voltage_to_temperature(tc_type, voltage, reference_junction_temp)


def temp_to_seebeck(tc_type: str, temperature: float) -> float:
    """
    Calculate Seebeck coefficient at a specific temperature.

    Parameters:
    -----------
    tc_type : str
        The thermocouple type designation (e.g., "K", "J", "E")
    temperature : float
        Temperature in degrees Celsius

    Returns:
    --------
    float
        Seebeck coefficient in microvolts per Kelvin (µV/K)

    Example:
    --------
    >>> seebeck = temp_to_seebeck("K", 100.0)
    >>> print(f"{seebeck:.2f} µV/K")
    """
    tc = get_thermocouple(tc_type)
    return tc.temp_to_seebeck(temperature)


def temp_to_dsdt(tc_type: str, temperature: float) -> float:
    """
    Calculate the temperature derivative of Seebeck coefficient (dS/dT).

    Parameters:
    -----------
    tc_type : str
        The thermocouple type designation (e.g., "K", "J", "E")
    temperature : float
        Temperature in degrees Celsius

    Returns:
    --------
    float
        Temperature derivative of Seebeck coefficient in nanovolts per Kelvin squared (nV/K²)

    Example:
    --------
    >>> dsdt = temp_to_dsdt("K", 100.0)
    >>> print(f"{dsdt:.2f} nV/K²")
    """
    tc = get_thermocouple(tc_type)
    return tc.temp_to_dsdt(temperature)


# Module exports
__all__ = [
    "THERMOCOUPLE_TYPES",
    "get_thermocouple",
    "temperature_to_voltage",
    "voltage_to_temperature",
    "voltage_to_temperature_with_reference",
    "temp_to_seebeck",
    "temp_to_dsdt",
]
