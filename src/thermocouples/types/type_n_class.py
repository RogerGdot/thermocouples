"""
Type N Thermocouple (Ni-Cr-Si / Ni-Si) - Abstract Class Implementation

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

This module implements Type N thermocouple as a class inheriting from the abstract
Thermocouple base class, maintaining all original NIST data and calculations.

Type N Characteristics:
- Positive leg: Nickel-Chromium-Silicon (Ni-Cr-Si, Nicrosil)
- Negative leg: Nickel-Silicon (Ni-Si, Nisil)
- Temperature range: -270°C to 1300°C
- EMF range: -3.990 mV to 47.513 mV
- Accuracy: ±2.2°C or ±0.75% (whichever is greater)
- Maximum continuous temperature: 1200°C in oxidizing atmosphere
- Developed to improve stability of Type K thermocouples
- Superior drift characteristics compared to Type K
"""

from typing import Callable, Optional

from ..base import Thermocouple


class TypeN(Thermocouple):
    """
    Type N Thermocouple (Nicrosil / Nisil) implementation.

    Inherits from abstract Thermocouple base class and provides all
    NIST-compliant calculation methods for Type N thermocouples.
    """

    @property
    def name(self) -> str:
        """Thermocouple type designation."""
        return "Type N"

    @property
    def _temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to voltage polynomial coefficients (°C to µV)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 207, Table 8.3.1, Type N thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    2.615910596200e01,  # c₁
                    1.095748422800e-02,  # c₂
                    -9.384111155400e-05,  # c₃
                    -4.641203975900e-06,  # c₄
                    -2.630335771600e-07,  # c₅
                    -2.265343800300e-09,  # c₆
                    -7.608930079100e-12,  # c₇
                    -9.341966783500e-15,  # c₈
                ],
            ),
            # Range: 0°C to 1300°C
            # $ Source: NIST Monograph 175, ITS-90, Page 207, Table 8.3.1, Type N thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 1300),
                [
                    0.000000000000e00,  # c₀
                    2.592939460100e01,  # c₁
                    1.571014188000e-02,  # c₂
                    4.382562723700e-05,  # c₃
                    -2.526116979400e-07,  # c₄
                    6.431181933900e-10,  # c₅
                    -1.006347151900e-12,  # c₆
                    9.974533899200e-16,  # c₇
                    -6.086324560700e-19,  # c₈
                    2.084922933800e-22,  # c₉
                    -3.068219615200e-26,  # c₁₀
                ],
            ),
        ]

    @property
    def _microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Voltage to temperature polynomial coefficients (µV to °C)."""
        return [
            # Range: -3990µV to 0µV (-200°C to 0°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 296, Table A8.1, Type N thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-3990, 0),
                [
                    0.000000000000e00,  # c₀
                    3.843684562900e-02,  # c₁
                    1.101048482300e-06,  # c₂
                    -9.341966783500e-11,  # c₃
                    -1.203944560700e-15,  # c₄
                    -8.227313663600e-20,  # c₅
                    -2.341650218400e-24,  # c₆
                    -2.526116979400e-29,  # c₇
                ],
            ),
            # Range: 0µV to 20613µV (0°C to 600°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 296, Table A8.1, Type N thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 20613),
                [
                    0.000000000000e00,  # c₀
                    3.868596100000e-02,  # c₁
                    -1.082267000000e-06,  # c₂
                    4.702562000000e-11,  # c₃
                    -2.121169000000e-16,  # c₄
                    -1.172972000000e-20,  # c₅
                    5.392615000000e-25,  # c₆
                    -7.981322000000e-30,  # c₇
                ],
            ),
            # Range: 20613µV to 47513µV (600°C to 1300°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 296, Table A8.1, Type N thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (20613, 47513),
                [
                    1.972485000000e01,  # c₀
                    3.300943000000e-02,  # c₁
                    -3.915159000000e-07,  # c₂
                    9.855391000000e-12,  # c₃
                    -1.274371000000e-16,  # c₄
                    7.767022000000e-22,  # c₅
                ],
            ),
        ]

    @property
    def _temp_to_seebeck_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to Seebeck coefficient polynomial coefficients (°C to µV/K)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (-270, 0),
                [
                    2.615910596200e01,  # c₀ (1 * 2.615910596200e01)
                    2.191496845600e-02,  # c₁ (2 * 1.095748422800e-02)
                    -2.815233346620e-04,  # c₂ (3 * -9.384111155400e-05)
                    -1.856481590360e-05,  # c₃ (4 * -4.641203975900e-06)
                    -1.315167885800e-06,  # c₄ (5 * -2.630335771600e-07)
                    -1.359206280180e-08,  # c₅ (6 * -2.265343800300e-09)
                    -5.326251055370e-11,  # c₆ (7 * -7.608930079100e-12)
                    -7.473573426800e-14,  # c₇ (8 * -9.341966783500e-15)
                ],
            ),
            # Range: 0°C to 1300°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (0, 1300),
                [
                    2.592939460100e01,  # c₀ (1 * 2.592939460100e01)
                    3.142028376000e-02,  # c₁ (2 * 1.571014188000e-02)
                    1.314768817110e-04,  # c₂ (3 * 4.382562723700e-05)
                    -1.010446791760e-06,  # c₃ (4 * -2.526116979400e-07)
                    3.215590966950e-09,  # c₄ (5 * 6.431181933900e-10)
                    -6.038082911400e-12,  # c₅ (6 * -1.006347151900e-12)
                    6.982774329440e-15,  # c₆ (7 * 9.974533899200e-16)
                    -4.869059648560e-18,  # c₇ (8 * -6.086324560700e-19)
                    1.876430640420e-21,  # c₈ (9 * 2.084922933800e-22)
                    -3.068219615200e-25,  # c₉ (10 * -3.068219615200e-26)
                ],
            ),
        ]

    @property
    def _temp_to_dsdt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to dSeebeck/dT polynomial coefficients (°C to nV/K²)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (-270, 0),
                [
                    2.191496845600e-02,  # c₀ (2 * 1.095748422800e-02)
                    -8.445700039860e-04,  # c₁ (3 * -2.815233346620e-04)
                    -7.425926361440e-05,  # c₂ (4 * -1.856481590360e-05)
                    -6.575839429000e-06,  # c₃ (5 * -1.315167885800e-06)
                    -8.155237681080e-08,  # c₄ (6 * -1.359206280180e-08)
                    -3.728375538759e-10,  # c₅ (7 * -5.326251055370e-11)
                    -5.981258741360e-13,  # c₆ (8 * -7.473573426800e-14)
                ],
            ),
            # Range: 0°C to 1300°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (0, 1300),
                [
                    3.142028376000e-02,  # c₀ (2 * 1.571014188000e-02)
                    3.944306451330e-04,  # c₁ (3 * 1.314768817110e-04)
                    -4.041787167040e-06,  # c₂ (4 * -1.010446791760e-06)
                    1.607795483475e-08,  # c₃ (5 * 3.215590966950e-09)
                    -3.622849746840e-11,  # c₄ (6 * -6.038082911400e-12)
                    4.888142030608e-14,  # c₅ (7 * 6.982774329440e-15)
                    -3.895247718848e-17,  # c₆ (8 * -4.869059648560e-18)
                    1.688787576378e-20,  # c₇ (9 * 1.876430640420e-21)
                    -3.068219615200e-24,  # c₈ (10 * -3.068219615200e-25)
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for positive leg (°C to µV)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 214, Table 8.4.1, Type NP thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    5.273511806700e01,  # c₁
                    1.780498013300e-02,  # c₂
                    -1.466317395700e-04,  # c₃
                    -7.285594608500e-06,  # c₄
                    -4.232754851900e-07,  # c₅
                    -3.720859480400e-09,  # c₆
                    -1.287530414300e-11,  # c₇
                    -1.675446783100e-14,  # c₈
                ],
            ),
            # Range: 0°C to 1300°C
            # $ Source: NIST Monograph 175, ITS-90, Page 214, Table 8.4.1, Type NP thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 1300),
                [
                    0.000000000000e00,  # c₀
                    5.234468654000e01,  # c₁
                    2.552906394000e-02,  # c₂
                    6.839993079800e-05,  # c₃
                    -3.954067222600e-07,  # c₄
                    1.006347151900e-09,  # c₅
                    -1.575292329900e-12,  # c₆
                    1.566816717400e-15,  # c₇
                    -9.553386850900e-19,  # c₈
                    3.264869890600e-22,  # c₉
                    -4.802694711000e-26,  # c₁₀
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for negative leg (°C to µV)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 215, Table 8.4.2, Type NN thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    2.657558210500e01,  # c₁
                    7.249982110000e-03,  # c₂
                    -5.517878759200e-05,  # c₃
                    -2.644187032400e-06,  # c₄
                    -1.602228391700e-07,  # c₅
                    -1.455515920100e-09,  # c₆
                    -5.216699205800e-12,  # c₇
                    -7.665859969400e-15,  # c₈
                ],
            ),
            # Range: 0°C to 1300°C
            # $ Source: NIST Monograph 175, ITS-90, Page 215, Table 8.4.2, Type NN thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 1300),
                [
                    0.000000000000e00,  # c₀
                    2.641529194100e01,  # c₁
                    9.809139240000e-03,  # c₂
                    2.457544944800e-05,  # c₃
                    -1.427821244200e-07,  # c₄
                    3.625363183000e-10,  # c₅
                    -5.690847663000e-13,  # c₆
                    5.656831582800e-16,  # c₇
                    -3.467062066200e-19,  # c₈
                    1.180447757200e-22,  # c₉
                    -1.734474894800e-26,  # c₁₀
                ],
            ),
        ]

    @property
    def _temp_to_seebeck_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to Seebeck coefficient polynomial coefficients for positive leg (°C to µV/K)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: Derivative of positive leg coefficients
            (
                (-270, 0),
                [
                    5.273511806700e01,  # c₀ (1 * 5.273511806700e01)
                    3.560996026600e-02,  # c₁ (2 * 1.780498013300e-02)
                    -4.398952187100e-04,  # c₂ (3 * -1.466317395700e-04)
                    -2.914237843400e-05,  # c₃ (4 * -7.285594608500e-06)
                    -2.116377425950e-06,  # c₄ (5 * -4.232754851900e-07)
                    -2.232515688240e-08,  # c₅ (6 * -3.720859480400e-09)
                    -9.012713001000e-11,  # c₆ (7 * -1.287530414300e-11)
                    -1.340357426480e-13,  # c₇ (8 * -1.675446783100e-14)
                ],
            ),
            # Range: 0°C to 1300°C
            # $ Source: Derivative of positive leg coefficients
            (
                (0, 1300),
                [
                    5.234468654000e01,  # c₀ (1 * 5.234468654000e01)
                    5.105812788000e-02,  # c₁ (2 * 2.552906394000e-02)
                    2.051997723940e-04,  # c₂ (3 * 6.839993079800e-05)
                    -1.581626889040e-06,  # c₃ (4 * -3.954067222600e-07)
                    5.031735595000e-09,  # c₄ (5 * 1.006347151900e-09)
                    -9.451753979400e-12,  # c₅ (6 * -1.575292329900e-12)
                    1.096772102180e-14,  # c₆ (7 * 1.566816717400e-15)
                    -7.642709480720e-18,  # c₇ (8 * -9.553386850900e-19)
                    2.938382901540e-21,  # c₈ (9 * 3.264869890600e-22)
                    -4.802694711000e-25,  # c₉ (10 * -4.802694711000e-26)
                ],
            ),
        ]

    @property
    def _temp_to_seebeck_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to Seebeck coefficient polynomial coefficients for negative leg (°C to µV/K)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: Derivative of negative leg coefficients
            (
                (-270, 0),
                [
                    2.657558210500e01,  # c₀ (1 * 2.657558210500e01)
                    1.449996422000e-02,  # c₁ (2 * 7.249982110000e-03)
                    -1.655363627760e-04,  # c₂ (3 * -5.517878759200e-05)
                    -1.057674812960e-05,  # c₃ (4 * -2.644187032400e-06)
                    -8.011141958500e-07,  # c₄ (5 * -1.602228391700e-07)
                    -8.733095520600e-09,  # c₅ (6 * -1.455515920100e-09)
                    -3.651689444060e-11,  # c₆ (7 * -5.216699205800e-12)
                    -6.132687975520e-14,  # c₇ (8 * -7.665859969400e-15)
                ],
            ),
            # Range: 0°C to 1300°C
            # $ Source: Derivative of negative leg coefficients
            (
                (0, 1300),
                [
                    2.641529194100e01,  # c₀ (1 * 2.641529194100e01)
                    1.961827848000e-02,  # c₁ (2 * 9.809139240000e-03)
                    7.372634834400e-05,  # c₂ (3 * 2.457544944800e-05)
                    -5.711284976800e-07,  # c₃ (4 * -1.427821244200e-07)
                    1.812681591500e-09,  # c₄ (5 * 3.625363183000e-10)
                    -3.414508597800e-12,  # c₅ (6 * -5.690847663000e-13)
                    3.959782507960e-15,  # c₆ (7 * 5.656831582800e-16)
                    -2.773649652960e-18,  # c₇ (8 * -3.467062066200e-19)
                    1.062403181480e-21,  # c₈ (9 * 1.180447757200e-22)
                    -1.734474894800e-25,  # c₉ (10 * -1.734474894800e-26)
                ],
            ),
        ]

    @property
    def _microvolt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for voltage calculation."""
        return None  # Type N has no exponential correction

    @property
    def _seebeck_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for Seebeck calculation."""
        return None  # Type N has no exponential correction

    @property
    def _dsdt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for dS/dT calculation."""
        return None  # Type N has no exponential correction
