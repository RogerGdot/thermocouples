"""
Type T Thermocouple (Cu / Cu-Ni) - Abstract Class Implementation

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

This module implements Type T thermocouple as a class inheriting from the abstract
Thermocouple base class, maintaining all original NIST data and calculations.

Type T Characteristics:
- Positive leg: Copper (Cu)
- Negative leg: Copper-Nickel (Cu-Ni, Constantan)
- Temperature range: -270°C to 400°C
- EMF range: -5.603 mV to 20.872 mV
- Accuracy: ±1.0°C or ±0.75% (whichever is greater)
- Maximum continuous temperature: 350°C in oxidizing atmosphere
- Excellent for low temperature measurements
- High stability and linearity at sub-zero temperatures
- Resistant to corrosion in moist atmospheres
"""

from typing import Callable, Optional

from ..base import Thermocouple


class TypeT(Thermocouple):
    """
    Type T Thermocouple (Copper / Copper-Nickel) implementation.

    Inherits from abstract Thermocouple base class and provides all
    NIST-compliant calculation methods for Type T thermocouples.
    """

    @property
    def name(self) -> str:
        """Thermocouple type designation."""
        return "Type T"

    @property
    def _temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Temperature to voltage polynomial coefficients (°C to µV)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 253, Table 9.3.1, Type T thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    3.874810636400e01,  # c₁
                    4.419443434700e-02,  # c₂
                    1.184432310500e-04,  # c₃
                    2.003297355400e-05,  # c₄
                    9.013801955900e-07,  # c₅
                    2.265115659300e-08,  # c₆
                    3.607115420500e-10,  # c₇
                    3.849393988300e-12,  # c₈
                    2.821352192500e-14,  # c₉
                    1.425159477900e-16,  # c₁₀
                    4.876866228600e-19,  # c₁₁
                    1.079553927000e-21,  # c₁₂
                    1.394502706200e-24,  # c₁₃
                    7.979515392700e-28,  # c₁₄
                ],
            ),
            # Range: 0°C to 400°C
            # $ Source: NIST Monograph 175, ITS-90, Page 253, Table 9.3.1, Type T thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 400),
                [
                    0.000000000000e00,  # c₀
                    3.874810636400e01,  # c₁
                    3.329222788000e-02,  # c₂
                    2.061824340400e-04,  # c₃
                    -2.188225684600e-06,  # c₄
                    1.099688092800e-08,  # c₅
                    -3.081575877200e-11,  # c₆
                    4.547913529000e-14,  # c₇
                    -2.751290167300e-17,  # c₈
                ],
            ),
        ]

    @property
    def _microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Voltage to temperature polynomial coefficients (µV to °C)."""
        return [
            # Range: -5603µV to 0µV (-200°C to 0°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 309, Table A9.1, Type T thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-5603, 0),
                [
                    0.000000000000e00,  # c₀
                    2.594919200000e-02,  # c₁
                    -2.131696700000e-07,  # c₂
                    7.901869200000e-10,  # c₃
                    4.252777700000e-13,  # c₄
                    1.330447300000e-16,  # c₅
                    2.024144600000e-20,  # c₆
                    1.266817100000e-24,  # c₇
                ],
            ),
            # Range: 0µV to 20872µV (0°C to 400°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 309, Table A9.1, Type T thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 20872),
                [
                    0.000000000000e00,  # c₀
                    2.592800000000e-02,  # c₁
                    -7.602961000000e-07,  # c₂
                    4.637791000000e-11,  # c₃
                    -2.165394000000e-15,  # c₄
                    6.048144000000e-20,  # c₅
                    -7.293422000000e-25,  # c₆
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
                    3.874810636400e01,  # c₀ (1 * 3.874810636400e01)
                    8.838886869400e-02,  # c₁ (2 * 4.419443434700e-02)
                    3.553296931500e-04,  # c₂ (3 * 1.184432310500e-04)
                    8.013189421600e-05,  # c₃ (4 * 2.003297355400e-05)
                    4.506900977950e-06,  # c₄ (5 * 9.013801955900e-07)
                    1.359069395580e-07,  # c₅ (6 * 2.265115659300e-08)
                    2.524880794350e-09,  # c₆ (7 * 3.607115420500e-10)
                    3.079515190640e-11,  # c₇ (8 * 3.849393988300e-12)
                    2.539206932500e-13,  # c₈ (9 * 2.821352192500e-14)
                    1.425159477900e-15,  # c₉ (10 * 1.425159477900e-16)
                    5.364553051460e-18,  # c₁₀ (11 * 4.876866228600e-19)
                    1.295464712400e-20,  # c₁₁ (12 * 1.079553927000e-21)
                    1.812853118060e-23,  # c₁₂ (13 * 1.394502706200e-24)
                    1.117332550780e-26,  # c₁₃ (14 * 7.979515392700e-28)
                ],
            ),
            # Range: 0°C to 400°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (0, 400),
                [
                    3.874810636400e01,  # c₀ (1 * 3.874810636400e01)
                    6.658445576000e-02,  # c₁ (2 * 3.329222788000e-02)
                    6.185473021200e-04,  # c₂ (3 * 2.061824340400e-04)
                    -8.752902738400e-06,  # c₃ (4 * -2.188225684600e-06)
                    5.498440464000e-08,  # c₄ (5 * 1.099688092800e-08)
                    -1.848945526320e-10,  # c₅ (6 * -3.081575877200e-11)
                    3.183539470300e-13,  # c₆ (7 * 4.547913529000e-14)
                    -2.201032133840e-16,  # c₇ (8 * -2.751290167300e-17)
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
                    8.838886869400e-02,  # c₀ (2 * 4.419443434700e-02)
                    1.065989079450e-03,  # c₁ (3 * 3.553296931500e-04)
                    3.205275768640e-04,  # c₂ (4 * 8.013189421600e-05)
                    2.253450488975e-05,  # c₃ (5 * 4.506900977950e-06)
                    8.154416373480e-07,  # c₄ (6 * 1.359069395580e-07)
                    1.514928476610e-08,  # c₅ (7 * 2.164183537300e-09)
                    2.463612152512e-10,  # c₆ (8 * 3.079515190640e-11)
                    2.285286039250e-12,  # c₇ (9 * 2.539206932500e-13)
                    1.282643530110e-14,  # c₈ (10 * 1.425159477900e-15)
                    5.364928850600e-17,  # c₉ (11 * 4.877207136418e-18)
                    1.425164712400e-19,  # c₁₀ (12 * 1.187637260333e-20)
                    2.356710723278e-22,  # c₁₁ (13 * 1.812853518060e-23)
                    1.562382668092e-25,  # c₁₂ (14 * 1.117332550780e-26)
                ],
            ),
            # Range: 0°C to 400°C
            # $ Source: Second derivative of temp_to_microvolt coefficients
            (
                (0, 400),
                [
                    6.658445576000e-02,  # c₀ (2 * 3.329222788000e-02)
                    1.855641906360e-03,  # c₁ (3 * 6.185473021200e-04)
                    -3.501161095360e-05,  # c₂ (4 * -8.752902738400e-06)
                    2.749220232000e-07,  # c₃ (5 * 5.498440464000e-08)
                    -1.109367031580e-09,  # c₄ (6 * -1.848945526320e-10)
                    2.228253652210e-12,  # c₅ (7 * 3.183539470300e-13)
                    -1.540722496720e-15,  # c₆ (8 * -1.925903120900e-16)
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for positive leg (°C to µV)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 260, Table 9.4.1, Type TP thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    5.894548229700e01,  # c₁
                    2.177354516700e-02,  # c₂
                    2.826751733100e-04,  # c₃
                    2.256129063200e-05,  # c₄
                    9.502026902000e-07,  # c₅
                    2.412716823300e-08,  # c₆
                    3.910747567800e-10,  # c₇
                    4.217403476600e-12,  # c₈
                    3.094671890400e-14,  # c₉
                    1.551930033900e-16,  # c₁₀
                    5.235860991100e-19,  # c₁₁
                    1.136383791300e-21,  # c₁₂
                    1.433054079200e-24,  # c₁₃
                    7.979515392700e-28,  # c₁₄
                ],
            ),
            # Range: 0°C to 400°C
            # $ Source: NIST Monograph 175, ITS-90, Page 260, Table 9.4.1, Type TP thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 400),
                [
                    0.000000000000e00,  # c₀
                    5.894548229700e01,  # c₁
                    1.638500624600e-02,  # c₂
                    5.177203018000e-04,  # c₃
                    -3.901166059300e-06,  # c₄
                    1.966823989100e-08,  # c₅
                    -5.505781842700e-11,  # c₆
                    8.134297489900e-14,  # c₇
                    -4.917094071000e-17,  # c₈
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Temperature to voltage polynomial coefficients for negative leg (°C to µV)."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 261, Table 9.4.2, Type TN thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    2.019737593000e01,  # c₁
                    -2.237911104600e-02,  # c₂
                    -1.642308423600e-04,  # c₃
                    -2.526935291900e-06,  # c₄
                    -4.882249709100e-08,  # c₅
                    -1.476016412900e-09,  # c₆
                    -3.036485026700e-11,  # c₇
                    -3.681065829700e-13,  # c₈
                    -2.736717021100e-15,  # c₉
                    -1.267639110200e-17,  # c₁₀
                    -3.580946385000e-20,  # c₁₁
                    -5.683696630000e-23,  # c₁₂
                    -3.864413928000e-26,  # c₁₃
                    0.000000000000e00,  # c₁₄
                ],
            ),
            # Range: 0°C to 400°C
            # $ Source: NIST Monograph 175, ITS-90, Page 261, Table 9.4.2, Type TN thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 400),
                [
                    0.000000000000e00,  # c₀
                    2.019737593000e01,  # c₁
                    -1.691222164000e-02,  # c₂
                    -3.115988436600e-04,  # c₃
                    1.712961874700e-06,  # c₄
                    -8.663962851800e-09,  # c₅
                    2.426122951500e-11,  # c₆
                    -3.585839945900e-14,  # c₇
                    2.165709850700e-17,  # c₈
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
                    5.894548229700e01,  # c₀ (1 * 5.894548229700e01)
                    4.354709033400e-02,  # c₁ (2 * 2.177354516700e-02)
                    8.480255199300e-04,  # c₂ (3 * 2.826751733100e-04)
                    9.024516252800e-05,  # c₃ (4 * 2.256129063200e-05)
                    4.751013451000e-06,  # c₄ (5 * 9.502026902000e-07)
                    1.447630093980e-07,  # c₅ (6 * 2.412716823300e-08)
                    2.737523297460e-09,  # c₆ (7 * 3.910747567800e-10)
                    3.373922781280e-11,  # c₇ (8 * 4.217403476600e-12)
                    2.785204701360e-13,  # c₈ (9 * 3.094671890400e-14)
                    1.551930033900e-15,  # c₉ (10 * 1.551930033900e-16)
                    5.759447090210e-18,  # c₁₀ (11 * 5.235860991100e-19)
                    1.363660549560e-20,  # c₁₁ (12 * 1.136383791300e-21)
                    1.862970302960e-23,  # c₁₂ (13 * 1.433054079200e-24)
                    1.117332550780e-26,  # c₁₃ (14 * 7.979515392700e-28)
                ],
            ),
            # Range: 0°C to 400°C
            # $ Source: Derivative of positive leg coefficients
            (
                (0, 400),
                [
                    5.894548229700e01,  # c₀ (1 * 5.894548229700e01)
                    3.277001249200e-02,  # c₁ (2 * 1.638500624600e-02)
                    1.553160905400e-03,  # c₂ (3 * 5.177203018000e-04)
                    -1.560466423720e-05,  # c₃ (4 * -3.901166059300e-06)
                    9.834119955000e-08,  # c₄ (5 * 1.966823989100e-08)
                    -3.303469105620e-10,  # c₅ (6 * -5.505781842700e-11)
                    5.694008242930e-13,  # c₆ (7 * 8.134297489900e-14)
                    -3.933675256800e-16,  # c₇ (8 * -4.917094071000e-17)
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
                    2.019737593000e01,  # c₀ (1 * 2.019737593000e01)
                    -4.475822209200e-02,  # c₁ (2 * -2.237911104600e-02)
                    -4.926925270800e-04,  # c₂ (3 * -1.642308423600e-04)
                    -1.010774116760e-05,  # c₃ (4 * -2.526935291900e-06)
                    -2.441124854550e-07,  # c₄ (5 * -4.882249709100e-08)
                    -8.856098477400e-09,  # c₅ (6 * -1.476016412900e-09)
                    -2.125539518690e-10,  # c₆ (7 * -3.036485026700e-11)
                    -2.944852663760e-12,  # c₇ (8 * -3.681065829700e-13)
                    -2.463045318990e-14,  # c₈ (9 * -2.736717021100e-15)
                    -1.267639110200e-16,  # c₉ (10 * -1.267639110200e-17)
                    -3.939041023500e-19,  # c₁₀ (11 * -3.580946385000e-20)
                    -6.820435956000e-22,  # c₁₁ (12 * -5.683696630000e-23)
                    -5.023738106400e-25,  # c₁₂ (13 * -3.864413928000e-26)
                ],
            ),
            # Range: 0°C to 400°C
            # $ Source: Derivative of negative leg coefficients
            (
                (0, 400),
                [
                    2.019737593000e01,  # c₀ (1 * 2.019737593000e01)
                    -3.382444328000e-02,  # c₁ (2 * -1.691222164000e-02)
                    -9.347965309800e-04,  # c₂ (3 * -3.115988436600e-04)
                    6.851847498800e-06,  # c₃ (4 * 1.712961874700e-06)
                    -4.331981425900e-08,  # c₄ (5 * -8.663962851800e-09)
                    1.455673770900e-10,  # c₅ (6 * 2.426122951500e-11)
                    -2.510087962300e-13,  # c₆ (7 * -3.585839945900e-14)
                    1.732567880560e-16,  # c₇ (8 * 2.165709850700e-17)
                ],
            ),
        ]

    @property
    def _microvolt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for voltage calculation."""
        return None  # Type T has no exponential correction

    @property
    def _seebeck_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for Seebeck calculation."""
        return None  # Type T has no exponential correction

    @property
    def _dsdt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for dS/dT calculation."""
        return None  # Type T has no exponential correction
