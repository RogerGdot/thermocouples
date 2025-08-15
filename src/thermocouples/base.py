"""
Abstract base class for thermocouple types.
"""

from abc import ABC, abstractmethod
from typing import Callable, Optional


class Thermocouple(ABC):
    """
    Abstract base class for thermocouple types.

    Supports:
    - Temperature to Voltage (mV)
    - Voltage (mV) to Temperature
    - Temperature to Seebeck coefficient (µV/K)
    - Temperature to dSeebeck/dT (nV/°C²)
    - Direct calculation of temperature from measured voltage and reference temperature
    - Individual leg voltage calculations (positive and negative)
    - Individual leg Seebeck coefficient calculations (positive and negative)
    """

    @property
    def name(self) -> str:
        """Get the thermocouple type name."""
        # This will be overridden by subclasses
        return "Unknown"

    @property
    @abstractmethod
    def temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Get temperature to microvolt polynomial coefficients."""
        pass

    @property
    @abstractmethod
    def microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Get microvolt to temperature polynomial coefficients."""
        pass

    @property
    def temp_to_seebeck_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients."""
        return None

    @property
    def temp_to_dsdt_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to dSeebeck/dT polynomial coefficients."""
        return None

    @property
    def temp_to_microvolt_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to microvolt polynomial coefficients for positive leg."""
        return None

    @property
    def temp_to_microvolt_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to microvolt polynomial coefficients for negative leg."""
        return None

    @property
    def temp_to_seebeck_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients for positive leg."""
        return None

    @property
    def temp_to_seebeck_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients for negative leg."""
        return None

    @property
    def microvolt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for voltage calculation."""
        return None

    @property
    def seebeck_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for Seebeck coefficient calculation."""
        return None

    @property
    def dsdt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for dSeebeck/dT calculation."""
        return None

    @property
    def microvolt_neg_leg_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for negative leg voltage calculation."""
        return None

    def _polynomial_evaluation(self, value: float, coefficients: list[float]) -> float:
        """
        Evaluate polynomial with given coefficients.

        Args:
            value: Input value
            coefficients: Polynomial coefficients [a0, a1, a2, ...]

        Returns:
            Polynomial result: a0 + a1*x + a2*x² + ...
        """
        result = 0.0
        power = 1.0
        for coeff in coefficients:
            result += coeff * power
            power *= value
        return result

    def _find_range_and_evaluate(
        self, value: float, ranges_and_coeffs: list[tuple[tuple[float, float], list[float]]], expo_function: Optional[Callable[[float], float]] = None
    ) -> float:
        """
        Find appropriate range and evaluate polynomial.

        Args:
            value: Input value
            ranges_and_coeffs: List of ((min, max), [coefficients])
            expo_function: Optional exponential correction function

        Returns:
            Polynomial evaluation result

        Raises:
            ValueError: If value is outside all ranges
        """
        for (min_val, max_val), coeffs in ranges_and_coeffs:
            if min_val <= value <= max_val:
                result = self._polynomial_evaluation(value, coeffs)
                if expo_function:
                    result += expo_function(value)
                return result

        raise ValueError(f"Value {value} is outside valid range for thermocouple type {self.name}")

    def temperature_to_voltage(self, temp_c: float, reference_junction_temp: float = 0.0) -> float:
        """
        Convert temperature (°C) to thermoelectric voltage (V).

        Args:
            temp_c: Temperature in degrees Celsius
            reference_junction_temp: Reference junction temperature in degrees Celsius (default: 0.0)

        Returns:
            Thermoelectric voltage in volts (V)
        """
        # Calculate voltage at measurement temperature
        microvolt_meas = self._find_range_and_evaluate(temp_c, self.temp_to_microvolt_data, self.microvolt_expo_function)

        # Calculate voltage at reference junction temperature
        if reference_junction_temp != 0.0:
            microvolt_ref = self._find_range_and_evaluate(reference_junction_temp, self.temp_to_microvolt_data, self.microvolt_expo_function)
        else:
            microvolt_ref = 0.0

        # Return difference (voltage at measurement - voltage at reference)
        return (microvolt_meas - microvolt_ref) / 1e6  # Convert microvolts to volts

    def voltage_to_temperature(self, voltage: float, reference_junction_temp: float = 0.0) -> float:
        """
        Convert thermoelectric voltage (V) to temperature (°C).

        Args:
            voltage: Thermoelectric voltage in volts (V)
            reference_junction_temp: Reference junction temperature in degrees Celsius (default: 0.0)

        Returns:
            Temperature in degrees Celsius
        """
        # Add reference junction compensation
        if reference_junction_temp != 0.0:
            microvolt_ref = self._find_range_and_evaluate(reference_junction_temp, self.temp_to_microvolt_data, self.microvolt_expo_function)
            voltage_compensated = voltage + (microvolt_ref / 1e6)
        else:
            voltage_compensated = voltage

        # Convert to microvolts for calculation
        microvolt = voltage_compensated * 1e6

        # Find temperature using inverse polynomial
        return self._find_range_and_evaluate(microvolt, self.microvolt_to_temp_data)

    def voltage_to_temperature_with_reference(self, voltage: float, ref_temp: float) -> float:
        """
        Convert measured voltage to temperature with cold junction compensation.

        Args:
            voltage: Measured voltage in volts (V)
            ref_temp: Reference (cold junction) temperature in degrees Celsius

        Returns:
            Actual temperature in degrees Celsius
        """
        ref_voltage = self.temperature_to_voltage(ref_temp)
        total_voltage = voltage + ref_voltage
        return self.voltage_to_temperature(total_voltage)

    def temperature_to_seebeck(self, temp_c: float) -> float:
        """
        Calculate Seebeck coefficient (µV/K) at given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient in microvolts per Kelvin (µV/K)
        """
        if self.temp_to_seebeck_data is None:
            raise NotImplementedError(f"Seebeck coefficient calculation not available for type {self.name}")

        return self._find_range_and_evaluate(temp_c, self.temp_to_seebeck_data, self.seebeck_expo_function)

    def temp_to_seebeck(self, temp_c: float) -> float:
        """
        Alias for temperature_to_seebeck for backward compatibility.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient in microvolts per Kelvin (µV/K)
        """
        return self.temperature_to_seebeck(temp_c)

    def temp_to_dsdt(self, temp_c: float) -> float:
        """
        Alias for temperature_to_dsdt for backward compatibility.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Temperature derivative of Seebeck coefficient in nanovolts per Kelvin squared (nV/K²)
        """
        return self.temperature_to_dsdt(temp_c)

    def temperature_to_dsdt(self, temp_c: float) -> float:
        """
        Calculate dSeebeck/dT (nV/K²) at given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Temperature derivative of Seebeck coefficient in nanovolts per Kelvin squared (nV/K²)
        """
        if self.temp_to_dsdt_data is None:
            raise NotImplementedError(f"dSeebeck/dT calculation not available for type {self.name}")

        return self._find_range_and_evaluate(temp_c, self.temp_to_dsdt_data, self.dsdt_expo_function)

    def temperature_to_volt_pos_leg(self, temp_c: float) -> float:
        """
        Calculate the thermoelectric voltage of the positive leg at a given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Thermoelectric voltage of positive leg in volts (V)
        """
        if self.temp_to_microvolt_pos_leg_data is None:
            raise NotImplementedError(f"Positive leg voltage calculation not available for type {self.name}")

        microvolt = self._find_range_and_evaluate(temp_c, self.temp_to_microvolt_pos_leg_data)
        return microvolt / 1e6  # Convert microvolts to volts

    def temperature_to_volt_neg_leg(self, temp_c: float) -> float:
        """
        Calculate the thermoelectric voltage of the negative leg at a given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Thermoelectric voltage of negative leg in volts (V)
        """
        if self.temp_to_microvolt_neg_leg_data is None:
            raise NotImplementedError(f"Negative leg voltage calculation not available for type {self.name}")

        microvolt = self._find_range_and_evaluate(temp_c, self.temp_to_microvolt_neg_leg_data, self.microvolt_neg_leg_expo_function)
        return microvolt / 1e6  # Convert microvolts to volts

    def temperature_to_seebeck_pos_leg(self, temp_c: float) -> float:
        """
        Calculate the Seebeck coefficient of the positive leg at a given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient of positive leg in microvolts per Kelvin (µV/K)
        """
        if self.temp_to_seebeck_pos_leg_data is None:
            raise NotImplementedError(f"Positive leg Seebeck coefficient calculation not available for type {self.name}")

        return self._find_range_and_evaluate(temp_c, self.temp_to_seebeck_pos_leg_data)

    def temperature_to_seebeck_neg_leg(self, temp_c: float) -> float:
        """
        Calculate the Seebeck coefficient of the negative leg at a given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient of negative leg in microvolts per Kelvin (µV/K)
        """
        if self.temp_to_seebeck_neg_leg_data is None:
            raise NotImplementedError(f"Negative leg Seebeck coefficient calculation not available for type {self.name}")

        return self._find_range_and_evaluate(temp_c, self.temp_to_seebeck_neg_leg_data)
