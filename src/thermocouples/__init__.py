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
- Support for individual thermocouple legs

Example:
--------
>>> from thermocouples import get_thermocouple, temperature_to_voltage
>>>
>>> # Using thermocouple instance
>>> tc_k = get_thermocouple("K")
>>> voltage = tc_k.temperature_to_voltage(100.0)  # 100°C
>>> temp = tc_k.voltage_to_temperature(0.004096)  # 4.096 mV
>>>
>>> # Using convenience functions
>>> voltage = temperature_to_voltage("K", 100.0)
>>> temp = voltage_to_temperature("K", 0.004096)
"""

# Import main API from registry
from .registry import (
    # Constants
    THERMOCOUPLE_TYPES,
    # Main class
    ThermocoupleType,
    # Convenience functions
    get_thermocouple,
    temp_to_dsdt,
    temp_to_seebeck,
    temperature_to_voltage,
    voltage_to_temperature,
    voltage_to_temperature_with_reference,
)

# Module metadata
__version__ = "1.1.0"
__author__ = "Dipl.-Ing. Gregor Oppitz"
__email__ = "gregor.oppitz@dlr.de"
__license__ = "MIT"
__url__ = "https://github.com/your-username/python-thermocouples"

# Define what gets exported when using "from thermocouples import *"
__all__ = [
    # Main class
    "ThermocoupleType",
    # Convenience functions
    "get_thermocouple",
    "temperature_to_voltage",
    "voltage_to_temperature",
    "voltage_to_temperature_with_reference",
    "temp_to_seebeck",
    "temp_to_dsdt",
    # Constants
    "THERMOCOUPLE_TYPES",
    # Metadata
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__url__",
]
