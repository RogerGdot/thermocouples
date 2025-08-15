"""
Basic tests for the thermocouples package.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from thermocouples import get_thermocouple, temperature_to_voltage, voltage_to_temperature


def test_type_k_basic():
    """Test basic Type K thermocouple conversion."""
    tc_k = get_thermocouple("K")

    # Test known values (approximately)
    temp = 100.0  # °C
    voltage = tc_k.temperature_to_voltage(temp)
    temp_back = tc_k.voltage_to_temperature(voltage)

    # Should round-trip within reasonable tolerance
    assert abs(temp - temp_back) < 0.1, f"Round-trip failed: {temp} != {temp_back}"


def test_convenience_functions():
    """Test convenience functions."""
    temp = 100.0
    voltage = temperature_to_voltage("K", temp)
    temp_back = voltage_to_temperature("K", voltage)

    assert abs(temp - temp_back) < 0.1, "Convenience function round-trip failed"


def test_all_types_available():
    """Test that all thermocouple types are available."""
    expected_types = ["B", "E", "J", "K", "N", "R", "S", "T"]

    for tc_type in expected_types:
        tc = get_thermocouple(tc_type)
        assert tc is not None, f"Type {tc_type} not available"


def test_cold_junction_compensation():
    """Test cold junction compensation."""
    tc_k = get_thermocouple("K")

    # Test with known values
    measured_voltage = 0.025  # V
    ref_temp = 25.0  # °C

    # Should not raise an exception
    actual_temp = tc_k.voltage_to_temperature_with_reference(measured_voltage, ref_temp)
    assert isinstance(actual_temp, (int, float)), "Temperature should be numeric"


def test_seebeck_coefficients():
    """Test Seebeck coefficient calculations."""
    tc_k = get_thermocouple("K")

    # Test Seebeck coefficient at 100°C
    seebeck = tc_k.temperature_to_seebeck(100.0)
    assert isinstance(seebeck, (int, float)), "Seebeck should be numeric"
    assert 30 < seebeck < 50, f"Seebeck coefficient seems unreasonable: {seebeck}"

    # Test dSeebeck/dT
    dsdt = tc_k.temperature_to_dsdt(100.0)
    assert isinstance(dsdt, (int, float)), "dS/dT should be numeric"


def test_modular_structure():
    """Test that the modular structure works correctly."""
    # Test that we can access different thermocouple types
    types_to_test = ["K", "J", "T", "E", "N"]

    for tc_type in types_to_test:
        tc = get_thermocouple(tc_type)

        # Test basic conversion at room temperature
        temp = 25.0
        voltage = tc.temperature_to_voltage(temp)
        temp_back = tc.voltage_to_temperature(voltage)

        assert abs(temp - temp_back) < 0.1, f"Type {tc_type} round-trip failed"

        # Test that the thermocouple has the expected name
        assert tc.name == tc_type, f"Name mismatch for type {tc_type}"


def test_high_temperature_types():
    """Test high-temperature thermocouple types (B, R, S)."""
    high_temp_types = ["B", "R", "S"]

    for tc_type in high_temp_types:
        tc = get_thermocouple(tc_type)

        # Test at higher temperature (B type doesn't work well below 250°C)
        temp = 500.0 if tc_type == "B" else 200.0
        voltage = tc.temperature_to_voltage(temp)
        temp_back = tc.voltage_to_temperature(voltage)

        assert abs(temp - temp_back) < 0.5, f"Type {tc_type} high-temp round-trip failed"


if __name__ == "__main__":
    test_type_k_basic()
    test_convenience_functions()
    test_all_types_available()
    test_cold_junction_compensation()
    test_seebeck_coefficients()
    test_modular_structure()
    test_high_temperature_types()
    print("All tests passed!")
