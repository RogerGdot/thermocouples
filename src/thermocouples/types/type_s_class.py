"""
Type S Thermocouple (Pt-10%Rh / Pt) - Abstract Class Implementation

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

This module implements Type S thermocouple as a class inheriting from the abstract
Thermocouple base class, maintaining all original NIST data and calculations.

Type S Characteristics:
- Positive leg: Platinum-10%Rhodium (Pt-10%Rh)
- Negative leg: Pure Platinum (Pt)
- Temperature range: -50°C to 1768.1°C
- EMF range: -0.235 mV to 18.693 mV
- Accuracy: ±1.5°C or ±0.25% (whichever is greater)
- Maximum continuous temperature: 1600°C in oxidizing atmosphere
- High accuracy and stability at elevated temperatures
- Standard for ITS-90 calibration from 630.74°C to 1064.18°C
"""

from typing import Callable, Optional

from ..base import Thermocouple


class TypeS(Thermocouple):
    """
    Type S Thermocouple (Platinum-10%Rhodium / Platinum) implementation.

    Inherits from abstract Thermocouple base class and provides all
    NIST-compliant calculation methods for Type S thermocouples.
    """

    @property
    def name(self) -> str:
        """Thermocouple type designation."""
        return "Type S"

    @property
    def _temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to voltage polynomial coefficients (°C to µV)."""
        return [
            # Range: -50°C to 1064.18°C
            # $ Source: NIST Monograph 175, ITS-90, Page 107, Table 4.3.1, Type S thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-50, 1064.18),
                [
                    0.000000000000e00,  # c₀
                    5.403133086310e00,  # c₁
                    1.259342897770e-02,  # c₂
                    -2.324779686040e-05,  # c₃
                    3.220288230310e-08,  # c₄
                    -3.314651963040e-11,  # c₅
                    2.557442517860e-14,  # c₆
                    -1.250688713930e-17,  # c₇
                    2.714431761140e-21,  # c₈
                ],
            ),
            # Range: 1064.18°C to 1664.5°C
            # $ Source: NIST Monograph 175, ITS-90, Page 107, Table 4.3.1, Type S thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (1064.18, 1664.5),
                [
                    1.329004440850e03,  # c₀
                    3.345784570100e00,  # c₁
                    6.548051928980e-03,  # c₂
                    -1.648562592370e-05,  # c₃
                    1.299896051750e-09,  # c₄
                ],
            ),
            # Range: 1664.5°C to 1768.1°C
            # $ Source: NIST Monograph 175, ITS-90, Page 107, Table 4.3.1, Type S thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (1664.5, 1768.1),
                [
                    1.466282326400e05,  # c₀
                    -2.584305167700e02,  # c₁
                    1.636935746900e-01,  # c₂
                    -3.304390469700e-05,  # c₃
                    -9.432236906500e-09,  # c₄
                ],
            ),
        ]

    @property
    def _microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Voltage to temperature polynomial coefficients (µV to °C)."""
        return [
            # Range: -235µV to 1874µV (-50°C to 250°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 270, Table A4.1, Type S thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-235, 1874),
                [
                    0.000000000000e00,  # c₀
                    1.849494760000e-01,  # c₁
                    -8.005040620000e-05,  # c₂
                    1.022374500000e-07,  # c₃
                    -1.522485920000e-10,  # c₄
                    1.888213320000e-13,  # c₅
                    -1.590859410000e-16,  # c₆
                    8.230278000000e-20,  # c₇
                    -2.341077000000e-23,  # c₈
                    2.797862000000e-27,  # c₉
                ],
            ),
            # Range: 1874µV to 11950µV (250°C to 1200°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 270, Table A4.1, Type S thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (1874, 11950),
                [
                    1.291507177000e01,  # c₀
                    1.466298863000e-01,  # c₁
                    -1.534713402000e-05,  # c₂
                    3.145945973000e-09,  # c₃
                    -4.163257839000e-13,  # c₄
                    3.187963771000e-17,  # c₅
                    -1.291637500000e-21,  # c₆
                    2.183475087000e-26,  # c₇
                    -1.447379511000e-31,  # c₈
                    8.211272125000e-37,  # c₉
                ],
            ),
            # Range: 11950µV to 17536µV (1200°C to 1600°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 270, Table A4.1, Type S thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (11950, 17536),
                [
                    -8.087801117000e01,  # c₀
                    1.621573104000e-01,  # c₁
                    -8.536869453000e-06,  # c₂
                    4.719686976000e-10,  # c₃
                    -1.441693666000e-14,  # c₄
                    2.081618890000e-19,  # c₅
                ],
            ),
            # Range: 17536µV to 18693µV (1600°C to 1768.1°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 270, Table A4.1, Type S thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (17536, 18693),
                [
                    5.333875126000e04,  # c₀
                    -1.235892298000e01,  # c₁
                    1.092657613000e-03,  # c₂
                    -4.265693686000e-08,  # c₃
                    6.247205420000e-13,  # c₄
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
                    5.403133086310e00,  # c₀ (1 * 5.403133086310e00)
                    2.518685795540e-02,  # c₁ (2 * 1.259342897770e-02)
                    -6.974339058120e-05,  # c₂ (3 * -2.324779686040e-05)
                    1.288115292124e-07,  # c₃ (4 * 3.220288230310e-08)
                    -1.657325981520e-10,  # c₄ (5 * -3.314651963040e-11)
                    1.534465510716e-13,  # c₅ (6 * 2.557442517860e-14)
                    -8.754819975510e-17,  # c₆ (7 * -1.250688713930e-17)
                    2.171545408912e-20,  # c₇ (8 * 2.714431761140e-21)
                ],
            ),
            # Range: 1064.18°C to 1664.5°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (1064.18, 1664.5),
                [
                    3.345784570100e00,  # c₀ (1 * 3.345784570100e00)
                    1.309610385796e-02,  # c₁ (2 * 6.548051928980e-03)
                    -4.945687777110e-05,  # c₂ (3 * -1.648562592370e-05)
                    5.199584207000e-09,  # c₃ (4 * 1.299896051750e-09)
                ],
            ),
            # Range: 1664.5°C to 1768.1°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (1664.5, 1768.1),
                [
                    -2.584305167700e02,  # c₀ (1 * -2.584305167700e02)
                    3.273871493800e-01,  # c₁ (2 * 1.636935746900e-01)
                    -9.913171409100e-05,  # c₂ (3 * -3.304390469700e-05)
                    -3.772894762600e-08,  # c₃ (4 * -9.432236906500e-09)
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
                    2.518685795540e-02,  # c₀ (2 * 1.259342897770e-02)
                    -2.092301727436e-04,  # c₁ (3 * -6.974339058120e-05)
                    5.152461168496e-07,  # c₂ (4 * 1.288115292124e-07)
                    -8.286629907600e-10,  # c₃ (5 * -1.657325981520e-10)
                    9.206793064296e-13,  # c₄ (6 * 1.534465510716e-13)
                    -6.128373982857e-16,  # c₅ (7 * -8.754819975510e-17)
                    1.737236327130e-19,  # c₆ (8 * 2.171545408912e-20)
                ],
            ),
            # Range: 1064.18°C to 1664.5°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (1064.18, 1664.5),
                [
                    1.309610385796e-02,  # c₀ (2 * 6.548051928980e-03)
                    -1.483706333133e-04,  # c₁ (3 * -4.945687777110e-05)
                    2.079833682800e-08,  # c₂ (4 * 5.199584207000e-09)
                ],
            ),
            # Range: 1664.5°C to 1768.1°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (1664.5, 1768.1),
                [
                    3.273871493800e-01,  # c₀ (2 * 1.636935746900e-01)
                    -2.973951422730e-04,  # c₁ (3 * -9.913171409100e-05)
                    -1.509157905040e-07,  # c₂ (4 * -3.772894762600e-08)
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for positive leg (°C to µV)."""
        return None  # Individual leg data not available for Type S

    @property
    def _temp_to_microvolt_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for negative leg (°C to µV)."""
        return None  # Individual leg data not available for Type S

    @property
    def _temp_to_seebeck_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to Seebeck coefficient polynomial coefficients for positive leg (°C to µV/K)."""
        return None  # Individual leg data not available for Type S

    @property
    def _temp_to_seebeck_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to Seebeck coefficient polynomial coefficients for negative leg (°C to µV/K)."""
        return None  # Individual leg data not available for Type S

    @property
    def _microvolt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for voltage calculation."""
        return None  # Type S has no exponential correction

    @property
    def _seebeck_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for Seebeck calculation."""
        return None  # Type S has no exponential correction

    @property
    def _dsdt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for dS/dT calculation."""
        return None  # Type S has no exponential correction
