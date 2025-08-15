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
    >>> voltage = tc_k.temp_to_volt(100.0)     # 100°C -> voltage
    >>> temp = tc_k.volt_to_temp(0.004096)     # 4.096 mV -> temperature
    """
    tc_type_upper = tc_type.upper()

    if tc_type_upper not in _THERMOCOUPLE_CLASSES:
        available = ", ".join(sorted(THERMOCOUPLE_TYPES))
        raise ValueError(f"Thermocouple type '{tc_type}' not available. Available types: {available}")

    return _THERMOCOUPLE_CLASSES[tc_type_upper]()


# Module exports
__all__ = [
    "THERMOCOUPLE_TYPES",
    "get_thermocouple",
]
