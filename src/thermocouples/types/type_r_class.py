"""
Type R Thermocouple (Pt-13%Rh / Pt) - Abstract Class Implementation

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

This module implements Type R thermocouple as a class inheriting from the abstract
Thermocouple base class, maintaining all original NIST data and calculations.

Type R Characteristics:
- Positive leg: Platinum-13%Rhodium (Pt-13%Rh)
- Negative leg: Pure Platinum (Pt)
- Temperature range: -50°C to 1768.1°C
- EMF range: -0.226 mV to 21.103 mV
- Accuracy: ±1.5°C or ±0.25% (whichever is greater)
- Maximum continuous temperature: 1600°C in oxidizing atmosphere
- High accuracy and stability at elevated temperatures
"""

from typing import Callable, Optional

from ..base import Thermocouple


class TypeR(Thermocouple):
    """
    Type R Thermocouple (Platinum-13%Rhodium / Platinum) implementation.

    Inherits from abstract Thermocouple base class and provides all
    NIST-compliant calculation methods for Type R thermocouples.
    """

    @property
    def name(self) -> str:
        """Thermocouple type designation."""
        return "Type R"

    @property
    def _temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to voltage polynomial coefficients (°C to µV)."""
        return [
            # Range: -50°C to 1064.18°C
            # $ Source: NIST Monograph 175, ITS-90, Page 62, Table 3.3.1, Type R thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-50, 1064.18),
                [
                    0.000000000000e00,  # c₀
                    5.289617297650e00,  # c₁
                    1.391665897820e-02,  # c₂
                    -2.388556930170e-05,  # c₃
                    3.569160010630e-08,  # c₄
                    -4.623476662980e-11,  # c₅
                    5.007774410340e-14,  # c₆
                    -3.731058861910e-17,  # c₇
                    1.577164823670e-20,  # c₈
                    -2.810386252510e-24,  # c₉
                ],
            ),
            # Range: 1064.18°C to 1664.5°C
            # $ Source: NIST Monograph 175, ITS-90, Page 62, Table 3.3.1, Type R thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (1064.18, 1664.5),
                [
                    2.951579253160e03,  # c₀
                    -2.520612513320e00,  # c₁
                    1.595645018650e-02,  # c₂
                    -7.640859475760e-06,  # c₃
                    2.053052910240e-09,  # c₄
                    -2.933596681730e-13,  # c₅
                ],
            ),
            # Range: 1664.5°C to 1768.1°C
            # $ Source: NIST Monograph 175, ITS-90, Page 62, Table 3.3.1, Type R thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (1664.5, 1768.1),
                [
                    1.522321182090e05,  # c₀
                    -2.688198885450e02,  # c₁
                    1.712802804710e-01,  # c₂
                    -3.458957064740e-05,  # c₃
                    -9.346339710650e-09,  # c₄
                ],
            ),
        ]

    @property
    def _microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Voltage to temperature polynomial coefficients (µV to °C)."""
        return [
            # Range: -226µV to 1923µV (-50°C to 250°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 264, Table A3.1, Type R thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-226, 1923),
                [
                    0.000000000000e00,  # c₀
                    1.889138370200e-01,  # c₁
                    -9.383529496300e-05,  # c₂
                    1.306131930200e-07,  # c₃
                    -2.270358218200e-10,  # c₄
                    3.514565770700e-13,  # c₅
                    -3.895390360700e-16,  # c₆
                    2.823947122000e-19,  # c₇
                    -1.260728228000e-22,  # c₈
                    3.135361540000e-26,  # c₉
                    -3.318776790000e-30,  # c₁₀
                ],
            ),
            # Range: 1923µV to 13228µV (250°C to 1200°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 264, Table A3.1, Type R thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (1923, 13228),
                [
                    1.334584505000e01,  # c₀
                    1.472644573000e-01,  # c₁
                    -1.844024844000e-05,  # c₂
                    4.031129726000e-09,  # c₃
                    -6.249428360000e-13,  # c₄
                    6.468412046000e-17,  # c₅
                    -4.458750426000e-21,  # c₆
                    1.994710149000e-25,  # c₇
                    -5.313401790000e-30,  # c₈
                    6.481976217000e-35,  # c₉
                ],
            ),
            # Range: 13228µV to 19739µV (1200°C to 1600°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 264, Table A3.1, Type R thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (19739, 21103),
                [
                    -8.199599416000e01,  # c₀
                    1.553962042000e-01,  # c₁
                    -8.342197663000e-06,  # c₂
                    4.279433549000e-10,  # c₃
                    -1.191577910000e-14,  # c₄
                    1.492290091000e-19,  # c₅
                ],
            ),
        ]

    @property
    def _temp_to_seebeck_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to Seebeck coefficient polynomial coefficients (°C to µV/K)."""
        return [
            # Range: -50°C to 1064.18°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (-50, 1064.18),
                [
                    5.289617297650e00,  # c₀ (1 * 5.289617297650e00)
                    2.783331795640e-02,  # c₁ (2 * 1.391665897820e-02)
                    -7.165670790510e-05,  # c₂ (3 * -2.388556930170e-05)
                    1.427664004252e-07,  # c₃ (4 * 3.569160010630e-08)
                    -2.311738331490e-10,  # c₄ (5 * -4.623476662980e-11)
                    3.004664646204e-13,  # c₅ (6 * 5.007774410340e-14)
                    -2.611741203370e-16,  # c₆ (7 * -3.731058861910e-17)
                    1.261731858936e-19,  # c₇ (8 * 1.577164823670e-20)
                    -2.529347627259e-23,  # c₈ (9 * -2.810386252510e-24)
                ],
            ),
            # Range: 1064.18°C to 1664.5°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (1064.18, 1664.5),
                [
                    -2.520612513320e00,  # c₀ (1 * -2.520612513320e00)
                    3.191290037300e-02,  # c₁ (2 * 1.595645018650e-02)
                    -2.292257842728e-05,  # c₂ (3 * -7.640859475760e-06)
                    8.212211640960e-09,  # c₃ (4 * 2.053052910240e-09)
                    -1.466798340865e-12,  # c₄ (5 * -2.933596681730e-13)
                ],
            ),
            # Range: 1664.5°C to 1768.1°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (1664.5, 1768.1),
                [
                    -2.688198885450e02,  # c₀ (1 * -2.688198885450e02)
                    3.425605609420e-01,  # c₁ (2 * 1.712802804710e-01)
                    -1.037687419422e-04,  # c₂ (3 * -3.458957064740e-05)
                    -3.738535884260e-08,  # c₃ (4 * -9.346339710650e-09)
                ],
            ),
        ]

    @property
    def _temp_to_dsdt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to dSeebeck/dT polynomial coefficients (°C to nV/K²)."""
        return [
            # Range: -50°C to 1064.18°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (-50, 1064.18),
                [
                    2.783331795640e-02,  # c₀ (2 * 1.391665897820e-02)
                    -2.149701237153e-04,  # c₁ (3 * -7.165670790510e-05)
                    5.710656017008e-07,  # c₂ (4 * 1.427664004252e-07)
                    -1.155869332745e-09,  # c₃ (5 * -2.311738331490e-10)
                    1.802798787722e-12,  # c₄ (6 * 3.004664646204e-13)
                    -1.828216842036e-15,  # c₅ (7 * -2.611741203370e-16)
                    1.009385455149e-18,  # c₆ (8 * 1.261731858936e-19)
                    -2.276412864533e-22,  # c₇ (9 * -2.529347627259e-23)
                ],
            ),
            # Range: 1064.18°C to 1664.5°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (1064.18, 1664.5),
                [
                    3.191290037300e-02,  # c₀ (2 * 1.595645018650e-02)
                    -6.876773528184e-05,  # c₁ (3 * -2.292257842728e-05)
                    3.284884656384e-08,  # c₂ (4 * 8.212211640960e-09)
                    -7.333991704325e-12,  # c₃ (5 * -1.466798340865e-12)
                ],
            ),
            # Range: 1664.5°C to 1768.1°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (1664.5, 1768.1),
                [
                    3.425605609420e-01,  # c₀ (2 * 1.712802804710e-01)
                    -3.113062258266e-04,  # c₁ (3 * -1.037687419422e-04)
                    -1.495414353704e-07,  # c₂ (4 * -3.738535884260e-08)
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for positive leg (°C to µV)."""
        return None  # Individual leg data not available for Type R

    @property
    def _temp_to_microvolt_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for negative leg (°C to µV)."""
        return None  # Individual leg data not available for Type R

    @property
    def _temp_to_seebeck_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to Seebeck coefficient polynomial coefficients for positive leg (°C to µV/K)."""
        return None  # Individual leg data not available for Type R

    @property
    def _temp_to_seebeck_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to Seebeck coefficient polynomial coefficients for negative leg (°C to µV/K)."""
        return None  # Individual leg data not available for Type R

    @property
    def _microvolt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for voltage calculation."""
        return None  # Type R has no exponential correction

    @property
    def _seebeck_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for Seebeck calculation."""
        return None  # Type R has no exponential correction

    @property
    def _dsdt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for dS/dT calculation."""
        return None  # Type R has no exponential correction
