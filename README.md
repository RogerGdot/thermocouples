# Python Thermocouples

[![PyPI version](https://badge.fury.io/py/thermocouples.svg)](https://badge.fury.io/py/thermocouples)
[![Python](https://img.shields.io/pypi/pyversions/thermocouples.svg)](https://pypi.org/project/thermocouples/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, high-accuracy thermocouple calculation library for Python, implementing all standard thermocouple types with NIST-compliant polynomial calculations.

## Features

✅ **Complete NIST Implementation**: All polynomial coefficients from NIST Monograph 175  
✅ **All Standard Types**: B, E, J, K, N, R, S, T thermocouples  
✅ **Modular Architecture**: Each thermocouple type in separate module for maintainability  
✅ **Bidirectional Conversion**: Temperature ↔ Voltage  
✅ **Seebeck Coefficients**: Calculate sensitivity (µV/K)  
✅ **Cold Junction Compensation**: Automatic reference junction correction  
✅ **Individual Leg Support**: Separate positive/negative leg calculations  
✅ **High Precision**: NIST-grade accuracy for scientific applications  

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

```python
# For thermocouples with individual leg data (Types E, J, K, N, T)
tc_k = get_thermocouple("K")

# Positive leg (Ni-Cr)
v_pos = tc_k.temperature_to_voltage_positive_leg(100.0)

# Negative leg (Ni-Al) 
v_neg = tc_k.temperature_to_voltage_negative_leg(100.0)

# The thermocouple voltage is the difference
v_total = v_pos - v_neg  # Should equal tc_k.temperature_to_voltage(100.0)
```

### Available Functions

```python
from thermocouples import (
    get_thermocouple,           # Get thermocouple instance
    temperature_to_voltage,     # Direct T→V conversion
    voltage_to_temperature,     # Direct V→T conversion
    voltage_to_temperature_with_reference,  # With cold junction compensation
    temp_to_seebeck,           # Temperature to Seebeck coefficient
    temp_to_dsdt,              # Temperature to dSeebeck/dT
    THERMOCOUPLE_TYPES,        # Dictionary of all available types
)
```

## Data Source & Accuracy

All polynomial coefficients and equations are based on:

**NIST Monograph 175**: *"Temperature-Electromotive Force Reference Functions and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90"*

- 📖 [Official NIST Publication](https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf)
- 🎯 **Accuracy**: Matches NIST reference tables to measurement precision
- ✅ **Validation**: Coefficients verified using AI-assisted validation
- 📐 **Standards**: ITS-90 temperature scale compliant

## Use Cases

- **Laboratory Instrumentation**: High-precision temperature measurements
- **Industrial Process Control**: Temperature monitoring and control systems
- **Research & Development**: Thermal analysis and calibration
- **Data Acquisition**: Convert raw thermocouple voltages to temperatures
- **Sensor Calibration**: Validate thermocouple measurement systems
- **Educational**: Learn thermocouple physics and calculations

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
