"""
Type K Thermocouple (Ni-Cr / Ni-Al) Data and Coefficients

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

Type K Characteristics:
- Positive leg: Nickel-Chromium (Ni-Cr, Chromel)
- Negative leg: Nickel-Aluminum (Ni-Al, Alumel)
- Temperature range: -270°C to 1372°C
- EMF range: -5.891 mV to 54.886 mV
- Accuracy: ±2.2°C or ±0.75% (whichever is greater)
- Maximum continuous temperature: 1200°C in oxidizing atmosphere
- Most widely used thermocouple type
- Exhibits magnetic phase transition effects around 127°C
"""

import math
from typing import Callable, Optional

from ..base import Thermocouple


def _type_k_voltage_expo_function(temp_c: float) -> float:
    """
    Exponential correction function for Type K thermocouple voltage calculation.

    Type K thermocouples (Chromel-Alumel) exhibit non-linear behavior at positive temperatures
    due to magnetic phase transitions in the Chromel alloy around 127°C. This exponential
    correction term compensates for the deviation from polynomial behavior in voltage calculation.

    Mathematical form: a₀ × exp[a₁ × (T - a₂)²]

    Where:
    - a₀ = 1.185976e02(amplitude coefficient)
    - a₁ = -1.183432e-04 (exponential coefficient)
    - a₂ = 126.9686°C (reference temperature near magnetic transition)

    This correction is only applied for temperatures > 0°C and is added to the
    polynomial calculation to achieve NIST-standard accuracy.

    Args:
        temp_c: Temperature in degrees Celsius

    Returns:
        Exponential correction term in microvolts (0.0 for T ≤ 0°C)
    """
    # $ Source: NIST Monograph 175, ITS-90, Page 157, Table 7.3.1, Type K thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    if temp_c > 0:
        a0 = 1.185976e02
        a1 = -1.183432e-04
        a2 = 126.9686
        result = a0 * math.exp(a1 * (temp_c - a2) ** 2)
        return result

    return 0.0


def _type_k_seebeck_expo_function(temp_c: float) -> float:
    """
    Exponential correction term for Type K thermocouple Seebeck coefficient calculation.

    Mathematical form: d/dT[a₀ × exp[a₁ × (T - a₂)²]] = a₀ × exp[a₁ × (T - a₂)²] × 2a₁ × (T - a₂)

    Where:
    - a₀ = 1.185976e02 (amplitude coefficient)
    - a₁ = -1.183432e-04 (exponential coefficient)
    - a₂ = 126.9686°C (reference temperature)

    Args:
        temp_c: Temperature in degrees Celsius

    Returns:
        Exponential correction term for Seebeck coefficient (µV/K, 0.0 for T ≤ 0°C)
    """
    # $ Source: NIST Monograph 175, ITS-90, Page 157, Table 7.3.1, Type K thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    if temp_c > 0:
        a0 = 1.185976e02
        a1 = -1.183432e-04
        a2 = 126.9686
        result = a0 * math.exp(a1 * (temp_c - a2) ** 2) * 2 * a1 * (temp_c - a2)
        return result

    return 0.0


def _type_k_dsdt_expo_function(temp_c: float) -> float:
    """
    Exponential correction term for Type K thermocouple dSeebeck/dT calculation.
    Second derivative of the exponential function.

    Mathematical form:
    f(T) = exp(a * (T - b)^2) * (c * T^2 + d * T + e)
    f'(T) = exp(a * (T - b)^2) * [2c*T + d + 2a*(T-b)*(c*T^2 + d*T + e)]

    Where:
    - a = -0.000118343
    - b = 126.9686
    - c = 6.64387e-6
    - d = -0.00168713
    - e = 0.0790359

    Args:
        temp_c: Temperature in degrees Celsius

    Returns:
        Exponential correction term for dSeebeck/dT (µV/K², 0.0 for T ≤ 0°C)
    """
    # $ Source: NIST Monograph 175, ITS-90, Page 157, Table 7.3.1, Type K thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    if temp_c > 0:
        # f(T) = exp(a * (T - b)^2) * (c * T^2 + d * T + e)
        # f'(T) = exp(a * (T - b)^2) * [2c*T + d + 2a*(T-b)*(c*T^2 + d*T + e)]
        a = -0.000118343
        b = 126.9686
        c = 6.64387e-6
        d = -0.00168713
        e = 0.0790359
        T = temp_c

        exp_term = math.exp(a * (T - b) ** 2)
        poly = c * T**2 + d * T + e
        poly_deriv = 2 * c * T + d
        result = exp_term * (poly_deriv + 2 * a * (T - b) * poly)
        return result

    return 0.0


def _type_k_kn_expo_function(temp_c: float) -> float:
    """
    Exponential correction term for Pt-67 vs KN thermoelements (Type K negative leg)
    NBS Monograph 125, Table 7.5.1, p.167 (0 to 1372 °C range)

    Args:
        temp_c: Temperature in degrees Celsius

    Returns:
        Exponential correction term (microvolt)
    """
    # $ Source:  NIST Monograph 175, ITS-90, Page 187, Table 7.5.1, Type KN thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    if temp_c > 0:
        a0 = 1.185976e02
        a1 = -1.183432e-04
        a2 = 126.9686
        result = a0 * math.exp(a1 * (temp_c - a2) ** 2)
        return result

    return 0.0


class TypeK(Thermocouple):
    """Type K Thermocouple (Ni-Cr / Ni-Al) implementation."""

    @property
    def name(self) -> str:
        """Get the thermocouple type name."""
        return "Type K"

    @property
    def _temp_to_microvolt_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Get temperature to microvolt polynomial coefficients."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 157, Table 7.3.1, Type K thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    3.945012802500e01,  # c₁
                    2.362237359800e-02,  # c₂
                    -3.285890678400e-04,  # c₃
                    -4.990482877700e-06,  # c₄
                    -6.750905917300e-08,  # c₅
                    -5.741032742800e-10,  # c₆
                    -3.108887289400e-12,  # c₇
                    -1.045160936500e-14,  # c₈
                    -1.988926687800e-17,  # c₉
                    -1.632269748600e-20,  # c₁₀
                ],
            ),
            # Range: 0°C to 1372°C
            # $ Source: NIST Monograph 175, ITS-90, Page 157, Table 7.3.1, Type K thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 1372),
                [
                    -1.760041368600e01,  # c₀
                    3.892120497500e01,  # c₁
                    1.855877003200e-02,  # c₂
                    -9.945759287400e-05,  # c₃
                    3.184094571900e-07,  # c₄
                    -5.607284488900e-10,  # c₅
                    5.607505905900e-13,  # c₆
                    -3.202072000300e-16,  # c₇
                    9.715114715200e-20,  # c₈
                    -1.210472127500e-23,  # c₉
                ],
            ),
        ]

    @property
    def _microvolt_to_temp_data(self) -> list[tuple[tuple[float, float], list[float]]]:
        """Get microvolt to temperature polynomial coefficients."""
        return [
            # Range: -5891µV to 0µV (-200°C to 0°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 305, Table A7.1, Type K thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-5891, 0),
                [
                    0.000000000000e00,  # c₀
                    2.517346200000e-02,  # c₁
                    -1.166287800000e-06,  # c₂
                    -1.083363800000e-09,  # c₃
                    -8.977354000000e-13,  # c₄
                    -3.734237700000e-16,  # c₅
                    -8.663264300000e-20,  # c₆
                    -1.045059800000e-23,  # c₇
                    -5.192057700000e-28,  # c₈
                ],
            ),
            # Range: 0µV to 20644µV (0°C to 500°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 305, Table A7.1, Type K thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 20644),
                [
                    0.000000000000e00,  # c₀
                    2.508355000000e-02,  # c₁
                    7.860106000000e-08,  # c₂
                    -2.503131000000e-10,  # c₃
                    8.315270000000e-14,  # c₄
                    -1.228034000000e-17,  # c₅
                    9.804036000000e-22,  # c₆
                    -4.413030000000e-26,  # c₇
                    1.057734000000e-30,  # c₈
                    -1.052755000000e-35,  # c₉
                ],
            ),
            # Range: 20644µV to 54886µV (500°C to 1372°C)
            # $ Source: NIST Monograph 175, ITS-90, Page 305, Table A7.1, Type K thermocouples
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (20644, 54886),
                [
                    -1.318058000000e02,  # c₀
                    4.830222000000e-02,  # c₁
                    -1.646031000000e-06,  # c₂
                    5.464731000000e-11,  # c₃
                    -9.650715000000e-16,  # c₄
                    8.802193000000e-21,  # c₅
                    -3.110810000000e-26,  # c₆
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
                    3.945012802500e01,  # c₀ (1 * c₁ 3.945012802500e01)
                    4.724475719600e-02,  # c₁ (2 * c₂ 2.362237359800e-02)
                    -9.857672035200e-04,  # c₂ (3 * c₃ -3.285890678400e-04)
                    -1.996193110800e-05,  # c₃ (4 * c₄ -4.990482877700e-06)
                    -3.375452958650e-07,  # c₄ (5 * c₅ -6.750905917300e-08)
                    -3.444619645680e-09,  # c₅ (6 * c₆ -5.741032742800e-10)
                    -2.176221125580e-11,  # c₆ (7 * c₇ -3.108887289400e-12)
                    -8.361287492000e-14,  # c₇ (8 * c₈ -1.045160936500e-14)
                    -1.790034019020e-16,  # c₈ (9 * c₉ -1.988926687800e-17)
                    -1.632269748600e-19,  # c₉ (10 * c₁₀ -1.632269748600e-20)
                ],
            ),
            # Range: 0°C to 1372°C
            # $ Source: Derivative of temp_to_microvolt coefficients
            (
                (0, 1372),
                [
                    3.892120497500e01,  # c₀ (1 * c₁ 3.892120497500e01)
                    3.711754006400e-02,  # c₁ (2 * c₂ 1.855877003200e-02)
                    -2.983727886220e-04,  # c₂ (3 * c₃ -9.945759287400e-05)
                    1.273637828760e-06,  # c₃ (4 * c₄ 3.184094571900e-07)
                    -2.803642244450e-09,  # c₄ (5 * c₅ -5.607284488900e-10)
                    3.364503543540e-12,  # c₅ (6 * c₆ 5.607505905900e-13)
                    -2.241450400210e-15,  # c₆ (7 * c₇ -3.202072000300e-16)
                    7.772091772160e-19,  # c₇ (8 * c₈ 9.715114715200e-20)
                    -1.089384914750e-22,  # c₈ (9 * c₉ -1.210472127500e-23)
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
                    4.724475719600e-02,  # c₀ (1 * 4.724475719600e-02)
                    -1.971534407040e-03,  # c₁ (2 * -9.857672035200e-04)
                    -5.988579332400e-05,  # c₂ (3 * -1.996193110800e-05)
                    -1.350181183460e-06,  # c₃ (4 * -3.375452958650e-07)
                    -1.722309822840e-08,  # c₄ (5 * -3.444619645680e-09)
                    -1.305732675348e-10,  # c₅ (6 * -2.176221125580e-11)
                    -5.852901244400e-13,  # c₆ (7 * -8.361287492000e-14)
                    -1.432027215216e-15,  # c₇ (8 * -1.790034019020e-16)
                    -1.469042773740e-18,  # c₈ (9 * -1.632269748600e-19)
                ],
            ),
            # Range: 0°C to 1372°C
            # $ Source: Derivative of temp_to_seebeck coefficients
            (
                (0, 1372),
                [
                    3.711754006400e-02,  # c₀ (1 * 3.711754006400e-02)
                    -5.967455772440e-04,  # c₁ (2 * -2.983727886220e-04)
                    3.820913486280e-06,  # c₂ (3 * 1.273637828760e-06)
                    -1.121456897780e-08,  # c₃ (4 * -2.803642244450e-09)
                    1.682251771770e-11,  # c₄ (5 * 3.364503543540e-12)
                    -1.344870240126e-14,  # c₅ (6 * -2.241450400210e-15)
                    5.440464240512e-18,  # c₆ (7 * 7.772091772160e-19)
                    -8.715079318000e-22,  # c₇ (8 * -1.089384914750e-22)
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to microvolt polynomial coefficients for positive leg."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 172, Table 7.4.1, Type KP thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    2.581195057400e01,  # c₁
                    2.299008894300e-02,  # c₂
                    -6.157475446000e-04,  # c₃
                    -2.327184376500e-05,  # c₄
                    -5.457033359600e-07,  # c₅
                    -7.845394226400e-09,  # c₆
                    -7.251284060800e-11,  # c₇
                    -4.356917479100e-13,  # c₈
                    -1.664752760600e-15,  # c₉
                    -3.737720750100e-18,  # c₁₀
                    -3.774144269500e-21,  # c₁₁
                    1.002535559000e-24,  # c₁₂
                    3.893531072500e-27,  # c₁₃
                ],
            ),
            # Range: 0°C to 1372°C
            # $ Source: NIST Monograph 175, ITS-90, Page 172, Table 7.4.1, Type KP thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 1372),
                [
                    0.000000000000e00,  # c₀
                    2.581195057300e01,  # c₁
                    2.683139535500e-02,  # c₂
                    -3.867519441200e-05,  # c₃
                    3.030555323400e-08,  # c₄
                    -1.028040353300e-11,  # c₅
                    -3.448171733000e-14,  # c₆
                    8.251289448000e-17,  # c₇
                    -7.889338217700e-20,  # c₈
                    3.569925312600e-23,  # c₉
                    -6.331536065900e-27,  # c₁₀
                ],
            ),
        ]

    @property
    def _temp_to_microvolt_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to microvolt polynomial coefficients for negative leg."""
        return [
            # Range: -270°C to 0°C
            # $ Source: NIST Monograph 175, ITS-90, Page 187, Table 7.5.1, Type KN thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (-270, 0),
                [
                    0.000000000000e00,  # c₀
                    1.363817745200e01,  # c₁
                    6.322846542600e-04,  # c₂
                    2.871584767600e-04,  # c₃
                    1.828136088700e-05,  # c₄
                    4.781942767900e-07,  # c₅
                    7.271290952100e-09,  # c₆
                    6.940395331900e-11,  # c₇
                    4.252401385500e-13,  # c₈
                    1.644863493800e-15,  # c₉
                    3.721398052600e-18,  # c₁₀
                    3.774144269500e-21,  # c₁₁
                    -1.002535559000e-24,  # c₁₂
                    -3.893531072500e-27,  # c₁₃
                ],
            ),
            # Range: 0°C to 1372°C
            # $ Source: NIST Monograph 175, ITS-90, Page 187, Table 7.5.1, Type KN thermoelements versus platinum, Pt-67
            # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
            (
                (0, 1372),
                [
                    -1.760041368600e01,  # c₀
                    1.310925440300e01,  # c₁
                    -8.272625323000e-03,  # c₂
                    -6.078239846200e-05,  # c₃
                    2.891099093900e-08,  # c₄
                    -5.504804535600e-10,  # c₅
                    5.952323079200e-13,  # c₆
                    -4.027200945100e-16,  # c₇
                    1.760445293300e-19,  # c₈
                    -4.780397440100e-23,  # c₉
                    6.331536065900e-27,  # c₁₀
                ],
            ),
        ]

    @property
    def _temp_to_seebeck_pos_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients for positive leg."""
        return [
            # Range: -270°C to 0°C
            # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
            (
                (-270, 0),
                [
                    2.581195057400e01,  # c₀ (1 * 2.581195057400e01)
                    4.598017788600e-02,  # c₁ (2 * 2.299008894300e-02)
                    -1.847242633800e-03,  # c₂ (3 * -6.157475446000e-04)
                    -9.308737506000e-05,  # c₃ (4 * -2.327184376500e-05)
                    -2.728516679800e-06,  # c₄ (5 * -5.457033359600e-07)
                    -4.707236535840e-08,  # c₅ (6 * -7.845394226400e-09)
                    -5.075898842560e-10,  # c₆ (7 * -7.251284060800e-11)
                    -3.921225731190e-12,  # c₇ (8 * -4.356917479100e-13)
                    -1.664752760600e-14,  # c₈ (9 * -1.664752760600e-15)
                    -3.737720750100e-17,  # c₉ (10 * -3.737720750100e-18)
                    -4.151558696450e-20,  # c₁₀ (11 * -3.774144269500e-21)
                    1.302796226000e-23,  # c₁₁ (12 * 1.002535559000e-24)
                    5.061590394250e-26,  # c₁₂ (13 * 3.893531072500e-27)
                ],
            ),
            # Range: 0°C to 1372°C
            # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
            (
                (0, 1372),
                [
                    2.581195057300e01,  # c₀ (1 * 2.581195057300e01)
                    5.366279071000e-02,  # c₁ (2 * 2.683139535500e-02)
                    -1.160255832360e-04,  # c₂ (3 * -3.867519441200e-05)
                    1.212222129360e-07,  # c₃ (4 * 3.030555323400e-08)
                    -5.140201766500e-11,  # c₄ (5 * -1.028040353300e-11)
                    -2.413720213100e-13,  # c₅ (6 * -3.448171733000e-14)
                    5.775902613600e-16,  # c₆ (7 * 8.251289448000e-17)
                    -6.310470574160e-19,  # c₇ (8 * -7.889338217700e-20)
                    3.212932781340e-22,  # c₈ (9 * 3.569925312600e-23)
                    -6.964689672490e-26,  # c₉ (10 * -6.331536065900e-27)
                ],
            ),
        ]

    @property
    def _temp_to_seebeck_neg_leg_data(self) -> Optional[list[tuple[tuple[float, float], list[float]]]]:
        """Get temperature to Seebeck coefficient polynomial coefficients for negative leg."""
        return [
            # Range: -270°C to 0°C
            # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
            (
                (-270, 0),
                [
                    1.363817745200e01,  # c₀ (1 * 1.363817745200e01)
                    1.264569308520e-03,  # c₁ (2 * 6.322846542600e-04)
                    5.743169535200e-04,  # c₂ (3 * 2.871584767600e-04)
                    7.312544354800e-05,  # c₃ (4 * 1.828136088700e-05)
                    2.390971383950e-06,  # c₄ (5 * 4.781942767900e-07)
                    4.089903666470e-08,  # c₅ (6 * 7.271290952100e-09)
                    4.858276732330e-10,  # c₆ (7 * 6.940395331900e-11)
                    3.827161246950e-12,  # c₇ (8 * 4.252401385500e-13)
                    1.644863493800e-14,  # c₈ (9 * 1.644863493800e-15)
                    3.721398052600e-17,  # c₉ (10 * 3.721398052600e-18)
                    4.151558696450e-20,  # c₁₀ (11 * 3.774144269500e-21)
                    -1.303296226000e-23,  # c₁₁ (12 * -1.002535559000e-24)
                    -5.061590394250e-26,  # c₁₂ (13 * -3.893531072500e-27)
                ],
            ),
            # Range: 0°C to 1372°C
            # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
            (
                (0, 1372),
                [
                    1.310925440300e01,  # c₀ (1 * 1.310925440300e01)
                    -1.654525064600e-02,  # c₁ (2 * -8.272625323000e-03)
                    -1.823471953860e-04,  # c₂ (3 * -6.078239846200e-05)
                    1.156439637560e-07,  # c₃ (4 * 2.891099093900e-08)
                    -2.752402267800e-09,  # c₄ (5 * -5.504804535600e-10)
                    4.166626155440e-12,  # c₅ (6 * 5.952323079200e-13)
                    -2.819040661570e-15,  # c₆ (7 * -4.027200945100e-16)
                    1.584400763970e-18,  # c₇ (8 * 1.760445293300e-19)
                    -4.302357696090e-21,  # c₈ (9 * -4.780397440100e-23)
                    6.964689672490e-25,  # c₉ (10 * 6.331536065900e-27)
                ],
            ),
        ]

    @property
    def _microvolt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for voltage calculation."""
        return _type_k_voltage_expo_function

    @property
    def _seebeck_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for Seebeck coefficient calculation."""
        return _type_k_seebeck_expo_function

    @property
    def _dsdt_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for dSeebeck/dT calculation."""
        return _type_k_dsdt_expo_function

    @property
    def _microvolt_neg_leg_expo_function(self) -> Optional[Callable[[float], float]]:
        """Get exponential correction function for negative leg voltage calculation."""
        return _type_k_kn_expo_function
