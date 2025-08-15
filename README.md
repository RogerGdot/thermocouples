# Python Thermocouples

[![PyPI version](https://badge.fury.io/py/thermocouples.svg)](https://badge.fury.io/py/thermocouples)
[![Python](https://img.shields.io/pypi/pyversions/thermocouples.svg)](https://pypi.org/project/thermocouples/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, high-accuracy thermocouple calculation library for Python, implementing all standard thermocouple types with NIST-compliant polynomial calculations.

## Features

- **Temperature to Voltage Conversion**: Convert temperature (°C) to thermoelectric voltage (V)
- **Voltage to Temperature Conversion**: Convert voltage (V) to temperature (°C)
- **Seebeck Coefficient Calculation**: Get the Seebeck coefficient (µV/K) at any temperature
- **Temperature Derivative of Seebeck**: Calculate dSeebeck/dT (nV/K²) for advanced analysis
- **Cold Junction Compensation**: Built-in support for reference junction temperature compensation
- **Individual Thermocouple Leg Calculations**: 
  - Voltage calculations for positive and negative legs separately
  - Seebeck coefficient calculations for positive and negative legs separately
- **High Accuracy**: Based on NIST Monograph 175 polynomial coefficients
- **All Standard Types**: Supports B, E, J, K, N, R, S, and T type thermocouples
- **Pure Python**: No external dependencies required
- **Well Tested**: Comprehensive test suite ensuring accuracy

## Supported Thermocouple Types

| Type | Temperature Range | Materials |
|------|------------------|-----------|
| **B** | 0°C to 1820°C | Pt-30%Rh / Pt-6%Rh |
| **E** | -270°C to 1000°C | Ni-Cr / Cu-Ni |
| **J** | -210°C to 1200°C | Fe / Cu-Ni |
| **K** | -270°C to 1372°C | Ni-Cr / Ni-Al |
| **N** | -270°C to 1300°C | Ni-Cr-Si / Ni-Si |
| **R** | -50°C to 1768°C | Pt-13%Rh / Pt |
| **S** | -50°C to 1768°C | Pt-10%Rh / Pt |
| **T** | -270°C to 400°C | Cu / Cu-Ni |

## Installation

```bash
pip install thermocouples
```

## Quick Start

```python
from thermocouples import get_thermocouple, temperature_to_voltage

# Method 1: Using thermocouple instance
tc_k = get_thermocouple("K")
voltage = tc_k.temperature_to_voltage(100.0)  # 100°C → 0.004096 V
temp = tc_k.voltage_to_temperature(0.004096)  # 0.004096 V → 100°C

# Method 2: Using convenience functions
voltage = temperature_to_voltage("K", 100.0)
temp = voltage_to_temperature("K", 0.004096)

# Cold junction compensation (measuring with reference temperature)
measured_voltage = 0.025  # V
reference_temp = 25.0     # °C
actual_temp = tc_k.voltage_to_temperature_with_reference(
    measured_voltage, reference_temp
)
```

## Advanced Usage

### Seebeck Coefficient Calculation

```python
tc_k = get_thermocouple("K")

# Calculate Seebeck coefficient (sensitivity) at 100°C
seebeck = tc_k.temperature_to_seebeck(100.0)  # Returns µV/K
print(f"Sensitivity at 100°C: {seebeck:.2f} µV/K")

# Calculate temperature coefficient of Seebeck coefficient
dsdt = tc_k.temperature_to_dsdt(100.0)  # Returns nV/K²
print(f"dS/dT at 100°C: {dsdt:.2f} nV/K²")
```

### Individual Thermocouple Legs

For advanced applications, you can calculate voltages for individual thermocouple legs:

```python
# Get voltage for positive leg only (Ni-Cr for Type K)
v_pos = tc_k.temperature_to_volt_pos_leg(100.0)  # Returns voltage in V

# Get voltage for negative leg only (Ni-Al for Type K)
v_neg = tc_k.temperature_to_volt_neg_leg(100.0)  # Returns voltage in V

# The total thermocouple voltage is the difference
v_total = v_pos - v_neg  # Should equal tc_k.temperature_to_voltage(100.0)
```

### Individual Leg Seebeck Coefficients

You can also calculate Seebeck coefficients for individual thermocouple legs:

```python
# Get Seebeck coefficient for positive leg (Ni-Cr for Type K)
seebeck_pos = tc_k.temperature_to_seebeck_pos_leg(100.0)  # Returns µV/K
print(f"Positive leg Seebeck at 100°C: {seebeck_pos:.3f} µV/K")

# Get Seebeck coefficient for negative leg (Ni-Al for Type K)
seebeck_neg = tc_k.temperature_to_seebeck_neg_leg(100.0)  # Returns µV/K
print(f"Negative leg Seebeck at 100°C: {seebeck_neg:.3f} µV/K")

# The total Seebeck coefficient is the difference
seebeck_total = seebeck_pos - seebeck_neg  # Should equal tc_k.temperature_to_seebeck(100.0)
print(f"Total Seebeck coefficient: {seebeck_total:.3f} µV/K")
```

## API Reference

### ThermocoupleType Class

```python
class ThermocoupleType:
    def temperature_to_voltage(self, temp_c: float) -> float:
        """Convert temperature (°C) to voltage (V)"""
        
    def voltage_to_temperature(self, voltage: float) -> float:
        """Convert voltage (V) to temperature (°C)"""
        
    def voltage_to_temperature_with_reference(self, voltage: float, ref_temp: float) -> float:
        """Convert voltage (V) to temperature (°C) with cold junction compensation"""
        
    def temperature_to_seebeck(self, temp_c: float) -> float:
        """Calculate Seebeck coefficient (µV/K) at temperature"""
        
    def temperature_to_dsdt(self, temp_c: float) -> float:
        """Calculate dSeebeck/dT (nV/K²) at temperature"""
        
    def temperature_to_volt_pos_leg(self, temp_c: float) -> float:
        """Calculate the thermoelectric voltage of the positive leg at a given temperature."""
        
    def temperature_to_volt_neg_leg(self, temp_c: float) -> float:
        """Calculate the thermoelectric voltage of the negative leg at a given temperature."""
        
    def temperature_to_seebeck_pos_leg(self, temp_c: float) -> float:
        """Calculate the Seebeck coefficient of the positive leg at a given temperature."""
        
    def temperature_to_seebeck_neg_leg(self, temp_c: float) -> float:
        """Calculate the Seebeck coefficient of the negative leg at a given temperature."""
```

## Requirements

- **Python**: 3.9+
- **Dependencies**: None (pure Python implementation)

## Testing

Run the built-in test when installing:

```bash
python -m thermocouples
```

Or run the test with help information:

```bash
python -m thermocouples --help
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

⚠️ **Important**: While this library implements NIST-standard calculations with high precision, users are responsible for validating results for their specific applications. For critical measurements or safety-related applications, please refer directly to NIST Monograph 175 or conduct independent verification.

## Author

**Dipl.-Ing. Gregor Oppitz**  
*Deutsches Zentrum für Luft- und Raumfahrt (DLR)*

---

*If this library helped your project, please consider giving it a ⭐ on GitHub!*
*If this library helped your project, please consider giving it a ⭐ on GitHub!*
