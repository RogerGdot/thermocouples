"""
Type R Thermocouple (Pt-13%Rh / Pt) Data and Coefficients

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

Type R Characteristics:
- Positive leg: Platinum-13%Rhodium (Pt-13%Rh)
- Negative leg: Pure Platinum (Pt)
- Temperature range: -50°C to 1768.1°C
- EMF range: -0.226 mV to 21.103 mV
- Accuracy: ±1.5°C or ±0.25% (whichever is greater)
- Maximum continuous temperature: 1600°C in oxidizing atmosphere
- High accuracy and stability at elevated temperatures
"""

# Temperature to Voltage Tables (°C to µV)
TEMP_TO_MICROVOLT = [
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
            -3.458957064530e-05,  # c₃
            -9.346339710460e-12,  # c₄
        ],
    ),
]

# Voltage to Temperature Tables (µV to °C)
MICROVOLT_TO_TEMP = [
    # Range: -226µV to 1923µV (-50°C to 250°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 297, Table A3.1, Type R thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-226, 1923),
        [
            0.0000000000e00,  # c₀
            1.8891380000e-01,  # c₁
            -9.3835290000e-05,  # c₂
            1.3068619000e-07,  # c₃
            -2.2703580000e-10,  # c₄
            3.5145659000e-13,  # c₅
            -3.8953900000e-16,  # c₆
            2.8239471000e-19,  # c₇
            -1.2607281000e-22,  # c₈
            3.1353611000e-26,  # c₉
            -3.3187769000e-30,  # c₁₀
        ],
    ),
    # Range: 1923µV to 13228µV (250°C to 1200°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 297, Table A3.1, Type R thermocouples
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
    # Range: 11361µV to 19739µV (1064°C to 1664.5°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 297, Table A3.1, Type R thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (11361, 19739),
        [
            -8.199599416000e01,  # c₀
            1.553962042000e-01,  # c₁
            -8.342197663000e-06,  # c₂
            4.279433549000e-10,  # c₃
            -1.191577910000e-14,  # c₄
            1.492290091000e-19,  # c₅
        ],
    ),
    # Range: 19739µV to 21103µV (1664.5°C to 1768.1°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 297, Table A3.1, Type R thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (19739, 21103),
        [
            3.406177836000e01,  # c₀
            -7.023729171000e-03,  # c₁
            5.582903813000e-06,  # c₂
            -1.952394635000e-09,  # c₃
            2.560740231000e-13,  # c₄
        ],
    ),
]

# Temperature to Seebeck Coefficient Tables (°C to µV/K)
TEMP_TO_SEEBECK = [
    # Range: -50°C to 1064.18°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (-50, 1064.18),
        [
            5.289617297650e00,  # c₀ (1 * c₁ 5.289617297650e00)
            2.783331795640e-02,  # c₁ (2 * c₂ 1.391665897820e-02)
            -7.165670790510e-05,  # c₂ (3 * c₃ -2.388556930170e-05)
            1.427664004252e-07,  # c₃ (4 * c₄ 3.569160010630e-08)
            -2.311738331490e-10,  # c₄ (5 * c₅ -4.623476662980e-11)
            3.004664646204e-13,  # c₅ (6 * c₆ 5.007774410340e-14)
            -2.611741203370e-16,  # c₆ (7 * c₇ -3.731058861910e-17)
            1.261731858936e-19,  # c₇ (8 * c₈ 1.577164823670e-20)
            -2.529347502259e-23,  # c₈ (9 * c₉ -2.810386252510e-24)
        ],
    ),
    # Range: 1064.18°C to 1664.5°C
    # $ Source: Derivative of temp_to_microvolt coefficientsf
    (
        (1064.18, 1664.5),
        [
            -2.520612513320e00,  # c₀ (1 * c₁ -2.520612513320e00)
            3.191290037300e-02,  # c₁ (2 * c₂ 1.595645018650e-02)
            -2.292257862280e-05,  # c₂ (3 * c₃ -7.640859475760e-06)
            8.212211640960e-09,  # c₃ (4 * c₄ 2.053052910240e-09)
            -1.466798340865e-12,  # c₄ (5 * c₅ -2.933596681730e-13)
        ],
    ),
    # Range: 1664.5°C to 1768.1°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (1664.5, 1768.1),
        [
            -2.688198885450e02,  # c₀ (1 * c₁ -2.688198885450e02)
            3.425605609420e-01,  # c₁ (2 * c₂ 1.712802804710e-01)
            -1.037691219359e-04,  # c₂ (3 * c₃ -3.458957064530e-05)
            -3.738533884184e-11,  # c₃ (4 * c₄ -9.346339710460e-12)
        ],
    ),
]

# Temperature to dSeebeck/dT conversion (°C to µV/K²)
TEMP_TO_DSDT = [
    # Range: -50°C to 1064.18°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (-50, 1064.18),
        [
            2.783331795640e-02,  # c₀ (1 * 2.783331795640e-02)
            -1.433134158102e-04,  # c₁ (2 * -7.165670790510e-05)
            4.282992012756e-07,  # c₂ (3 * 1.427664004252e-07)
            -9.246953325960e-10,  # c₃ (4 * -2.311738331490e-10)
            1.502332323102e-12,  # c₄ (5 * 3.004664646204e-13)
            -1.567044722022e-15,  # c₅ (6 * -2.611741203370e-16)
            8.821230212552e-19,  # c₆ (7 * 1.261731858936e-19)
            -2.026478001807e-22,  # c₇ (8 * -2.529347502259e-23)
        ],
    ),
    # Range: 1064.18°C to 1664.5°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (1064.18, 1664.5),
        [
            3.191290037300e-02,  # c₀ (1 * 3.191290037300e-02)
            -4.584515724560e-05,  # c₁ (2 * -2.292257862280e-05)
            2.463663492288e-08,  # c₂ (3 * 8.212211640960e-09)
            -5.867193363460e-12,  # c₃ (4 * -1.466798340865e-12)
        ],
    ),
    # Range: 1664.5°C to 1768.1°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (1664.5, 1768.1),
        [
            3.425605609420e-01,  # c₀ (1 * 3.425605609420e-01)
            -2.075382438718e-04,  # c₁ (2 * -1.037691219359e-04)
            -1.121560165255e-10,  # c₂ (3 * -3.738533884184e-11)
        ],
    ),
]

# Temperature to thermovoltage positive leg (°C to µV)
TEMP_TO_MICROVOLT_POS_LEG = [
    # Range: -50°C to 1064.18°C
    # $ Coefficients of the Positive leg are identical to the the type R thermocouples coefficients
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
    # $ Coefficients of the Positive leg are identical to the the type R thermocouples coefficients
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
    # $ Coefficients of the Positive leg are identical to the the type R thermocouples coefficients
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (1664.5, 1768.1),
        [
            1.522321182090e05,  # c₀
            -2.688198885450e02,  # c₁
            1.712802804710e-01,  # c₂
            -3.458957064530e-05,  # c₃
            -9.346339710460e-12,  # c₄
        ],
    ),
]

# Temperature to thermovoltage negative leg (°C to µV)
TEMP_TO_MICROVOLT_NEG_LEG = [
    # Range: 0°C to 630.615°C
    # $ RN high-purity platinum, Pt vs. Pt = 0µV
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-50, 1768.1),
        [
            0.000000000000e00,  # c₀
        ],
    ),
]

# Seebeck-Koeffizienten positive Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_POS_LEG = [
    # Range: -50°C to 1064.18°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
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
            -2.529347502259e-23,  # c₈ (9 * -2.810386252510e-24)
        ],
    ),
    # Range: 1064.18°C to 1664.5°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (1064.18, 1664.5),
        [
            -2.520612513320e00,  # c₀ (1 * -2.520612513320e00)
            3.191290037300e-02,  # c₁ (2 * 1.595645018650e-02)
            -2.292257862280e-05,  # c₂ (3 * -7.640859475760e-06)
            8.212211640960e-09,  # c₃ (4 * 2.053052910240e-09)
            -1.466798340865e-12,  # c₄ (5 * -2.933596681730e-13)
        ],
    ),
    # Range: 1664.5°C to 1768.1°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (1664.5, 1768.1),
        [
            -2.688198885450e02,  # c₀ (1 * -2.688198885450e02)
            3.425605609420e-01,  # c₁ (2 * 1.712802804710e-01)
            -1.037691219359e-04,  # c₂ (3 * -3.458957064530e-05)
            -3.738533884184e-11,  # c₃ (4 * -9.346339710460e-12)
        ],
    ),
]

# Seebeck-Koeffizienten negative Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_NEG_LEG = [
    # Range: -50°C to 1768.1°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (-50, 1768.1),
        [
            0.0,  # c₀ (Platin-Referenz, Ableitung = 0)
        ],
    ),
]
