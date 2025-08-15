"""
Python Thermocouples - High-accuracy NIST-compliant thermocouple calculations.

This package provides comprehensive thermocouple calculation capabilities for all
standard thermocouple types (B, E, J, K, N, R, S, T) based on NIST Monograph 175.

Features:
---------
- Temperature to voltage conversion (°C to V)
- Voltage to temperature conversion (V to °C)
- Seebeck coefficient calculation (µV/K)
- dSeebeck/dT calculation (nV/K²)
- Cold junction compensation
- High-accuracy NIST polynomial calculations
- Support for individual thermocouple legs:
  - Voltage calculations for positive and negative legs
  - Seebeck coefficient calculations for positive and negative legs

Example:
--------
>>> from thermocouples import get_thermocouple, temp_to_voltage
>>>
>>> # Using thermocouple instance (recommended)
>>> tc_k = get_thermocouple("K")
>>> voltage = tc_k.temperature_to_voltage(100.0)  # 100°C
>>> temp = tc_k.voltage_to_temperature(0.004096)  # 4.096 mV
>>>
>>> # Using legacy functions (backward compatibility)
>>> voltage = temp_to_voltage(100.0, "K")
>>> temp = voltage_to_temp(0.004096, "K")
"""

import warnings

from .base import Thermocouple
from .registry import THERMOCOUPLE_TYPES, get_thermocouple


# Legacy compatibility functions (maintained for backward compatibility)
def temp_to_voltage(temperature: float, tc_type: str, cold_junction: float = 0.0) -> float:
    """
    Convert temperature to voltage for specified thermocouple type.

    Args:
        temperature: Temperature in °C
        tc_type: Thermocouple type ("B", "E", "J", "K", "N", "R", "S", "T")
        cold_junction: Cold junction temperature in °C (default: 0.0)

    Returns:
        Voltage in V
    """
    tc = get_thermocouple(tc_type)
    voltage_hot = tc.temperature_to_voltage(temperature)
    if cold_junction != 0.0:
        voltage_cold = tc.temperature_to_voltage(cold_junction)
        return voltage_hot - voltage_cold
    return voltage_hot


def voltage_to_temp(voltage: float, tc_type: str, cold_junction: float = 0.0) -> float:
    """
    Convert voltage to temperature for specified thermocouple type.

    Args:
        voltage: Voltage in V
        tc_type: Thermocouple type ("B", "E", "J", "K", "N", "R", "S", "T")
        cold_junction: Cold junction temperature in °C (default: 0.0)

    Returns:
        Temperature in °C
    """
    tc = get_thermocouple(tc_type)
    if cold_junction != 0.0:
        voltage_cold = tc.temperature_to_voltage(cold_junction)
        voltage = voltage + voltage_cold
    return tc.voltage_to_temperature(voltage)


def temp_to_seebeck(temperature: float, tc_type: str) -> float:
    """
    Calculate Seebeck coefficient for specified thermocouple type.

    Args:
        temperature: Temperature in °C
        tc_type: Thermocouple type ("B", "E", "J", "K", "N", "R", "S", "T")

    Returns:
        Seebeck coefficient in µV/K
    """
    tc = get_thermocouple(tc_type)
    return tc.temp_to_seebeck(temperature)


def temp_to_dsdt(temperature: float, tc_type: str) -> float:
    """
    Calculate temperature derivative of Seebeck coefficient.

    Args:
        temperature: Temperature in °C
        tc_type: Thermocouple type ("B", "E", "J", "K", "N", "R", "S", "T")

    Returns:
        dSeebeck/dT in nV/K²
    """
    tc = get_thermocouple(tc_type)
    return tc.temp_to_dsdt(temperature)


# Individual leg functions for advanced applications
def pos_temp_to_voltage(temperature: float, tc_type: str) -> float:
    """Calculate positive leg voltage for specified thermocouple type."""
    tc = get_thermocouple(tc_type)
    return tc.temperature_to_volt_pos_leg(temperature)


def neg_temp_to_voltage(temperature: float, tc_type: str) -> float:
    """Calculate negative leg voltage for specified thermocouple type."""
    tc = get_thermocouple(tc_type)
    return tc.temperature_to_volt_neg_leg(temperature)


def pos_temp_to_seebeck(temperature: float, tc_type: str) -> float:
    """Calculate positive leg Seebeck coefficient for specified thermocouple type."""
    tc = get_thermocouple(tc_type)
    return tc.temperature_to_seebeck_pos_leg(temperature)


def neg_temp_to_seebeck(temperature: float, tc_type: str) -> float:
    """Calculate negative leg Seebeck coefficient for specified thermocouple type."""
    tc = get_thermocouple(tc_type)
    return tc.temperature_to_seebeck_neg_leg(temperature)


# Additional convenience functions for common use cases
def get_available_types():
    """Get list of all available thermocouple types."""
    return THERMOCOUPLE_TYPES


# Module metadata
__version__ = "2.0.0"  # Major version bump for new OOP architecture
__author__ = "Dipl.-Ing. Gregor Oppitz"

# Export all main functionality
__all__ = [
    "Thermocouple",
    "THERMOCOUPLE_TYPES",
    "get_thermocouple",
    "get_available_types",
    "temp_to_voltage",
    "voltage_to_temp",
    "temp_to_seebeck",
    "temp_to_dsdt",
    "pos_temp_to_voltage",
    "neg_temp_to_voltage",
    "pos_temp_to_seebeck",
    "neg_temp_to_seebeck",
]


def _create_legacy_thermocouple_type():
    """Create a legacy ThermocoupleType class for backwards compatibility."""

    class ThermocoupleType:
        """
        Legacy ThermocoupleType class for backwards compatibility.

        This class is deprecated. Use the new get_thermocouple() function instead.

        Example:
        --------
        Old way (deprecated):
        >>> tc = ThermocoupleType(name, ...)  # Complex initialization

        New way (recommended):
        >>> tc = get_thermocouple("K")  # Simple factory function
        """

        def __init__(self, *args, **kwargs):
            warnings.warn(
                "ThermocoupleType is deprecated and will be removed in a future version. Use get_thermocouple() instead.", DeprecationWarning, stacklevel=2
            )
            # For now, just create a Type K instance for basic compatibility
            self._instance = get_thermocouple("K")

        def __getattr__(self, name):
            # Delegate all attribute access to the new instance
            return getattr(self._instance, name)

    return ThermocoupleType


# Provide legacy compatibility
ThermocoupleType = _create_legacy_thermocouple_type()
