# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.1] - 2025-08-16

### Fixed
- **Bugfix**: Corrected `temp_to_dsdt()` method calculation for accurate Seebeck coefficient derivative computation
- Improved numerical stability in temperature derivative calculations
- Enhanced accuracy for all thermocouple types in sensitivity analysis

### Documentation
- Updated README to properly showcase `volt_to_temp_with_cjc()` cold junction compensation method
- Clarified API documentation with accurate method examples
- Added comprehensive cold junction compensation usage examples

## [2.1.0] - 2025-08-15

### Changed
- **BREAKING**: Complete API cleanup - removed all legacy function-based APIs
- **Professional Design**: All internal implementation details now hidden with underscore prefixes
- **Simplified Methods**: Shortened function names for better usability:
  - `temperature_to_voltage()` → `temp_to_volt()`
  - `voltage_to_temperature()` → `volt_to_temp()`
  - `temperature_to_seebeck()` → `temp_to_seebeck()`
  - `temperature_to_dsdt()` → `temp_to_dsdt()`
- **Clean Interface**: Only user-relevant methods visible in IDE autocomplete
- **Hidden Properties**: All internal data properties now prefixed with underscore:
  - `temp_to_microvolt_data` → `_temp_to_microvolt_data`
  - `microvolt_to_temp_data` → `_microvolt_to_temp_data`
  - `expo_functions` → `_expo_functions`

### Removed
- All legacy function-based APIs (`temp_to_voltage`, `voltage_to_temp`, etc.)
- `get_available_types()` function - use factory pattern instead
- Public access to internal implementation properties

### Added
- Professional API documentation with clean examples
- Comprehensive type hints throughout the codebase
- Better IDE support with hidden implementation details

## [2.0.1] - 2025-08-15

### Fixed
- Package metadata and PyPI publishing setup
- GitHub Actions workflow for automated releases

## [2.0.0] - 2025-08-15

### Added
- Complete object-oriented architecture redesign
- Abstract base class `Thermocouple` with common calculation logic
- Factory pattern with `get_thermocouple()` function
- Individual thermocouple type classes (TypeK, TypeB, TypeE, etc.)
- Full type hints throughout the codebase
- Comprehensive test suite
- GitHub Actions for automated PyPI publishing

### Changed
- **BREAKING**: Primary API is now object-oriented
- Improved code organization with separate type classes
- Better maintainability and extensibility

### Deprecated
- Function-based APIs (maintained for backward compatibility)

## [1.0.0] - Previous

### Added
- Initial implementation with function-based API
- Support for all standard thermocouple types (B, E, J, K, N, R, S, T)
- NIST-compliant polynomial calculations
- Temperature to voltage conversion
- Voltage to temperature conversion
- Seebeck coefficient calculations
