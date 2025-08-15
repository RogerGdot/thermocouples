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
    def _temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Get temperature to microvolt polynomial coefficients."""
        pass

    @property
    @abstractmethod
    def _microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Get microvolt to temperature polynomial coefficients."""
        pass

    @property
    def _temp_to_seebeck_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients."""
        return None

    @property
    def _temp_to_dsdt_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to dSeebeck/dT polynomial coefficients."""
        return None

    @property
    def _temp_to_microvolt_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to microvolt polynomial coefficients for positive leg."""
        return None

    @property
    def _temp_to_microvolt_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to microvolt polynomial coefficients for negative leg."""
        return None

    @property
    def _temp_to_seebeck_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients for positive leg."""
        return None

    @property
    def _temp_to_seebeck_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients for negative leg."""
        return None

    @property
    def _microvolt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for voltage calculation."""
        return None

    @property
    def _seebeck_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for Seebeck coefficient calculation."""
        return None

    @property
    def _dsdt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for dSeebeck/dT calculation."""
        return None

    @property
    def _microvolt_neg_leg_expo_function(self) -> Optional[Callable[[float], float]]:
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

    def temp_to_volt(self, temp_c: float) -> float:
        """
        Convert temperature (°C) to thermoelectric voltage (V).

        This assumes reference junction at 0°C.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Thermoelectric voltage in volts (V)
        """
        # Calculate voltage at measurement temperature (reference = 0°C)
        microvolt = self._find_range_and_evaluate(temp_c, self._temp_to_microvolt_data, self._microvolt_expo_function)
        return microvolt / 1e6  # Convert microvolts to volts

    def volt_to_temp(self, voltage: float) -> float:
        """
        Convert thermoelectric voltage (V) to temperature (°C).

        This assumes reference junction at 0°C.

        Args:
            voltage: Thermoelectric voltage in volts (V)

        Returns:
            Temperature in degrees Celsius
        """
        # Convert to microvolts for calculation
        microvolt = voltage * 1e6

        # Find temperature using inverse polynomial
        return self._find_range_and_evaluate(microvolt, self._microvolt_to_temp_data)

    def volt_to_temp_with_cjc(self, voltage: float, ref_temp: float) -> float:
        """
        Convert measured voltage to temperature with cold junction compensation.

        Args:
            voltage: Measured voltage in volts (V)
            ref_temp: Reference (cold junction) temperature in degrees Celsius

        Returns:
            Actual temperature in degrees Celsius
        """
        ref_voltage = self.temp_to_voltage(ref_temp)
        total_voltage = voltage + ref_voltage
        return self.voltage_to_temp(total_voltage)

    def temp_to_seebeck(self, temp_c: float) -> float:
        """
        Calculate Seebeck coefficient (µV/K) at given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient in microvolts per Kelvin (µV/K)
        """
        if self._temp_to_seebeck_data is None:
            raise NotImplementedError(f"Seebeck coefficient calculation not available for type {self.name}")

        return self._find_range_and_evaluate(temp_c, self._temp_to_seebeck_data, self._seebeck_expo_function)

    def temp_to_dsdt(self, temp_c: float) -> float:
        """
        Calculate dSeebeck/dT (nV/K²) at given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Temperature derivative of Seebeck coefficient in nanovolts per Kelvin squared (nV/K²)
        """
        if self._temp_to_dsdt_data is None:
            raise NotImplementedError(f"dSeebeck/dT calculation not available for type {self.name}")

        result_microvolt_per_k2 = self._find_range_and_evaluate(temp_c, self._temp_to_dsdt_data, self._dsdt_expo_function)
        # Convert µV/K² to nV/K²
        return result_microvolt_per_k2 * 1000.0

    def temp_to_volt_pos_leg(self, temp_c: float) -> float:
        """
        Calculate the thermoelectric voltage of the positive leg at a given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Thermoelectric voltage of positive leg in volts (V)
        """
        if self._temp_to_microvolt_pos_leg_data is None:
            raise NotImplementedError(f"Positive leg voltage calculation not available for type {self.name}")

        microvolt = self._find_range_and_evaluate(temp_c, self._temp_to_microvolt_pos_leg_data)
        return microvolt / 1e6  # Convert microvolts to volts

    def temp_to_volt_neg_leg(self, temp_c: float) -> float:
        """
        Calculate the thermoelectric voltage of the negative leg at a given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Thermoelectric voltage of negative leg in volts (V)
        """
        if self._temp_to_microvolt_neg_leg_data is None:
            raise NotImplementedError(f"Negative leg voltage calculation not available for type {self.name}")

        microvolt = self._find_range_and_evaluate(temp_c, self._temp_to_microvolt_neg_leg_data, self._microvolt_neg_leg_expo_function)
        return microvolt / 1e6  # Convert microvolts to volts

    def temp_to_seebeck_pos_leg(self, temp_c: float) -> float:
        """
        Calculate the Seebeck coefficient of the positive leg at a given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient of positive leg in microvolts per Kelvin (µV/K)
        """
        if self._temp_to_seebeck_pos_leg_data is None:
            raise NotImplementedError(f"Positive leg Seebeck coefficient calculation not available for type {self.name}")

        return self._find_range_and_evaluate(temp_c, self._temp_to_seebeck_pos_leg_data)

    def temp_to_seebeck_neg_leg(self, temp_c: float) -> float:
        """
        Calculate the Seebeck coefficient of the negative leg at a given temperature.

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient of negative leg in microvolts per Kelvin (µV/K)
        """
        if self._temp_to_seebeck_neg_leg_data is None:
            raise NotImplementedError(f"Negative leg Seebeck coefficient calculation not available for type {self.name}")

        return self._find_range_and_evaluate(temp_c, self._temp_to_seebeck_neg_leg_data)
