"""
Type J Thermocouple (Fe / Cu-Ni) Data and Coefficients

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

Type J Characteristics:
- Positive leg: Iron (Fe)
- Negative leg: Copper-Nickel (Cu-Ni, Constantan)
- Temperature range: -210°C to 1200°C
- EMF range: -8.095 mV to 69.553 mV
- Accuracy: ±2.2°C or ±0.75% (whichever is greater)
- Maximum continuous temperature: 760°C in oxidizing atmosphere
- Good for reducing atmospheres, limited use above 760°C due to oxidation
- Iron leg susceptible to corrosion above 540°C
"""

# Temperature to Voltage Tables (°C to µV)
TEMP_TO_MICROVOLT = [
    # Range: -210°C to 760°C
    # $ Source: NIST Monograph 175, ITS-90, Page 121, Table 6.3.1, Type J thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-210, 760),
        [
            0.000000000000e00,  # c₀
            5.038118781500e01,  # c₁
            3.047583693000e-02,  # c₂
            -8.568106572000e-05,  # c₃
            1.322819529500e-07,  # c₄
            -1.705295833700e-10,  # c₅
            2.094809069700e-13,  # c₆
            -1.253839533600e-16,  # c₇
            1.563172569700e-20,  # c₈
        ],
    ),
    # Range: 760°C to 1200°C
    # $ Source: NIST Monograph 175, ITS-90, Page 121, Table 6.3.1, Type J thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (760, 1200),
        [
            2.964562568100e05,  # c₀
            -1.497612778600e03,  # c₁
            3.178710392400e00,  # c₂
            -3.184768670100e-03,  # c₃
            1.572081900400e-06,  # c₄
            -3.069136905600e-10,  # c₅
        ],
    ),
]

# Voltage to Temperature Tables (µV to °C)
MICROVOLT_TO_TEMP = [
    # Range: -8095µV to 0µV (-210°C to 0°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 303, Table A6.1, Type J thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-8095, 0),
        [
            0.000000000000e00,  # c₀
            1.952826800000e-02,  # c₁
            -1.228618500000e-06,  # c₂
            -1.075217800000e-09,  # c₃
            -5.908693300000e-13,  # c₄
            -1.725671300000e-16,  # c₅
            -2.813151300000e-20,  # c₆
            -2.396337000000e-24,  # c₇
            -8.382332100000e-29,  # c₈
        ],
    ),
    # Range: 0µV to 42919µV (0°C to 760°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 303, Table A6.1, Type J thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 42919),
        [
            0.000000000000e00,  # c₀
            1.978425000000e-02,  # c₁
            -2.001204000000e-07,  # c₂
            1.036969000000e-11,  # c₃
            -2.549687000000e-16,  # c₄
            3.585153000000e-21,  # c₅
            -5.344285000000e-26,  # c₆
            5.099890000000e-31,  # c₇
        ],
    ),
    # Range: 42919µV to 69553µV (760°C to 1200°C)
    # $ Source: NIST Monograph 175, ITS-90, Page 303, Table A6.1, Type J thermocouples
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (42919, 69553),
        [
            -3.113581870000e03,  # c₀
            3.005436840000e-01,  # c₁
            -9.947732300000e-06,  # c₂
            1.702766300000e-10,  # c₃
            -1.430334680000e-15,  # c₄
            4.738860840000e-21,  # c₅
        ],
    ),
]

# Temperature to Seebeck Coefficient Tables (°C to µV/K)
TEMP_TO_SEEBECK = [
    # Range: -210°C to 760°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (-210, 760),
        [
            5.038118781500e01,  # c₀ (1 * c₁ 5.038118781500e01)
            6.095167386000e-02,  # c₁ (2 * c₂ 3.047583693000e-02)
            -2.570431971600e-04,  # c₂ (3 * c₃ -8.568106572000e-05)
            5.291278118000e-07,  # c₃ (4 * c₄ 1.322819529500e-07)
            -8.526479168500e-10,  # c₄ (5 * c₅ -1.705295833700e-10)
            1.256885441820e-12,  # c₅ (6 * c₆ 2.094809069700e-13)
            -8.776837035200e-16,  # c₆ (7 * c₇ -1.253839533600e-16)
            1.250538055760e-19,  # c₇ (8 * c₈ 1.563172569700e-20)
        ],
    ),
    # Range: 760°C to 1200°C
    # $ Source: Derivative of temp_to_microvolt coefficientsf
    (
        (760, 1200),
        [
            -1.497612778600e03,  # c₀ (1 * c₁ -1.497612778600e03)
            6.357420784800e00,  # c₁ (2 * c₂ 3.178710392400e00)
            -9.554306010300e-03,  # c₂ (3 * c₃ -3.184768670100e-03)
            6.288327601600e-06,  # c₃ (4 * c₄ 1.572081900400e-06)
            -1.534568452800e-09,  # c₄ (5 * c₅ -3.069136905600e-10)
        ],
    ),
]

# Temperature to dSeebeck/dT conversion (°C to µV/K²)
TEMP_TO_DSDT = [
    # Range: -210°C to 760°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (-210, 760),
        [
            6.095167386000e-02,  # c₀ (1 * 6.095167386000e-02)
            -5.140863943200e-04,  # c₁ (2 * -2.570431971600e-04)
            1.587383435400e-06,  # c₂ (3 * 5.291278118000e-07)
            -3.410591667400e-09,  # c₃ (4 * -8.526479168500e-10)
            6.284427209100e-12,  # c₄ (5 * 1.256885441820e-12)
            -5.266102421120e-15,  # c₅ (6 * -8.776837035200e-16)
            8.753766390320e-19,  # c₆ (7 * 1.250538055760e-19)
        ],
    ),
    # Range: 760°C to 1200°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (760, 1200),
        [
            6.357420784800e00,  # c₀ (1 * 6.357420784800e00)
            -1.910861202060e-02,  # c₁ (2 * -9.554306010300e-03)
            1.886498280480e-05,  # c₂ (3 * 6.288327601600e-06)
            -6.138273811200e-09,  # c₃ (4 * -1.534568452800e-09)
        ],
    ),
]

# Temperature to Thermovoltage positive leg (°C to µV)
TEMP_TO_MICROVOLT_POS_LEG = [
    # Range: -210°C to 760°C
    # $ Source: NIST Monograph 175, ITS-90, page 133, table 6.4.1 Type JP thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-210, 760),
        [
            0.000000000000e00,  # c₀
            1.791354855900e01,  # c₁
            4.677466335800e-03,  # c₂
            -7.122599299100e-05,  # c₃
            1.335212501600e-07,  # c₄
            -1.500896263900e-10,  # c₅
            1.551431962500e-13,  # c₆
            -7.950357212500e-17,  # c₇
            2.429790391000e-21,  # c₈
        ],
    ),
]

# Temperature to thermovoltage negative leg (°C to µV)
TEMP_TO_MICROVOLT_NEG_LEG = [
    # Range: -210°C to 760°C
    # $ Source: NIST Monograph 175, ITS-90, Page 143, Table 6.5.1, Type JN thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-210, 760),
        [
            0.000000000000e00,  # c₀
            3.246763925600e01,  # c₁
            2.579837059400e-02,  # c₂
            -1.445507273000e-05,  # c₃
            -1.239297209300e-06,  # c₄
            -2.043995698000e-11,  # c₅
            5.433771071800e-14,  # c₆
            -4.588038123500e-17,  # c₇
            1.320193530600e-20,  # c₈
        ],
    ),
]

# Seebeck-Koeffizienten positive Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_POS_LEG = [
    # Range: -210°C to 760°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (-210, 760),
        [
            1.791354855900e01,  # c₀ (1 * 1.791354855900e01)
            9.354932671600e-03,  # c₁ (2 * 4.677466335800e-03)
            -2.136779789730e-04,  # c₂ (3 * -7.122599299100e-05)
            5.340850006400e-07,  # c₃ (4 * 1.335212501600e-07)
            -7.504481319500e-10,  # c₄ (5 * -1.500896263900e-10)
            9.308591775000e-13,  # c₅ (6 * 1.551431962500e-13)
            -5.565250048750e-16,  # c₆ (7 * -7.950357212500e-17)
            1.943832312800e-19,  # c₇ (8 * 2.429790391000e-21)
        ],
    ),
]

# Seebeck-Koeffizienten negative Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_NEG_LEG = [
    # Range: -210°C to 760°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (-210, 760),
        [
            3.246763925600e01,  # c₀ (1 * 3.246763925600e01)
            5.159674118800e-02,  # c₁ (2 * 2.579837059400e-02)
            -4.336521819000e-05,  # c₂ (3 * -1.445507273000e-05)
            -4.957188837200e-06,  # c₃ (4 * -1.239297209300e-06)
            -1.021997849000e-10,  # c₄ (5 * -2.043995698000e-11)
            3.260262643080e-13,  # c₅ (6 * 5.433771071800e-14)
            -3.210626686450e-16,  # c₆ (7 * -4.588038123500e-17)
            1.188174177540e-19,  # c₇ (8 * 1.320193530600e-20)
        ],
    ),
]
