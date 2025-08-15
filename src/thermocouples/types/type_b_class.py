"""
Type B Thermocouple (Pt-30%Rh / Pt-6%Rh) - Abstract Class Implementation

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

This module implements Type B thermocouple as a class inheriting from the abstract
Thermocouple base class, maintaining all original NIST data and calculations.

Type B Characteristics:
- Positive leg: Platinum-30%Rhodium (Pt-30%Rh)
- Negative leg: Platinum-6%Rhodium (Pt-6%Rh)
- Temperature range: 0°C to 1820°C
- EMF range: 0 mV to 13.820 mV
- Accuracy: ±1.5°C or ±0.25% (whichever is greater)
- Maximum continuous temperature: 1700°C in oxidizing atmosphere
- Minimum temperature: 0°C (no output below this)
- Used for very high temperature measurements
"""

from typing import Callable, Optional

from ..base import Thermocouple


class TypeB(Thermocouple):
    """
    Type B Thermocouple (Platinum-30%Rhodium / Platinum-6%Rhodium) implementation.

    Inherits from abstract Thermocouple base class and provides all
    NIST-compliant calculation methods for Type B thermocouples.
    """

    @property
    def name(self) -> str:
        """Get the thermocouple type name."""
        return "Type B"

    @property
    def _temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to voltage polynomial coefficients (°C to µV)."""
        return [
            # Range: 0°C to 630.615°C
            # $ Source: NIST Monograph 175, ITS-90, page 12, table 2.3.1, Type B thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 630.615),
                [
                    0.000000000000e00,  # c₀
                    -2.465081834600e-01,  # c₁
                    5.904042117100e-03,  # c₂
                    -1.325793163600e-06,  # c₃
                    1.566829190100e-09,  # c₄
                    -1.694452924000e-12,  # c₅
                    6.299034709400e-16,  # c₆
                ],
            ),
            # Range: 630.615°C to 1820°C
            # $ Source: NIST Monograph 175, ITS-90, page 12, table 2.3.1, Type B thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (630.615, 1820),
                [
                    -3.893816862100e03,  # c₀
                    2.857174747000e-01,  # c₁
                    -8.488510478500e-05,  # c₂
                    1.578528016400e-04,  # c₃
                    -1.683534486400e-07,  # c₄
                    1.110979401300e-10,  # c₅
                    -4.451543103300e-14,  # c₆
                    9.897564082100e-18,  # c₇
                    -9.379133028900e-22,  # c₈
                ],
            ),
        ]

    @property
    def _microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Voltage to temperature polynomial coefficients (µV to °C)."""
        return [
            # Range: 0µV to 2431µV (250°C to 700°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 258, Table A2.1, Type B thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 2431),
                [
                    9.842332814000e01,  # c₀
                    6.997150500000e-01,  # c₁
                    -8.476530504000e-04,  # c₂
                    1.005264562000e-06,  # c₃
                    -8.334595204000e-10,  # c₄
                    4.550854305000e-13,  # c₅
                    -1.552303513000e-16,  # c₆
                    2.988675001000e-20,  # c₇
                    -2.474286169000e-24,  # c₈
                ],
            ),
            # Range: 2431µV to 13820µV (700°C to 1820°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 258, Table A2.1, Type B thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (2431, 13820),
                [
                    2.131507177000e02,  # c₀
                    2.851050424000e-01,  # c₁
                    -5.274288120000e-05,  # c₂
                    9.916080701000e-09,  # c₃
                    -1.296530827000e-12,  # c₄
                    1.119587014000e-16,  # c₅
                    -6.062519230000e-21,  # c₆
                    1.866169854000e-25,  # c₇
                    -2.487858213000e-30,  # c₈
                ],
            ),
        ]

    @property
    def _temp_to_seebeck_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to Seebeck coefficient polynomial coefficients (°C to µV/K)."""
        return [
            # Range: 0°C to 630.615°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (0, 630.615),
                [
                    -2.465081834600e-01,  # c₀ (1 * -2.465081834600e-01)
                    1.180808423420e-02,  # c₁ (2 * 5.904042117100e-03)
                    -3.977379490800e-06,  # c₂ (3 * -1.325793163600e-06)
                    6.267316760400e-09,  # c₃ (4 * 1.566829190100e-09)
                    -8.472264620000e-12,  # c₄ (5 * -1.694452924000e-12)
                    3.779420825640e-15,  # c₅ (6 * 6.299034709400e-16)
                ],
            ),
            # Range: 630.615°C to 1820°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (630.615, 1820),
                [
                    2.857174747000e-01,  # c₀ (1 * 2.857174747000e-01)
                    -1.697702095700e-04,  # c₁ (2 * -8.488510478500e-05)
                    4.735584049200e-04,  # c₂ (3 * 1.578528016400e-04)
                    -6.734137945600e-07,  # c₃ (4 * -1.683534486400e-07)
                    5.554897006500e-10,  # c₄ (5 * 1.110979401300e-10)
                    -2.670925861980e-13,  # c₅ (6 * -4.451543103300e-14)
                    6.928294857470e-17,  # c₆ (7 * 9.897564082100e-18)
                    -7.503306423120e-21,  # c₇ (8 * -9.379133028900e-22)
                ],
            ),
        ]

    @property
    def _temp_to_dsdt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to dSeebeck/dT polynomial coefficients (°C to nV/K²)."""
        return [
            # Range: 0°C to 630.615°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (0, 630.615),
                [
                    1.180808423420e-02,  # c₀ (2 * 5.904042117100e-03)
                    -1.193213847240e-05,  # c₁ (3 * -3.977379490800e-06)
                    2.506926704160e-08,  # c₂ (4 * 6.267316760400e-09)
                    -4.236132310000e-11,  # c₃ (5 * -8.472264620000e-12)
                    2.267652495384e-14,  # c₄ (6 * 3.779420825640e-15)
                ],
            ),
            # Range: 630.615°C to 1820°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (630.615, 1820),
                [
                    -1.697702095700e-04,  # c₀ (2 * -8.488510478500e-05)
                    1.420675214760e-03,  # c₁ (3 * 4.735584049200e-04)
                    -2.693655178240e-06,  # c₂ (4 * -6.734137945600e-07)
                    2.777448503250e-09,  # c₃ (5 * 5.554897006500e-10)
                    -1.602555517188e-12,  # c₄ (6 * -2.670925861980e-13)
                    4.849806400229e-16,  # c₅ (7 * 6.928294857470e-17)
                    -6.002645138496e-20,  # c₆ (8 * -7.503306423120e-21)
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for positive leg (°C to µV)."""
        return None  # Individual leg data not available for Type B

    @property
    def _temp_to_microvolt_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for negative leg (°C to µV)."""
        return None  # Individual leg data not available for Type B

    @property
    def _temp_to_seebeck_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to Seebeck coefficient polynomial coefficients for positive leg (°C to µV/K)."""
        return None  # Individual leg data not available for Type B

    @property
    def _temp_to_seebeck_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to Seebeck coefficient polynomial coefficients for negative leg (°C to µV/K)."""
        return None  # Individual leg data not available for Type B

    @property
    def _microvolt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for voltage calculation."""
        return None  # Type B has no exponential correction

    @property
    def _seebeck_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for Seebeck calculation."""
        return None  # Type B has no exponential correction

    @property
    def _dsdt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for dS/dT calculation."""
        return None  # Type B has no exponential correction
