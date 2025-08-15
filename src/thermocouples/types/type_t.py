"""
Type T Thermocouple (Cu / Cu-Ni) Data and Coefficients

Based on NIST Monograph 175 - Temperature-Electromotive Force Reference Functions
and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90.

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

# Temperature to Voltage Tables (°C to µV)
TEMP_TO_MICROVOLT = [
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

# Voltage to Temperature Tables (µV to °C)
MICROVOLT_TO_TEMP = [
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

# Temperature to Seebeck Coefficient Tables (°C to µV/K)
TEMP_TO_SEEBECK = [
    # Range: -270°C to 0°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (-270, 0),
        [
            3.874810636400e01,  # c₀ (1 * c₁ 3.874810636400e01)
            8.838886869400e-02,  # c₁ (2 * c₂ 4.419443434700e-02)
            3.553296931500e-04,  # c₂ (3 * c₃ 1.184432310500e-04)
            8.013189421600e-05,  # c₃ (4 * c₄ 2.003297355400e-05)
            4.506909779500e-06,  # c₄ (5 * c₅ 9.013801955900e-07)
            1.359069395580e-07,  # c₅ (6 * c₆ 2.265115659300e-08)
            2.524990843500e-09,  # c₆ (7 * c₇ 3.607115420500e-10)
            3.079515190640e-11,  # c₇ (8 * c₈ 3.849393988300e-12)
            2.539206932500e-13,  # c₈ (9 * c₉ 2.821352192500e-14)
            1.425159477900e-15,  # c₉ (10 * c₁₀ 1.425159477900e-16)
            5.364928850600e-18,  # c₁₀ (11 * c₁₁ 4.876866228600e-19)
            1.295464712400e-20,  # c₁₁ (12 * c₁₂ 1.079553927000e-21)
            1.812853518060e-23,  # c₁₂ (13 * c₁₃ 1.394502706200e-24)
            1.117132050780e-26,  # c₁₃ (14 * c₁₄ 7.979515392700e-28)
        ],
    ),
    # Range: 0°C to 400°C
    # $ Source: Derivative of temp_to_microvolt coefficients
    (
        (0, 400),
        [
            3.874810636400e01,  # c₀ (1 * c₁ 3.874810636400e01)
            6.658445576000e-02,  # c₁ (2 * c₂ 3.329222788000e-02)
            6.185473021200e-04,  # c₂ (3 * c₃ 2.061824340400e-04)
            -8.752902738400e-06,  # c₃ (4 * c₄ -2.188225684600e-06)
            5.498440464000e-08,  # c₄ (5 * c₅ 1.099688092800e-08)
            -1.848945526320e-10,  # c₅ (6 * c₆ -3.081575877200e-11)
            3.183539470300e-13,  # c₆ (7 * c₇ 4.547913529000e-14)
            -2.201032138400e-16,  # c₇ (8 * c₈ -2.751290167300e-17)
        ],
    ),
]

# Temperature to dSeebeck/dT conversion (°C to µV/K²)
TEMP_TO_DSDT = [
    # Range: -270°C to 0°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (-270, 0),
        [
            8.838886869400e-02,  # c₀ (1 * 8.838886869400e-02)
            7.106593863000e-04,  # c₁ (2 * 3.553296931500e-04)
            2.403956826480e-04,  # c₂ (3 * 8.013189421600e-05)
            1.802763911800e-05,  # c₃ (4 * 4.506909779500e-06)
            6.795346977900e-07,  # c₄ (5 * 1.359069395580e-07)
            1.514994506100e-08,  # c₅ (6 * 2.524990843500e-09)
            2.155660633448e-10,  # c₆ (7 * 3.079515190640e-11)
            2.031365546000e-12,  # c₇ (8 * 2.539206932500e-13)
            1.282643530110e-14,  # c₈ (9 * 1.425159477900e-15)
            5.364928850600e-17,  # c₉ (10 * 5.364928850600e-18)
            1.425164712400e-19,  # c₁₀ (11 * 1.295464712400e-20)
            2.356710723278e-22,  # c₁₁ (12 * 1.812853518060e-23)
            1.562382668092e-25,  # c₁₂ (13 * 1.117132050780e-26)
        ],
    ),
    # Range: 0°C to 400°C
    # $ Source: Derivative of temp_to_seebeck coefficients
    (
        (0, 400),
        [
            6.658445576000e-02,  # c₀ (1 * 6.658445576000e-02)
            1.237094604240e-03,  # c₁ (2 * 6.185473021200e-04)
            -2.625870821520e-05,  # c₂ (3 * -8.752902738400e-06)
            2.199376185600e-07,  # c₃ (4 * 5.498440464000e-08)
            -9.244727631600e-10,  # c₄ (5 * -1.848945526320e-10)
            1.910123682180e-12,  # c₅ (6 * 3.183539470300e-13)
            -1.540722496720e-15,  # c₆ (7 * -2.201032138400e-16)
        ],
    ),
]

# Temperature to Thermovoltage positive leg (°C to µV)
TEMP_TO_MICROVOLT_POS_LEG = [
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
            5.894548226500e01,  # c₁
            1.509134765200e-02,  # c₂
            1.385988324200e-04,  # c₃
            -1.827351164900e-06,  # c₄
            1.033635649100e-08,  # c₅
            -3.065826553400e-11,  # c₆
            4.681530823500e-14,  # c₇
            -2.974071681200e-17,  # c₈
            1.474503431300e-20,  # c₉
            -3.659405308700e-25,  # c₁₀
        ],
    ),
]

# Temperature to Thermovoltage negative leg (°C to µV)
TEMP_TO_MICROVOLT_NEG_LEG = [
    # Range: -270°C to 0°C
    # $ Source: NIST Monograph 175, ITS-90, Page 268, Table 9.5.1, Type TN thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (-270, 0),
        [
            0.000000000000e00,  # c₀
            3.285355813400e01,  # c₁
            2.242088818100e-02,  # c₂
            -1.642329422600e-04,  # c₃
            -2.528317078000e-06,  # c₄
            -4.892249460900e-08,  # c₅
            -1.476011640400e-09,  # c₆
            -3.036321473100e-11,  # c₇
            -3.680094883000e-13,  # c₈
            -2.733196978500e-15,  # c₉
            -1.267705560500e-17,  # c₁₀
            -3.589947524700e-20,  # c₁₁
            -5.682986428000e-23,  # c₁₂
            -3.855137308500e-26,  # c₁₃
        ],
    ),
    # Range: 0°C to 1000°C
    # $ Source: NIST Monograph 175, ITS-90, Page 268, Table 9.5.1, Type TN thermoelements versus platinum, Pt-67
    # $ https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nistmonograph175.pdf
    (
        (0, 1000),
        [
            0.000000000000e00,  # c₀
            3.285355813800e01,  # c₁
            1.820088022700e-02,  # c₂
            6.758360162400e-05,  # c₃
            -3.608745197500e-07,  # c₄
            6.605244362300e-10,  # c₅
            -1.574932377100e-13,  # c₆
            -1.336172944200e-15,  # c₇
            2.227815139100e-18,  # c₈
            -1.474503431300e-21,  # c₉
            3.659405308700e-25,  # c₁₀
        ],
    ),
]

# Seebeck-Koeffizienten positive Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_POS_LEG = [
    # Range: -270°C to 0°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
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
            1.863970303960e-23,  # c₁₂ (13 * 1.433054079200e-24)
            1.117132050780e-26,  # c₁₃ (14 * 7.979515392700e-28)
        ],
    ),
    # Range: 0°C to 1000°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_POS_LEG coefficients
    (
        (0, 400),
        [
            5.894548226500e01,  # c₀ (1 * 5.894548226500e01)
            3.018269530400e-02,  # c₁ (2 * 1.509134765200e-02)
            4.157964972600e-04,  # c₂ (3 * 1.385988324200e-04)
            -7.309404659600e-06,  # c₃ (4 * -1.827351164900e-06)
            5.168178245500e-08,  # c₄ (5 * 1.033635649100e-08)
            -2.146078587380e-10,  # c₅ (6 * -3.065826553400e-11)
            3.277071576450e-13,  # c₆ (7 * 4.681530823500e-14)
            -2.379257345000e-16,  # c₇ (8 * -2.974071681200e-17)
            1.327053088170e-19,  # c₈ (9 * 1.474503431300e-20)
            -3.659405308700e-24,  # c₉ (10 * -3.659405308700e-25)
        ],
    ),
]

# Seebeck-Koeffizienten negative Leg (erste Ableitung, °C zu µV/K)
TEMP_TO_SEEBECK_NEG_LEG = [
    # Range: -270°C to 0°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (-270, 0),
        [
            3.285355813400e01,  # c₀ (1 * 3.285355813400e01)
            4.484177636200e-02,  # c₁ (2 * 2.242088818100e-02)
            -4.926988267800e-04,  # c₂ (3 * -1.642329422600e-04)
            -1.011326831200e-05,  # c₃ (4 * -2.528317078000e-06)
            -2.935349676540e-07,  # c₄ (5 * -4.892249460900e-08)
            -8.856069842400e-09,  # c₅ (6 * -1.476011640400e-09)
            -2.125425031170e-10,  # c₆ (7 * -3.036321473100e-11)
            -2.944075906400e-12,  # c₇ (8 * -3.680094883000e-13)
            -2.459877280650e-14,  # c₈ (9 * -2.733196978500e-15)
            -1.267705560500e-16,  # c₉ (10 * -1.267705560500e-17)
            -3.948942277170e-19,  # c₁₀ (11 * -3.589947524700e-20)
            -7.387882356000e-22,  # c₁₁ (12 * -5.682986428000e-23)
            -5.011678501050e-25,  # c₁₂ (13 * -3.855137308500e-26)
        ],
    ),
    # Range: 0°C to 1000°C
    # $ Source: Derivative of TEMP_TO_MICROVOLT_NEG_LEG coefficients
    (
        (0, 1000),
        [
            3.285355813800e01,  # c₀ (1 * 3.285355813800e01)
            3.640176045400e-02,  # c₁ (2 * 1.820088022700e-02)
            2.027508048720e-04,  # c₂ (3 * 6.758360162400e-05)
            -1.443498079000e-06,  # c₃ (4 * -3.608745197500e-07)
            3.963146617380e-09,  # c₄ (5 * 6.605244362300e-10)
            -9.449594262600e-13,  # c₅ (6 * -1.574932377100e-13)
            -9.353210609400e-15,  # c₆ (7 * -1.336172944200e-15)
            1.782252111280e-17,  # c₇ (8 * 2.227815139100e-18)
            -1.327053088170e-20,  # c₈ (9 * -1.474503431300e-21)
            3.659405308700e-24,  # c₉ (10 * 3.659405308700e-25)
        ],
    ),
]
