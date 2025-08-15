# Thermocouples

[![PyPI version](https://badge.fury.io/py/thermocouples.svg)](https://badge.fury.io/py/thermocouples)
[![Python](https://img.shields.io/pypi/pyversions/thermocouples.svg)](https://pypi.org/project/thermocouples/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, high-accuracy thermocouple calculation library for Python with clean object-oriented architecture and professional API design that hides implementation details.

## Features

- **🎯 Temperature to Voltage Conversion**: Convert temperature (°C) to thermoelectric voltage (V)
- **🌡️ Voltage to Temperature Conversion**: Convert voltage (V) to temperature (°C)
- **📊 Seebeck Coefficient Calculation**: Get the Seebeck coefficient (µV/K) at any temperature
- **📈 Temperature Derivative of Seebeck**: Calculate dSeebeck/dT (nV/K²) for advanced analysis
- **❄️ Cold Junction Compensation**: Built-in `volt_to_temp_with_cjc()` method for reference junction temperature compensation
- **🔬 Individual Thermocouple Leg Calculations**: 
  - Voltage calculations for positive and negative legs separately
  - Seebeck coefficient calculations for positive and negative legs separately
- **🎯 High Accuracy**: Based on NIST Monograph 175 polynomial coefficients
- **✅ All Standard Types**: Supports B, E, J, K, N, R, S, and T type thermocouples
- **🐍 Pure Python**: No external dependencies required
- **🏗️ Modern OOP Architecture**: Clean, maintainable object-oriented design
- **🧪 Well Tested**: Comprehensive test suite ensuring accuracy
- **📚 Type Safe**: Full type hints for better IDE support

## What's New in Version 2.1

**🧹 Professional API Cleanup:**
- **Clean Interface**: All internal implementation details hidden with underscore prefixes
- **IDE-Friendly**: Only user-relevant methods visible in autocomplete
- **Simplified Functions**: Shortened method names (`temp_to_volt` vs `temperature_to_voltage`)
- **Pure OOP Design**: Complete removal of legacy function-based API
- **Professional Standards**: Following Python best practices for library design

## Supported Thermocouple Types

| Type | Temperature Range | Materials | Application |
|------|------------------|-----------|-------------|
| **B** | 0°C to 1820°C | Pt-30%Rh / Pt-6%Rh | Ultra-high temperature |
| **E** | -270°C to 1000°C | Ni-Cr / Cu-Ni | Highest sensitivity |
| **K** | -270°C to 1372°C | Ni-Cr / Ni-Al | Most popular, general purpose |
| **N** | -270°C to 1300°C | Ni-Cr-Si / Ni-Si | Improved K-type |
| **R** | -50°C to 1768°C | Pt-13%Rh / Pt | High temperature, precious metal |
| **S** | -50°C to 1768°C | Pt-10%Rh / Pt | High temperature, precious metal |
| **T** | -270°C to 400°C | Cu / Cu-Ni | Cryogenic applications |

## Quick Start

### Installation

```bash
pip install thermocouples
```

### Basic Usage (New OOP API - Recommended)

```python
import thermocouples as tc

# Create thermocouple instance
tc_k = tc.get_thermocouple("K")

# Temperature to voltage conversion
voltage = tc_k.temp_to_volt(100.0)  # 4.096 mV at 100°C
print(f"K-type at 100°C: {voltage:.3f} mV")

# Voltage to temperature conversion  
temperature = tc_k.volt_to_temp(0.004096)  # Back to ~100°C
print(f"K-type at 4.096 mV: {temperature:.1f}°C")

# Seebeck coefficient calculation
seebeck = tc_k.temp_to_seebeck(100.0)  # µV/K
print(f"Seebeck coefficient at 100°C: {seebeck:.1f} µV/K")
```

### Advanced Usage

```python
import thermocouples as tc

# Get a thermocouple instance
tc_k = tc.get_thermocouple("K")

# High-precision calculations
voltage = tc_k.temp_to_volt(200.5)
seebeck = tc_k.temp_to_seebeck(200.5)  # Seebeck coefficient
dsdt = tc_k.temp_to_dsdt(200.5)        # Temperature derivative

# Cold junction compensation
hot_junction_temp = 500.0  # °C
cold_junction_temp = 25.0   # °C (room temperature)

# Method 1: Built-in Cold Junction Compensation (Recommended)
measured_voltage = 0.019665  # V (voltage measured by your instrument)
actual_temp = tc_k.volt_to_temp_with_cjc(measured_voltage, cold_junction_temp)
print(f"Actual temperature: {actual_temp:.1f}°C")

# Method 2: Manual calculation (for understanding)
voltage_hot = tc_k.temp_to_volt(hot_junction_temp)
voltage_cold = tc_k.temp_to_volt(cold_junction_temp)
expected_measurement = voltage_hot - voltage_cold
print(f"Expected measured voltage: {expected_measurement:.6f} V")

# Verify with built-in CJC function
calculated_temp = tc_k.volt_to_temp_with_cjc(expected_measurement, cold_junction_temp)
print(f"Calculated temperature: {calculated_temp:.1f}°C")

# Individual thermocouple leg analysis
tc_e = tc.get_thermocouple("E")

# Positive leg (Ni-Cr) calculations
pos_voltage = tc_e.temp_to_volt_pos_leg(300.0)
pos_seebeck = tc_e.temp_to_seebeck_pos_leg(300.0)

# Negative leg (Cu-Ni) calculations  
neg_voltage = tc_e.temp_to_volt_neg_leg(300.0)
neg_seebeck = tc_e.temp_to_seebeck_neg_leg(300.0)

print(f"E-type at 300°C:")
print(f"  Positive leg: {pos_voltage:.6f} V, {pos_seebeck:.3f} µV/K")
print(f"  Negative leg: {neg_voltage:.6f} V, {neg_seebeck:.3f} µV/K")
print(f"  Difference:   {pos_voltage - neg_voltage:.6f} V")
```

### Working with Multiple Types

```python
import thermocouples as tc

# Compare different thermocouple types at the same temperature
temperature = 400.0  # °C
types = ["B", "E", "J", "K", "N", "R", "S", "T"]

print(f"Voltages at {temperature}°C:")
for tc_type in types:
    if tc_type == "B" and temperature < 250:
        continue  # B-type has limited range at low temperatures
    
    thermocouple = tc.get_thermocouple(tc_type)
    voltage = thermocouple.temp_to_volt(temperature)
    seebeck = thermocouple.temp_to_seebeck(temperature)
    print(f"  Type {tc_type}: {voltage:.6f} V (Seebeck: {seebeck:.1f} µV/K)")
```

## Architecture Overview

**Version 2.0** features a clean object-oriented architecture:

```
thermocouples/
├── base.py              # Abstract base class with common calculation logic
├── registry.py          # Factory functions for creating thermocouple instances  
├── types/
│   ├── type_b_class.py  # B-type thermocouple implementation
│   ├── type_e_class.py  # E-type thermocouple implementation
│   ├── type_j_class.py  # J-type thermocouple implementation
│   ├── type_k_class.py  # K-type thermocouple implementation
│   ├── type_n_class.py  # N-type thermocouple implementation
│   ├── type_r_class.py  # R-type thermocouple implementation
│   ├── type_s_class.py  # S-type thermocouple implementation
│   └── type_t_class.py  # T-type thermocouple implementation
└── __init__.py          # Public API with backward compatibility
```

Each thermocouple type inherits from the abstract `Thermocouple` base class, ensuring:
- **Consistent Interface**: All types support the same methods
- **Code Reuse**: Common calculation logic is shared
- **Type Safety**: Full Python type hints throughout
- **Extensibility**: Adding new types is straightforward

## API Reference

### Factory Functions

- `get_thermocouple(tc_type: str) -> Thermocouple`: Get a thermocouple instance

### Thermocouple Class Methods

Each thermocouple instance provides:

#### Core Conversion Methods
- `temp_to_volt(temperature: float) -> float`
- `volt_to_temp(voltage: float) -> float`
- `volt_to_temp_with_cjc(voltage: float, ref_temp: float) -> float`
- `temp_to_seebeck(temperature: float) -> float` 
- `temp_to_dsdt(temperature: float) -> float`

#### Individual Leg Methods
- `temp_to_volt_pos_leg(temperature: float) -> float`
- `temp_to_volt_neg_leg(temperature: float) -> float`
- `temp_to_seebeck_pos_leg(temperature: float) -> float`
- `temp_to_seebeck_neg_leg(temperature: float) -> float`

#### Properties
- `name: str` - Thermocouple type identifier (e.g., "Type K")

## Requirements

- **Python**: 3.9+
- **Dependencies**: None (pure Python implementation)

## Accuracy and Validation

This library implements the official NIST ITS-90 thermocouple equations from **NIST Monograph 175** with rigorous precision:

- **Temperature-to-Voltage**: Polynomial evaluation using NIST coefficients
- **Voltage-to-Temperature**: Iterative solution with Newton-Raphson method
- **Individual Leg Calculations**: Separate positive and negative leg polynomials
- **Exponential Corrections**: Applied for specific types (K, N) where required
- **High Precision**: Maintains accuracy within NIST tolerance specifications

### Temperature Ranges by Type

| Type | Lower Limit | Upper Limit | Note |
|------|-------------|-------------|------|
| B | 0°C | 1820°C | Limited accuracy below 250°C |
| E | -270°C | 1000°C | Highest sensitivity of all types |
| J | -210°C | 1200°C | Iron oxidizes above 750°C in air |
| K | -270°C | 1372°C | Most common general-purpose type |
| N | -270°C | 1300°C | Improved drift characteristics vs. K |
| R | -50°C | 1768°C | Precious metal, high temperature |
| S | -50°C | 1768°C | Precious metal, similar to R |
| T | -270°C | 400°C | Excellent for cryogenic applications |

## Installation & Testing

### Install from PyPI

```bash
pip install thermocouples
```

### Run Built-in Tests

```bash
# Quick validation test
python -c "import thermocouples as tc; print('✓ Library loaded successfully')"

# Compare multiple types
python -c "
import thermocouples as tc
for t in ['K', 'J', 'T']:
    tc_obj = tc.get_thermocouple(t)
    v = tc_obj.temp_to_volt(100.0)
    print(f'Type {t}: {v:.6f} V at 100°C')
"
```

## Migration Guide

**Version 2.1 uses a clean OOP-only API**. Here's how to use the new simplified interface:

```python
# Modern API (clean, professional)
import thermocouples as tc
tc_k = tc.get_thermocouple("K")
voltage = tc_k.temp_to_volt(100.0)
temperature = tc_k.volt_to_temp(0.004096)
```

The clean OOP approach offers:
- **Better Performance**: Instantiate once, use many times
- **Type Safety**: Full Python type hints
- **IDE Support**: Only relevant methods visible in autocomplete
- **Code Clarity**: Professional object-oriented interface
- **Clean Design**: Implementation details hidden from user view

## Contributors

- **Version 2.1 Architecture** - *Clean API with hidden implementation details*

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Areas for contribution:
- Additional thermocouple types (C, G, M, etc.)
- Performance optimizations
- Enhanced documentation
- Test coverage improvements

## Disclaimer

⚠️ **Important**: While this library implements NIST-standard calculations with high precision, users are responsible for validating results for their specific applications. For critical measurements or safety-related applications, please refer directly to NIST Monograph 175 or conduct independent verification.

---

*If this library helped your project, please consider giving it a ⭐ on GitHub!*
