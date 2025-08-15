"""
Type E Thermocouple (Ni-Cr / Cu-Ni) Data and Coefficients

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

Type E Characteristics:
- Positive leg: Nickel-Chromium (Ni-Cr)
- Negative leg: Copper-Nickel (Cu-Ni)
- Temperature range: -270°C to 1000°C
- EMF range: -8.825 mV to 76.373 mV
- Accuracy: ±1.7°C or ±0.5% (whichever is greater)
- Maximum continuous temperature: 900°C in oxidizing atmosphere
"""

from typing import Optional

from ..base import Thermocouple


class TypeE(Thermocouple):
    """Type E Thermocouple (Ni-Cr / Cu-Ni) implementation."""

    @property
    def name(self) -> str:
        """Get the thermocouple type name."""
        return "Type E"

    @property
    def _temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Get temperature to microvolt polynomial coefficients."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 104, Table 5.3.1, Type E thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    5.866550870800e01,  # c₁
                    4.541097712400e-02,  # c₂
                    -7.799804868600e-04,  # c₃
                    -2.580016084300e-05,  # c₄
                    -5.945258305700e-07,  # c₅
                    -9.321405866700e-09,  # c₆
                    -1.028760553400e-10,  # c₇
                    -8.037012362100e-13,  # c₈
                    -4.397949739100e-15,  # c₉
                    -1.641477635500e-17,  # c₁₀
                    -3.967361951600e-20,  # c₁₁
                    -5.582732872100e-23,  # c₁₂
                    -3.465784201300e-26,  # c₁₃
                ],
            ),
            # Range: 0°C to 1000°C
            # $ Source: NIST Monograph 175, ITS-90, Page 104, Table 5.3.1, Type E thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 1000),
                [
                    0.000000000000e00,  # c₀
                    5.866550871000e01,  # c₁
                    4.503227558200e-02,  # c₂
                    2.890840721200e-05,  # c₃
                    -3.305689665200e-07,  # c₄
                    6.502440327000e-10,  # c₅
                    -1.919749550400e-13,  # c₆
                    -1.253660049700e-15,  # c₇
                    2.148921756900e-18,  # c₈
                    -1.438804178200e-21,  # c₉
                    3.596089948100e-25,  # c₁₀
                ],
            ),
        ]

    @property
    def _microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Get microvolt to temperature polynomial coefficients."""
        return [
            # Range: -8825µV to 0µV (-200°C to 0°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 301, Table A5.1, Type E thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-8825, 0),
                [
                    0.000000000000e00,  # c₀
                    1.697728800000e-02,  # c₁
                    -4.351497000000e-07,  # c₂
                    -1.585969700000e-10,  # c₃
                    -9.250287100000e-14,  # c₄
                    -2.608431400000e-17,  # c₅
                    -4.136019900000e-21,  # c₆
                    -3.403403000000e-25,  # c₇
                    -1.156489000000e-29,  # c₈
                ],
            ),
            # Range: 0µV to 76373µV (0°C to 1000°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 301, Table A5.1, Type E thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 76373),
                [
                    0.000000000000e00,  # c₀
                    1.705703500000e-02,  # c₁
                    -2.330175900000e-07,  # c₂
                    6.543558500000e-12,  # c₃
                    -7.356274900000e-17,  # c₄
                    -1.789600100000e-21,  # c₅
                    8.403616500000e-26,  # c₆
                    -1.373587900000e-30,  # c₇
                    1.062982300000e-35,  # c₈
                    -3.244708700000e-41,  # c₉
                ],
            ),
        ]

    @property
    def _temp_to_seebeck_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients."""
        return [
            # Range: -270°C to 0°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (-270, 0),
                [
                    5.866550870800e01,  # c₀ (1 * c₁ 5.866550870800e01)
                    9.082195442800e-02,  # c₁ (2 * c₂ 4.541097712400e-02)
                    -2.339941460580e-03,  # c₂ (3 * c₃ -7.799804868600e-04)
                    -1.032006433720e-04,  # c₃ (4 * c₄ -2.580016084300e-05)
                    -2.972629152850e-06,  # c₄ (5 * c₅ -5.945258305700e-07)
                    -5.592843520020e-08,  # c₅ (6 * c₆ -9.321405866700e-09)
                    -7.201323873800e-10,  # c₆ (7 * c₇ -1.028760553400e-10)
                    -6.429609889680e-12,  # c₇ (8 * c₈ -8.037012362100e-13)
                    -3.958164765190e-14,  # c₈ (9 * c₉ -4.397949739100e-15)
                    -1.641477635500e-16,  # c₉ (10 * c₁₀ -1.641477635500e-17)
                    -4.364101567600e-19,  # c₁₀ (11 * c₁₁ -3.967361951600e-20)
                    -6.699279446520e-22,  # c₁₁ (12 * c₁₂ -5.582732872100e-23)
                    -4.505519461690e-25,  # c₁₂ (13 * c₁₃ -3.465784201300e-26)
                ],
            ),
            # Range: 0°C to 1000°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (0, 1000),
                [
                    5.866550871000e01,  # c₀ (1 * c₁ 5.866550871000e01)
                    9.006455116400e-02,  # c₁ (2 * c₂ 4.503227558200e-02)
                    8.672522163600e-05,  # c₂ (3 * c₃ 2.890840721200e-05)
                    -1.322275866080e-06,  # c₃ (4 * c₄ -3.305689665200e-07)
                    3.251220163500e-09,  # c₄ (5 * c₅ 6.502440327000e-10)
                    -1.151849730240e-12,  # c₅ (6 * c₆ -1.919749550400e-13)
                    -8.775620347900e-15,  # c₆ (7 * c₇ -1.253660049700e-15)
                    1.719137405520e-17,  # c₇ (8 * c₈ 2.148921756900e-18)
                    -1.294923760380e-20,  # c₈ (9 * c₉ -1.438804178200e-21)
                    3.596089948100e-24,  # c₉ (10 * c₁₀ 3.596089948100e-25)
                ],
            ),
        ]

    @property
    def _temp_to_dsdt_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to dSeebeck/dT polynomial coefficients."""
        return [
            # Range: -270°C to 0°C
            # $ Source: Derivative of temp_to_seebeck coefficients
            (
                (-270, 0),
                [
                    9.082195442800e-02,  # c₀ (1 * 9.082195442800e-02)
                    -4.679882921160e-03,  # c₁ (2 * -2.339941460580e-03)
                    -3.096019301160e-04,  # c₂ (3 * -1.032006433720e-04)
                    -1.189051661140e-05,  # c₃ (4 * -2.972629152850e-06)
                    -2.796421760100e-07,  # c₄ (5 * -5.592843520020e-08)
                    -4.320794324280e-09,  # c₅ (6 * -7.201323873800e-10)
                    -4.500726922776e-11,  # c₆ (7 * -6.429609889680e-12)
                    -3.166531812152e-13,  # c₇ (8 * -3.958164765190e-14)
                    -1.477329871950e-15,  # c₈ (9 * -1.641477635500e-16)
                    -4.800511572360e-18,  # c₉ (10 * -4.364101567600e-19)
                    -8.039135335824e-21,  # c₁₀ (11 * -6.699279446520e-22)
                    -5.857175700197e-24,  # c₁₁ (12 * -4.505519461690e-25)
                ],
            ),
            # Range: 0°C to 1000°C
            # $ Source: Derivative of temp_to_seebeck coefficients
            (
                (0, 1000),
                [
                    9.006455116400e-02,  # c₀ (1 * 9.006455116400e-02)
                    1.734504432720e-04,  # c₁ (2 * 8.672522163600e-05)
                    -3.966827598240e-06,  # c₂ (3 * -1.322275866080e-06)
                    1.300488065400e-08,  # c₃ (4 * 3.251220163500e-09)
                    -5.759248651200e-12,  # c₄ (5 * -1.151849730240e-12)
                    -5.265372208740e-14,  # c₅ (6 * -8.775620347900e-15)
                    1.203396183640e-16,  # c₆ (7 * 1.719137405520e-17)
                    -1.035539008304e-19,  # c₇ (8 * -1.294923760380e-20)
                    3.236480953290e-23,  # c₈ (9 * 3.596089948100e-24)
                ],
            ),
        ]
