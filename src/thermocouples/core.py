"""
Core thermocouple calculation engine.
Contains the main ThermocoupleType class with all calculation methods.
"""


class ThermocoupleType:
    """
    Represents a thermocouple type with all relevant polynomials and conversion methods.

    Supports:
    - Temperature to Voltage (mV)
    - Voltage (mV) to Temperature
    - Temperature to Seebeck coefficient (µV/K)
    - Temperature to dSeebeck/dT (nV/°C²)
    - Direct calculation of temperature from measured voltage and reference temperature
    - Individual leg voltage calculations (positive and negative)
    - Individual leg Seebeck coefficient calculations (positive and negative)
    """

    def __init__(
        self,
        name: str,
        temp_to_microvolt: list[tuple[tuple[float, float], list[float]]],
        microvolt_to_temp: list[tuple[tuple[float, float], list[float]]],
        temp_to_seebeck: list[tuple[tuple[float, float], list[float]]] = None,
        temp_to_dsdt: list[tuple[tuple[float, float], list[float]]] = None,
        temp_to_microvolt_pos_leg: list[tuple[tuple[float, float], list[float]]] = None,
        temp_to_microvolt_neg_leg: list[tuple[tuple[float, float], list[float]]] = None,
        temp_to_seebeck_pos_leg: list[tuple[tuple[float, float], list[float]]] = None,
        temp_to_seebeck_neg_leg: list[tuple[tuple[float, float], list[float]]] = None,
        microvolt_expo_function=None,
        seebeck_expo_function=None,
        dsdt_expo_function=None,
        microvolt_neg_leg_expo_function=None,
    ):
        """
        Initialize thermocouple type with polynomial coefficients.

        Args:
            name: Thermocouple type name (e.g., 'K', 'J', 'T')
            temp_to_microvolt: List of ((temp_min, temp_max), [coefficients]) for T→µV conversion
            microvolt_to_temp: List of ((µv_min, µv_max), [coefficients]) for µV→T conversion
            temp_to_seebeck: Optional list for Seebeck coefficient calculation
            temp_to_dsdt: Optional list for dSeebeck/dT calculation
            special_function: Optional special function for complex calculations (e.g., Type K)
            seebeck_special_function: Optional special function for Seebeck coefficient calculations
            dseebeck_special_function: Optional special function for dSeebeck/dT calculations
        """
        self._name = name
        self._temp_to_microvolt = temp_to_microvolt
        self._microvolt_to_temp = microvolt_to_temp
        self._temp_to_seebeck = temp_to_seebeck or []
        self._temp_to_dsdt = temp_to_dsdt or []
        self._temp_to_microvolt_pos_leg = temp_to_microvolt_pos_leg
        self._temp_to_microvolt_neg_leg = temp_to_microvolt_neg_leg
        self._temp_to_seebeck_pos_leg = temp_to_seebeck_pos_leg
        self._temp_to_seebeck_neg_leg = temp_to_seebeck_neg_leg
        self._microvolt_expo_function = microvolt_expo_function
        self._seebeck_expo_function = seebeck_expo_function
        self._dsdt_expo_function = dsdt_expo_function
        self._microvolt_neg_leg_expo_function = microvolt_neg_leg_expo_function

    def _select_coeffs(self, x: float, tables: list[tuple[tuple[float, float], list[float]]]) -> list[float]:
        """Select appropriate polynomial coefficients based on input value."""
        for (lo, hi), coeffs in tables:
            if lo <= x <= hi:
                return coeffs
        raise ValueError(f"Value {x} out of range for Type {self._name} thermocouple")

    def _polyval(self, coeffs: list[float], x: float) -> float:
        """Evaluate polynomial with given coefficients."""
        return sum(c * (x**i) for i, c in enumerate(coeffs))

    def temperature_to_voltage(self, temp_c: float) -> float:
        """
        Convert temperature (°C) to thermoelectric voltage (V).

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Thermoelectric voltage in volts (V)
        """
        coeffs = self._select_coeffs(temp_c, self._temp_to_microvolt)
        result = self._polyval(coeffs, temp_c)

        # Apply special function if available (e.g., Type K exponential term)
        if self._microvolt_expo_function:
            result += self._microvolt_expo_function(temp_c)

        return result / 1e6  # Convert µV to V (SI unit)

    def voltage_to_temperature(self, v: float) -> float:
        """
        Convert thermoelectric voltage (V) to temperature (°C).

        Args:
            v: Thermoelectric voltage in volts

        Returns:
            Temperature in degrees Celsius
        """
        microvolt = v * 1e6  # Convert V to µV
        coeffs = self._select_coeffs(microvolt, self._microvolt_to_temp)
        result = self._polyval(coeffs, microvolt)

        return result

    def temperature_to_seebeck(self, temp_c: float) -> float:
        """
        Calculate the Seebeck coefficient (µV/K) at a given temperature (°C).

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient in µV/K
        """
        if not self._temp_to_seebeck:
            raise NotImplementedError(f"Seebeck coefficient not implemented for Type {self._name}")

        coeffs = self._select_coeffs(temp_c, self._temp_to_seebeck)
        result = self._polyval(coeffs, temp_c)

        # Apply special seebeck function if available (e.g., Type K exponential term)
        if self._seebeck_expo_function:
            result += self._seebeck_expo_function(temp_c)

        return result

    def temperature_to_dsdt(self, temp_c: float) -> float:
        """
        Calculate the temperature derivative of the Seebeck coefficient (nV/K²) at a given temperature (°C).

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            dSeebeck/dT in nV/K²
        """
        if not self._temp_to_dsdt:
            raise NotImplementedError(f"dSeebeck/dT not implemented for Type {self._name}")

        coeffs = self._select_coeffs(temp_c, self._temp_to_dsdt)
        result = self._polyval(coeffs, temp_c)

        # Apply special dsdt function if available (e.g., Type K exponential term)
        if self._dsdt_expo_function:
            result += self._dsdt_expo_function(temp_c)

        return result

    def temperature_to_volt_pos_leg(self, temp_c: float) -> float:
        """
        Calculate the thermovoltage (V) of the positive leg at a given temperature (°C).

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Thermovoltage positive leg in Volts (SI unit)
        """
        if not self._temp_to_microvolt_pos_leg:
            raise NotImplementedError(f"Thermovoltage positive leg not implemented for Type {self._name}")

        coeffs = self._select_coeffs(temp_c, self._temp_to_microvolt_pos_leg)
        result = self._polyval(coeffs, temp_c)

        return result / 1e6  # Convert µV to V (SI unit)

    def temperature_to_volt_neg_leg(self, temp_c: float) -> float:
        """
        Calculate the thermovoltage (V) of the negative leg at a given temperature (°C).

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Thermovoltage negative leg in Volts (SI unit)
        """
        if not self._temp_to_microvolt_neg_leg:
            raise NotImplementedError(f"Thermovoltage negative leg not implemented for Type {self._name}")

        coeffs = self._select_coeffs(temp_c, self._temp_to_microvolt_neg_leg)
        result = self._polyval(coeffs, temp_c)

        # Apply special volt_neg_leg function if available (e.g., Type K exponential term)
        if self._microvolt_neg_leg_expo_function:
            result += self._microvolt_neg_leg_expo_function(temp_c)

        # Convert µV to V (SI unit)
        return result / 1e6

    def temperature_to_seebeck_pos_leg(self, temp_c: float) -> float:
        """
        Calculate the Seebeck coefficient (µV/K) of the positive leg at a given temperature (°C).

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient positive leg in µV/K
        """
        if not self._temp_to_seebeck_pos_leg:
            raise NotImplementedError(f"Seebeck coefficient positive leg not implemented for Type {self._name}")

        coeffs = self._select_coeffs(temp_c, self._temp_to_seebeck_pos_leg)
        result = self._polyval(coeffs, temp_c)

        return result

    def temperature_to_seebeck_neg_leg(self, temp_c: float) -> float:
        """
        Calculate the Seebeck coefficient (µV/K) of the negative leg at a given temperature (°C).

        Args:
            temp_c: Temperature in degrees Celsius

        Returns:
            Seebeck coefficient negative leg in µV/K
        """
        if not self._temp_to_seebeck_neg_leg:
            raise NotImplementedError(f"Seebeck coefficient negative leg not implemented for Type {self._name}")

        coeffs = self._select_coeffs(temp_c, self._temp_to_seebeck_neg_leg)
        result = self._polyval(coeffs, temp_c)

        return result

    def voltage_to_temperature_with_reference(self, v_measured: float, t_ref: float) -> float:
        """
        Convert measured thermoelectric voltage (V) and reference temperature (°C) to actual temperature (°C).
        This uses cold-junction compensation.

        Args:
            v_measured: Measured thermoelectric voltage in Volts
            t_ref: Reference junction temperature in degrees Celsius

        Returns:
            Actual temperature in degrees Celsius
        """
        v_ref = self.temperature_to_voltage(t_ref)
        v_total = v_measured + v_ref
        result = self.voltage_to_temperature(v_total)

        return result
