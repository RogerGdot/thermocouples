"""
Thermocouples - High-accuracy NIST-compliant thermocouple calculations.

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
- Individual thermocouple leg calculations

Example:
--------
>>> import thermocouples as tc
>>>
>>> # Get thermocouple instance
>>> tc_k = tc.get_thermocouple("K")
>>>
>>> # Basic conversions
>>> voltage = tc_k.temp_to_volt(100.0)        # 100°C → V
>>> temp = tc_k.volt_to_temp(0.004096)        # 4.096 mV → °C
>>>
>>> # Seebeck calculations
>>> seebeck = tc_k.temp_to_seebeck(100.0)     # µV/K
>>> dsdt = tc_k.temp_to_dsdt(100.0)           # nV/K²
>>>
>>> # Individual legs (if available)
>>> pos_voltage = tc_k.temp_to_volt_pos_leg(100.0)
>>> neg_voltage = tc_k.temp_to_volt_neg_leg(100.0)
>>>
>>> # Cold junction compensation
>>> temp_compensated = tc_k.volt_to_temp_with_cjc(voltage, ref_temp=25.0)
"""

from .base import Thermocouple
from .registry import THERMOCOUPLE_TYPES, get_thermocouple

# Module metadata
__version__ = "2.1.1"
__author__ = "RogerGdot"

# Export main functionality
__all__ = [
    "Thermocouple",
    "THERMOCOUPLE_TYPES",
    "get_thermocouple",
]
