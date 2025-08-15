# Python Thermocouples v2.0

[![PyPI version](https://badge.fury.io/py/python-thermocouples.svg)](https://badge.fury.io/py/python-thermocouples)
[![Python](https://img.shields.io/pypi/pyversions/python-thermocouples.svg)](https://pypi.org/project/python-thermocouples/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/RogerGdot/thermocouples/actions/workflows/tests.yml/badge.svg)](https://github.com/RogerGdot/thermocouples/actions/workflows/tests.yml)

A comprehensive, high-accuracy thermocouple calculation library for Python, implementing all standard thermocouple types with NIST-compliant polynomial calculations using modern object-oriented architecture.

## Features

- **🎯 Temperature to Voltage Conversion**: Convert temperature (°C) to thermoelectric voltage (V)
- **🌡️ Voltage to Temperature Conversion**: Convert voltage (V) to temperature (°C)
- **📊 Seebeck Coefficient Calculation**: Get the Seebeck coefficient (µV/K) at any temperature
- **📈 Temperature Derivative of Seebeck**: Calculate dSeebeck/dT (nV/K²) for advanced analysis
- **❄️ Cold Junction Compensation**: Built-in support for reference junction temperature compensation
- **🔬 Individual Thermocouple Leg Calculations**: 
  - Voltage calculations for positive and negative legs separately
  - Seebeck coefficient calculations for positive and negative legs separately
- **🎯 High Accuracy**: Based on NIST Monograph 175 polynomial coefficients
- **✅ All Standard Types**: Supports B, E, J, K, N, R, S, and T type thermocouples
- **🐍 Pure Python**: No external dependencies required
- **🏗️ Modern OOP Architecture**: Clean, maintainable object-oriented design
- **🧪 Well Tested**: Comprehensive test suite ensuring accuracy
- **📚 Type Safe**: Full type hints for better IDE support

## What's New in Version 2.0

**🚀 Complete Architectural Redesign:**
- **Object-Oriented Design**: Each thermocouple type is now a class inheriting from an abstract base class
- **Factory Pattern**: Simple `get_thermocouple("K")` function for easy instantiation
- **Type Safety**: Full Python type hints throughout the codebase
- **Better Maintainability**: Cleaner code structure makes adding new types trivial
- **100% Backward Compatibility**: All existing APIs continue to work identically

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
pip install python-thermocouples
```

### Basic Usage (New OOP API - Recommended)

```python
import thermocouples as tc

# Create thermocouple instance
tc_k = tc.get_thermocouple("K")

# Temperature to voltage conversion
voltage = tc_k.temperature_to_voltage(100.0)  # 4.096 mV at 100°C
print(f"K-type at 100°C: {voltage:.3f} mV")

# Voltage to temperature conversion  
temperature = tc_k.voltage_to_temperature(0.004096)  # Back to ~100°C
print(f"K-type at 4.096 mV: {temperature:.1f}°C")

# Seebeck coefficient calculation
seebeck = tc_k.temp_to_seebeck(100.0)  # µV/K
print(f"Seebeck coefficient at 100°C: {seebeck:.1f} µV/K")
```

### Legacy API (Backward Compatible)

```python
import thermocouples as tc

# All original functions still work exactly the same
voltage = tc.temp_to_voltage(100.0, "K")
temperature = tc.voltage_to_temp(0.004096, "K")
seebeck = tc.temp_to_seebeck(100.0, "K")
```

### Advanced Usage

```python
import thermocouples as tc

# Get a thermocouple instance
tc_k = tc.get_thermocouple("K")

# High-precision calculations
voltage = tc_k.temperature_to_voltage(200.5)
seebeck = tc_k.temp_to_seebeck(200.5)  # Seebeck coefficient
dsdt = tc_k.temp_to_dsdt(200.5)        # Temperature derivative

# Cold junction compensation
hot_junction_temp = 500.0  # °C
cold_junction_temp = 25.0   # °C (room temperature)

# Calculate voltage with cold junction at 25°C instead of 0°C
voltage_hot = tc_k.temperature_to_voltage(hot_junction_temp)
voltage_cold = tc_k.temperature_to_voltage(cold_junction_temp)
actual_voltage = voltage_hot - voltage_cold
print(f"Actual measured voltage: {actual_voltage:.6f} V")

# Individual thermocouple leg analysis
tc_e = tc.get_thermocouple("E")

# Positive leg (Ni-Cr) calculations
pos_voltage = tc_e.pos_temp_to_voltage(300.0)
pos_seebeck = tc_e.pos_temp_to_seebeck(300.0)

# Negative leg (Cu-Ni) calculations  
neg_voltage = tc_e.neg_temp_to_voltage(300.0)
neg_seebeck = tc_e.neg_temp_to_seebeck(300.0)

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
    voltage = thermocouple.temperature_to_voltage(temperature)
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
- `get_available_types() -> List[str]`: List all supported thermocouple types

### Legacy Functions (maintained for backward compatibility)

- `temp_to_voltage(temperature: float, tc_type: str, cold_junction: float = 0.0) -> float`
- `voltage_to_temp(voltage: float, tc_type: str, cold_junction: float = 0.0) -> float`  
- `temp_to_seebeck(temperature: float, tc_type: str) -> float`
- `temp_to_dsdt(temperature: float, tc_type: str) -> float`

### Thermocouple Class Methods

Each thermocouple instance provides:

#### Core Conversion Methods
- `temperature_to_voltage(temperature: float) -> float`
- `voltage_to_temperature(voltage: float) -> float`
- `temp_to_seebeck(temperature: float) -> float` 
- `temp_to_dsdt(temperature: float) -> float`

#### Individual Leg Methods
- `pos_temp_to_voltage(temperature: float) -> float`
- `neg_temp_to_voltage(temperature: float) -> float`
- `pos_temp_to_seebeck(temperature: float) -> float`
- `neg_temp_to_seebeck(temperature: float) -> float`

#### Properties
- `tc_type: str` - Thermocouple type identifier
- `temperature_range: Tuple[float, float]` - Valid temperature range
- `pos_material: str` - Positive leg material composition
- `neg_material: str` - Negative leg material composition

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
    v = tc_obj.temperature_to_voltage(100.0)
    print(f'Type {t}: {v:.6f} V at 100°C')
"
```

## Migration from Version 1.x

**Version 2.0 is 100% backward compatible**. Existing code will continue to work without changes:

```python
# Old API (still works)
import thermocouples as tc
voltage = tc.temp_to_voltage(100.0, "K")
temperature = tc.voltage_to_temp(0.004096, "K")

# New API (recommended)
import thermocouples as tc
tc_k = tc.get_thermocouple("K")
voltage = tc_k.temperature_to_voltage(100.0)
temperature = tc_k.voltage_to_temperature(0.004096)
```

The new OOP approach offers:
- **Better Performance**: Instantiate once, use many times
- **Type Safety**: Full Python type hints
- **IDE Support**: Better autocomplete and error detection
- **Code Clarity**: More intuitive object-oriented interface

## Contributors

- **Dipl.-Ing. Gregor Oppitz** - *Original Author*  
  *Deutsches Zentrum für Luft- und Raumfahrt (DLR)*
- **Version 2.0 Architecture** - *Complete OOP refactoring*

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
